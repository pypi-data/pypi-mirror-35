# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 13:51:22 2015

@author: twagner
"""

### imports ###################################################################
import logging
import threading
import time

#### logging ##################################################################
logging.getLogger('owis').addHandler(logging.NullHandler())
   
###############################################################################
class PS10_Mock:
    """
    emulation of essential PS10 DLL commands
    """

    def __init__(self):
        self.logger = logging.getLogger('owis')

        self.jobs = []
        self.voltage = 0.0
        self.refMode = 4
        
        self.digitalInput = [1, 1, 1, 1, 1]
        self.digitalOutput = [0, 0, 0, 0, 0]

        self._accel = [0, 0]
        self._conversion = [1e-4, 9e-3]
        self.errorState = [0, 0]
        self._fastRefF = [0, 0]
        self._frequency = [0, 0]
        self._limitMax = [0, 0]
        self._limitMin = [0, 0]
        self._moveState = [0, 0]
        self._outputMode = 0
        self._posF = [0, 0]
        self._position = [0., 0.]
        self._pwmOutput = 0
        self._refReady = [0, 0]
        self._slowRefF = [0, 0]
        self._targetMode = 0

    def goRefWorker(self, axis):
        self.logger.info('moving axis %i to reference', axis)

        time.sleep(1)

        self._moveState[axis - 1] = 0
        self._refReady[axis - 1] = 1
        
        self.logger.info('finished moving axis %i to reference', axis)

    def PS10_CheckMem(self, controller):
        return 0

    def PS10_Connect(
        self, controller, interface, com, baud, handshake, bit1, bit2, bit3
    ):
        return 0
    
    def PS10_Disconnect(self, controller):
        for job in self.jobs:
            job.join()
            
        return 0
        
    def PS10_Stop(self, controller, axis):
        return False

    #%%
    def PS10_GetAccel(self, controller, axis):
        return self._accel[axis - 1]

    def PS10_SetAccel(self, controller, axis, value):
        self._accel[axis - 1] = value
    
    #%%
    def PS10_GetAnalogInput(self, controller, pin):
        value = self.voltage
        return value

    #%%
    def PS10_GetCanOpenSlave(self, slaveNumber):
        return 0

    def PS10_SetCanOpenSlave(self, slaveNumber, slaveID):
        return 0
    
    #%%
    def PS10_GetDigitalInput(self, controller, pin):
        return self.digitalInput[pin - 1]

    #%%
    def PS10_GetDigitalOutput(self, controller, pin):
        return self.digitalOutput[pin - 1]

    def PS10_SetDigitalOutput(self, controller, pin, state):
        self.digitalOutput[pin - 1] = state
        return 0

    #%%
    def PS10_GetEmergencyInput(self, controller):
        return False

    #%%
    def PS10_GetErrorState(self, controller, axis):
        return self.errorState[axis - 1]

    #%%
    def PS10_GetF(self, controller, axis):
        return self._frequency[axis - 1]

    def PS10_SetF(self, controller, axis, value):
        self._frequency[axis - 1] = value

    #%%
    def PS10_GetFastRefF(self, controller, axis):
        return self._fastRefF[axis - 1]

    def PS10_SetFastRefF(self, controller, axis, value):
        self._fastRefF[axis - 1] = value

    #%%%
    def PS10_GetLimitMax(self, controller, axis):
        return self._limitMax[axis - 1]

    def PS10_SetLimitMax(self, controller, axis, value):
        self._limitMax[axis - 1] = value

    #%%
    def PS10_GetLimitMin(self, controller, axis):
        return self._limitMin[axis - 1]

    def PS10_SetLimitMin(self, controller, axis, value):
        self._limitMin[axis - 1] = value

    #%%
    def PS10_GetMoveState(self, controller, axis):
        return self._moveState[axis - 1]
        
    #%%
    def PS10_GetOutputMode(self, controller):
        return self._outputMode

    def PS10_SetOutputMode(self, controller, mode):
        self._outputMode = mode

    #%%
    def PS10_GetPosF(self, controller, axis):
        return self._posF[axis - 1]

    def PS10_SetPosF(self, controller, axis, value):
        self._posF[axis - 1] = value

    #%%
    def PS10_GetPosition(self, controller, axis):
        position = self._position[axis - 1]
        return position

    #%%
    def PS10_GetPositionEx(self, controller, axis):
        return 0

    #%%
    def PS10_GetPwmOutput(self, controller, pin):
        return self._pwmOutput

    def PS10_SetPwmOutput(self, controller, pin, value):
        self._pwmOutput = value
        return 0
    
    #%%
    def PS10_GetReadError(self, controller):
        error = False
        return error

    #%%
    def PS10_GetRefDecel(self, controller, axis):
        return 0
        
    def PS10_SetRefDecel(self, controller, axis, value):
        self._refDecel = value

        
    def PS10_GetRefReady(self, controller, axis):
        return self._refReady[axis - 1]

    def PS10_GetRefSwitch(self, controller, axis):
        return 0

    def PS10_GetRefSwitchMode(self, controller, axis):
        return 0

    #%%
    def PS10_GetSlaves(self, controller):
        return 0

    #%%
    def PS10_GetSlowRefF(self, controller, axis):
        return self._slowRefF[axis - 1]

    def PS10_SetSlowRefF(self, controller, axis, value):
        self._slowRefF[axis - 1] = value

    #%%
    def PS10_GoRef(self, controller, axis, mode):

        self._moveState[axis - 1] = 3

        t = threading.Thread(
            target = self.goRefWorker, args = (axis,)
        )

        t.start()

        return 0

    def PS10_MotorInit(self, controller, axis):
        return 0

    def PS10_MotorOff(self, controller, axis):
        pass

    def PS10_MoveEx(self, controller, axis, position, flag):
        if self._targetMode == 0:
            self._position[axis - 1] += position.value
        elif self._targetMode == 1:
            self._position[axis - 1] = position.value
            
        return 0

    def PS10_SetCoversion(self, controller, axis, vaule):
        return 0
        
    def PS10_GetTargetMode(self, controller, axis):
        return self._targetMode
        
    def PS10_SetTargetMode(self, controller, axis, value):
        self._targetMode = value
        return 0
