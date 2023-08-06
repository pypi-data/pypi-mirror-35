# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 13:51:22 2015

@author: twagner
"""

### imports ###################################################################
import logging
import os
import serial.tools.list_ports
import time
import yaml

### imports from ##############################################################
from ctypes import c_char_p, c_double, c_int

if os.name != 'posix':
    from ctypes import WinDLL

### relative imports ##########################################################
from .ps10_analog_input import AnalogInput
from .ps10_axis import Axis
from .ps10_digital_input import DigitalInput
from .ps10_digital_output import DigitalOutput
from .ps10_mock import PS10_Mock

#### logging ##################################################################
logging.getLogger('owis').addHandler(logging.NullHandler())

class Position:
    def __init__(self):
        self.lrt = 0.0
        self.drt = 0.0

###############################################################################
class PS10(object):
    """
    Hardware controller interface.
    """
    
    MAX_TRY = 3

    def __init__(self, filename):
        self.logger = logging.getLogger('owis')
        self.logger.info("Starting OWIS PS10-32 controller")

        with open(filename) as f:    
            self.hardwareParameter = yaml.load(f)

        self.com = None
        self.controller = 1
        self.N_aIn = 4
        self.N_digOut = 5
        self.N_digIn = 4
        self.N_pwm = 2

        '''
            0: success
            -1: function error
            -2: communication error
            -3: syntax error
        '''
        self.error = 0

        self._emergency = 0
        self._emergencyPressed = False
        self._emergencyReleased = False
        self._outputMode = 0
        self._prevEmergency = 0

        self.port = None
        self._slaves = None
        self._serialNumber = 20 * ' '

        self.AXIS_LRT = 1
        self.AXIS_DRT = 2
 
        self.conv_axis = {self.AXIS_LRT : 1e-4, self.AXIS_DRT : 9e-3}

        self.reference = Position()

        self.maxReferenceState = 0
        self.maxPosition = 1e3
        self.needReference = True
        self.needVacuum = True
        self.offsetMark = 0
        self.referenceState = 0

        self.detectPort()

        self.baudrate = self.hardwareParameter['baudrate']
        self.dllfile = self.hardwareParameter['dllfile']
        self.logging = self.hardwareParameter['logging']
        self.logfile = self.hardwareParameter['logfile']
        self.timeout = self.hardwareParameter['timeout']

        for key, value in self.hardwareParameter.items():
            if key == 'needReference':
                self.needReference = value
            elif key == 'needVacuum':
                self.needVacuum = value
            elif key == 'offsetMark':
                self.offsetMark = value

        if self.com is not None:

            self.loadDLL(self.dllfile)
            
            interface = 0
    
            self.connect(
                self.controller, interface, self.com, self.baudrate,
                self.timeout
            )

        if self.error or (self.com is None):
            self.logger.warning("Switching to hardware emulator")
            self.dll = PS10_Mock()

        self.setCanOpenSlave(101, 1)
        self.getCanOpenSlave()

        if self.logging:
            self.initLogging()
        
        self.initAxes()
        self.initAnalogInput()
        self.initDigitalInput()
        self.initDigitalOutput()

        self.vacuumOutput = self.digitalOutput[0]
        self.vacuumInput = self.digitalInput[0]
        
        self.axes[0].motorInit()
        self.axes[1].motorInit()

        # using the method call leads to strange conversion erros
        self.axes[0].limitMax = 700000
        self.axes[0].limitMin = 0
        
        # set conversion
        # self.axes[0].conversion = 1E-4
        # self.axes[1].conversion = 9E-3

        self.axes[0].offsetMark = 0.
        self.axes[1].offsetMark = 0.


    def initAnalogInput(self):
        self.analogInput = []
        
        for i in range(self.N_aIn):
            analogInput = AnalogInput(self.dll, self.controller, i + 1)
            self.analogInput.append(analogInput)

    def initAxes(self):
        self.axes = []
        
        axesDict = self.hardwareParameter['axes']
        
        for a in axesDict:
            index = a['index']
            axisName = "axis" + a['name']
            
            axis = Axis(self.dll, self.controller, index)
            
            setattr(self, axisName, axis)
            self.axes.append(axis)

            for key in a.keys():            
                setattr(axis, key, a[key])

        for a in axesDict:
            axisName = "axis" + a['name']
            axis = getattr(self, axisName)
            
            for key in a.keys():            
                value = getattr(axis, key)

                self.logger.debug('%s %s = %s', axisName, key, value)
        
    def initDigitalInput(self):
        self.digitalInput = []
        
        for i in range(self.N_digIn):
            digInput = DigitalInput(self.dll, self.controller, i + 1)
            self.digitalInput.append(digInput)

    def initDigitalOutput(self):
        self.digitalOutput = []
        
        for i in range(self.N_digOut):
            output = DigitalOutput(self.dll, self.controller, i + 1)
            self.digitalOutput.append(output)
           
    def initLogging(self):
        self.logger.info(
            "Start logging to %s", self.logfile
        )
        
        filename = c_char_p(self.logfile)

        try:
            error = self.dll.PS10_LogFile(self.controller, 1, filename, 0, 1)
        except WindowsError:
            error = 99

        if error:
            self.logger.error(
                "Could not start logging to %s: %i", filename, error
            )

    #%% properties
    @property
    def checkSumMem(self):
        self._checkSum = self.dll.PS10_CheckMem(self.controller)
        error = self.dll.PS10_GetReadError(self.controller)

        if error:
            self.logger.error("Error getting memory check sum: %i", error)
        
        return self._checkSum

    #%%
    @property
    def emergency(self):
        self._prevEmergency = self._emergency
        self._emergency = self.dll.PS10_GetEmergencyInput(self.controller)

        if self._prevEmergency == 0 and self._emergency == 1:
            self._emergencyReleased = True
            
            self.logger.warning('Emergency input released')
        
        elif self._prevEmergency == 1 and self._emergency == 0:
            self._emergencyPressed = True

            self.logger.warning('Emergency input pressed')

        return self._emergency

    #%%
    @property
    def emergencyPressed(self):
        value = self._emergencyPressed
        self._emergencyPressed = False
        return value

    #%%
    @property
    def emergencyReleased(self):
        value = self._emergencyReleased
        self._emergencyReleased = False
        return value

    #%%
    @property
    def outputMode(self):
        self.logger.debug('Getting output mode')

        mode = self.dll.PS10_GetOutputMode(self.controller)
        error = self.dll.PS10_GetReadError(self.controller)
        
        if error:
            self.logger.error("Error getting output mode")
        else:
            self._outputMode = mode
            
            if mode == 0:
                self.logger.debug(
                    "pin 1: digital SPS-output," +
                    "pin 2: digital SPS-output"
                )
            elif mode == 1:
                self.logger.debug(
                    "pin 1: digital SPS-output," +
                    "pin 2: PWM-output"
                )
            elif mode == 2:
                self.logger.debug(
                    "pin 1: PWM-output," +
                    "pin 2: PWM-output")
                
        return mode

    @outputMode.setter
    def outputMode(self, mode):
        self.error = self.dll.PS10_SetOutputMode(self.controller, mode)

        if self.error:
            self.logger.error("Error setting output mode to %s", mode)
        else:
            self._outputMode = self.dll.PS10_GetOutputMode(self.controller)

    #%%
    @property
    def serialNumber(self):
        strBuffer = 20 * ' '
        bufSize = self.dll.PS10_GetSerNumber(1, strBuffer, 20)
        
        self._serialNumber = strBuffer[:bufSize]

        return self._serialNumber


    #%%
    @property
    def slaves(self):
        self._slaves = self.dll.PS10_GetSlaves(self.controller)
        error = self.dll.PS10_GetReadError(self.controller)

        if error:
            self.logger.error("Error getting slaves: %i", error)

        return self._slaves


    #%% methods 
    def connect(self, controller, interface, com, baud, timeout):
        self.logger.debug("Connecting to PS10")
        
        self.error = self.dll.PS10_Connect(
            controller, interface, com, baud, timeout,
            0, 0, 0
        )

        if self.error:
            self.logger.error("Could not connect to PS10: %s", self.error)
        else:
            self.controller = controller
            self.interface = interface
            
            self.logger.debug(
                "Connected to PS10(%s, %s)", controller, interface
            )
            
        return self.error

        
    def detectPort(self):
        ports = list(serial.tools.list_ports.comports())
        self.port = None
        self.com = None

        if len(ports) == 0:
            self.logger.warning("Could not find any serial device!")

        for p in ports:
            if 'STMicroelectronics Virtual COM Port' in p[1]:
                self.logger.debug(p[1])
                self.logger.debug(p[2])
                self.com = int(p[0][3])

                self.port = p                
                
        return self.com


    def loadDLL(self, dllFile):
        self.logger.debug("Loading %s", dllFile)
       
        if os.path.exists(dllFile):
            self.dll = WinDLL(dllFile)
        else:
            self.logger.error("Could not find %s", dllFile)

        self.dll.PS10_GetSerNumber.argtypes = [c_int, c_char_p, c_int]
        self.dll.PS10_GetPositionEx.restype = c_double


    def moveRef(self):
        self.logger.info("Going to reference position")

        error = self.axisLRT.goRef()
        
        if error:
            self.logger.error(
                "Setting axis 1 reference position failed: %i",
                error
            )
            
            # return

        time.sleep(1.0)        
        error = self.axisDRT.goRef()        

        if error:
            self.logger.error(
                "Setting axis 2 reference position failed: %i",
                error
            )
            
            # return

        while self.axisLRT.moveState:
            self.logger.debug("LRT move state: %i", self.axisLRT.moveState)
            time.sleep(0.1)

        while self.axisDRT.moveState:
            self.logger.debug("DRT move state: %i", self.axisDRT.moveState)
            time.sleep(0.1)

        '''
        while not self.axisLRT.refReady:
            time.sleep(0.1)

        while not self.axisDRT.refReady:
            time.sleep(0.1)
        '''

        self.logger.debug("DRT axis ready: %i", self.axisDRT.refReady)

        self.reference.lrt = self.getPosition(self.AXIS_LRT)
        self.reference.drt = self.getPosition(self.AXIS_DRT)

        self.logger.info("Reference position reached")

        self.getCurrentPosition()
        
        self.logger.info(
            "Position: %i, %i", self.axisLRT.position, self.axisDRT.position
        )

        self.logger.info(
            "Position: %i, %i", self.axisLRT.positionEx, self.axisDRT.positionEx
        )

        
    def getCurrentPosition(self):
        lrt = self.getPosition(self.AXIS_LRT)
        drt = self.getPosition(self.AXIS_DRT)

        self.logger.debug(
            "current position: %0.1f %s, %0.1f %s",
            lrt, self.axisLRT.unit,
            drt, self.axisDRT.unit
        )

        return lrt, drt
    
    
    def getPosition(self, axis):
        position = self.dll.PS10_GetPosition(self.controller, axis)
        error = self.dll.PS10_GetReadError(self.controller)

        position *= self.conv_axis[axis]

        if axis == self.AXIS_DRT:
            position += self.offsetMark
        
        if error:
            self.logger.error("Error getting axis %i position", axis)
            
        return position


    def checkReference(self, axis):
        self.referenceState &= (0 << (axis-1))
        '''
        reset reference state for axis:
            - workaround to keep reference state even if the axis was shut down
              due to light curtain obstruction
            - the real reference state will be ignored once it was set at least
              one time
            - this will also turn off software limits
        '''
        self.referenceState |= (self.maxReferenceState << (axis-1)) 

        if self.needReference:
            refState = self.dll.PS10_GetRefReady(self.controller, axis)
            self.maxReferenceState |= (refState << (axis-1))
            # set reference state for axis
            self.referenceState |= (refState << (axis-1))
        else:
            self.maxReferenceState |= (1 << (axis-1))
            self.referenceState |= (1 << (axis-1))

        return self.maxReferenceState & (1 << (axis - 1)) > 0


    def moveRelative(self, axis, position, wait = False):
        self.checkReference(axis)
        
        self.logger.info(
            "Moving axis %s a distance of %s %s",
            axis, position, self.axes[axis-1].unit
        )

        if(
            self.needVacuum and
            axis == self.AXIS_DRT and (
                self.vacuumOutput.value == 0 or
                self.vacuumInput.value == 0
            )
        ):
            # if no vacuum, don't move DRT
            self.logger.warning("Vacuum needed for axis %s", axis)
            return

        if(
            axis == self.AXIS_LRT and
            (self.getPosition(axis) + position) > self.maxPosition
        ):
            # software limit of LRT movement
            self.logger.warning("movement would hit limit ... abort")
            return

        if self.axes[axis-1].moveState > 0:
            # if axis is moving, don't do anything
            self.logger.warning("axis %s is already moving", axis)
            return

        if not self.referenceState & (1 << (axis-1)):
            # if no reference for axis is set, don't move
            self.logger.warning("no reference for axis %s", axis)
            return


        self.axes[axis - 1].moveRelative(position)
            

        if wait:
            while self.axes[axis-1].moveState != 0:
                pass


    def moveAbsolute(self, axis, position, wait = False):
        self.checkReference(axis)

        self.logger.info(
            "moving axis %s a distance of %s %s",
            axis, position, self.axes[axis-1].unit
        )

        if(
            self.needVacuum and
            axis == self.AXIS_DRT and
            (self.vacuumOutput.value == 0 or
            self.vacuumInput.value == 0)
        ): # if no vacuum, don't move DRT
            self.logger.warning("vacuum needed for axis %s", axis)
            return

        if axis == self.AXIS_LRT and position > self.maxPosition:
            # software limit of LRT movement
            self.logger.warning(
                "movement would hit software limit %s abort",
                self.maxPosition
            )
            return

        if self.axes[axis - 1].moveState > 0:
            # if axis is moving, don't do anything
            self.logger.warning("axis %s is already moving", axis)
            return

        if not self.referenceState & (1 << (axis-1)):
            # if no reference for axis is found, don't move
            self.logger.error("no reference for axis %s", axis)
            return

        if axis == self.AXIS_DRT: # if DRT apply position offset
            position -= self.offsetMark

        self.axes[axis - 1].moveAbsolute(position)

        if wait:
            while self.getMoveState(axis) != 0:
                pass


    def setCanOpenSlave(self, slaveNumber, slaveID):
        self.slaveNumber = slaveNumber
        self.slaveID = slaveID

        self.logger.debug(
            "setting CanOpen slave: (" +
            str(slaveNumber) + ", " +  str(slaveID) + ")"
        ) 

        
        error = self.dll.PS10_SetCanOpenSlave(slaveNumber, slaveID)
        
        if error:
            self.logger.error("Error:", error)


    def getCanOpenSlave(self, slaveNumber = None):

        if slaveNumber == None:
            slaveNumber = self.slaveNumber
            
        if slaveNumber > 100:
            self.slaveID = self.dll.PS10_GetCanOpenSlave(slaveNumber)
            error = self.dll.PS10_GetReadError(self.controller)
        else:
            error = -4

        if error:
            self.logger.error("Error getting slaveID:", error)

        return self.slaveID


    def disconnect(self):
        error = self.dll.PS10_Disconnect(self.controller)

        self.logger.debug(
            "Disconnecting from PS10 controller %s", self.controller
        )

        if error:
            self.logger.error("Error disconnecting PS10 controller: %s", error)
            
        return error


    def simpleConnect(self, controller):
        self.logger.debug("Connecting to PS10")
        
        serialNumber = '15050140'
        
        self.error = self.dll.PS10_SimpleConnect(
            controller, serialNumber
        )

        if self.error:
            self.logger.warning("Could not connect to PS10: %s", self.error)
        else:
            self.controller = controller
            
            self.logger.debug(
                "Connected to PS10(%s, %s)", controller, serialNumber
            )
            
        return self.error
