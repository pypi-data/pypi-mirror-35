# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 13:51:22 2015

@author: twagner
"""

### imports ###################################################################
import logging

### imports from ##############################################################
from ctypes import c_double
from inspect import stack

#### logging ##################################################################
logging.getLogger('owis').addHandler(logging.NullHandler())

###############################################################################
class Axis(object):
    def __init__(self, dll, controller, axis):
        self.logger = logging.getLogger('owis')
        
        self.axis = axis
        self.controller = controller
        self.dll = dll
        self.offsetMark = 0.       
        self.refMode = 4
        self._targetMode = 0
        self._targetEx = 0
        self.unit = '--'        

    ### properties ###
    #%%
    @property
    def accel(self):
        propertyName = stack()[0][3]
        return self.getProperty(propertyName)
        
    @accel.setter
    def accel(self, value):
        propertyName = stack()[0][3]
        self.setProperty(propertyName, value)

        
    #%%
    @property
    def conversion(self):
        propertyName = stack()[0][3]
        return self.getProperty(propertyName)
       
    @conversion.setter
    def conversion(self, value):
        propertyName = stack()[0][3]
        self.setProperty(propertyName, value)

        
    #%%
    @property
    def errorState(self):
        propertyName = stack()[0][3]
        return self.getProperty(propertyName)

    @errorState.setter
    def errorState(self, value):
        if hasattr(self.dll, 'errorState'):
            self.dll.errorState[self.axis - 1] = value        

    #%%
    @property
    def fastRefF(self):
        propertyName = stack()[0][3]
        return self.getProperty(propertyName)

    @fastRefF.setter
    def fastRefF(self, value):
        propertyName = stack()[0][3]
        self.setProperty(propertyName, value)
            
    #%%
    @property
    def frequency(self):
        propertyName = stack()[0][3]
        return self.getProperty(propertyName)

    @frequency.setter
    def frequency(self, value):
        propertyName = stack()[0][3]
        self.setProperty(propertyName, value)
        
    #%%
    @property
    def limitMax(self):
        propertyName = stack()[0][3]
        return self.getProperty(propertyName)

    @limitMax.setter
    def limitMax(self, value):
        propertyName = stack()[0][3]
        self.setProperty(propertyName, value)

        
    #%%
    @property
    def limitMin(self):
        propertyName = stack()[0][3]
        return self.getProperty(propertyName)

    @limitMin.setter
    def limitMin(self, value):
        propertyName = stack()[0][3]
        self.setProperty(propertyName, value)

        
    #%%
    @property
    def moveState(self):
        propertyName = stack()[0][3]
        return self.getProperty(propertyName)

        
    #%%
    @property
    def posF(self):
        '''
        read positioning velocity of an axis (values in Hz)
        '''
        propertyName = stack()[0][3]
        return self.getProperty(propertyName)
        
    @posF.setter
    def posF(self, value):
        propertyName = stack()[0][3]
        self.setProperty(propertyName, value)


    #%%
    @property
    def position(self):
        propertyName = stack()[0][3]
        return self.getProperty(propertyName)
        
    #%%
    @property
    def positionEx(self):
        propertyName = stack()[0][3]
        return self.getProperty(propertyName)
        
    #%%
    @property
    def posRange(self):
        propertyName = stack()[0][3]
        return self.getProperty(propertyName)
        
    #%%
    @property
    def refDecel(self):
        propertyName = stack()[0][3]
        return self.getProperty(propertyName)
        
    @refDecel.setter
    def refDecel(self, value):
        propertyName = stack()[0][3]
        self.setProperty(propertyName, value)
        
    #%%
    @property
    def refReady(self):
        '''
        read positioning velocity of an axis (values in Hz)
        '''
        propertyName = stack()[0][3]
        return self.getProperty(propertyName)
        
    #%%
    @property
    def refSwitch(self):
        propertyName = stack()[0][3]
        return self.getProperty(propertyName)

    #%%
    @property
    def refSwitchMode(self):
        propertyName = stack()[0][3]
        return self.getProperty(propertyName)

    #%%
    @property
    def slowRefF(self):
        propertyName = stack()[0][3]
        return self.getProperty(propertyName)
        
    @slowRefF.setter
    def slowRefF(self, value):
        propertyName = stack()[0][3]
        self.setProperty(propertyName, value)
        
    #%%
    @property
    def targetEx(self):
        propertyName = stack()[0][3]
        return self.getProperty(propertyName)

    @targetEx.setter
    def targetEx(self, position):
        propertyName = stack()[0][3]
        value = c_double(position)
        self.setProperty(propertyName, value)
        
    #%%
    @property
    def targetMode(self):
        propertyName = stack()[0][3]
        return self.getProperty(propertyName)

    @targetMode.setter        
    def targetMode(self, value):
        propertyName = stack()[0][3]
        self.setProperty(propertyName, value)
        
    ### methods ###
    def getProperty(self, propertyName):
        methodName = 'PS10_Get' + propertyName[0].upper() + propertyName[1:]
        getMethod = getattr(self.dll, methodName)
        value = getMethod(self.controller, self.axis)

        self.getReadError(propertyName)

        attributeName = '_' + propertyName
        setattr(self, attributeName, value)
        
        return value
            
    def getReadError(self, propertyName):        
        error = self.dll.PS10_GetReadError(self.controller)

        if error:
            self.logger.error(
                "Error getting axis %s %s: %s",
                self.axis, propertyName, error
            )
            
        return error
        
    def setProperty(self, propertyName, value):        
        methodName = 'PS10_Set' + propertyName[0].upper() + propertyName[1:]
        setMethod = getattr(self.dll, methodName)
        error = setMethod(self.controller, self.axis, value)
        
        if error:
            self.logger.error(
                "Error setting axis %i %s to %s: %i",
                self.axis, propertyName, value, error
            )

        propertyValue = getattr(self, propertyName)
            
        if (value != propertyValue):
            self.logger.error(
                "Axis %i %s value %s differs from %s",
                self.axis, propertyName, value, propertyValue
            )
            
        return error
   
    def goRef(self):
        self.logger.debug("Going to axis %i reference position", self.axis)
            
        error = self.dll.PS10_GoRef(self.controller, self.axis, self.refMode)

        if error:
            self.logger.error(
                "Could not go to axis %i reference position in mode %i: %i",
                self.axis, self.refMode, error
            )

        return error

    def goTarget(self):
        error = self.dll.PS10_GoTarget(self.controller, self.axis)

        if error:
            self.logger.error(
                "Could not go to axis %i target: %i",
                self.axis, error
            )

        return error

    #%%
    def motorInit(self):
        '''
        initialize an axis and switch on.

        With this function the axis is completely initialized and afterwards is
        with a current and with active positioning regulator. It must be
        executed after the turning on of the control unit, so that the axis can
        be moved afterwards with the commands REF, PGO, VGO etc. Before the
        following parameters must have been set:
            - limit switch mask,
            - polarity,
            - start regulator parameters.
        '''

        self.logger.debug("Initialising axis %i", self.axis)
        error = self.dll.PS10_MotorInit(self.controller, self.axis)

        if error:
            self.logger.debug(
                "Error initialising axis %i: %i", self.axis, error
            )

        return error

    def motorOn(self):
        self.logger.info("Switching on axis %i", self.axis)
        error = self.dll.PS10_MotorOn(self.controller, self.axis)

        if error:
            self.logger.error(
                "Error switching on axis %i: %i", self.axis, error
            )

    def motorOff(self):
        self.logger.info("Switching off axis %i", self.axis)
        error = self.dll.PS10_MotorOff(self.controller, self.axis)

        if error:
            self.logger.error(
                "Error switching off axis %i: %i", self.axis, error
            )

    def moveAbsolute(self, position):
        self.setTargetAbsolute()

        error = self.dll.PS10_MoveEx(
            self.controller, self.axis, c_double(position), 1
        )
        
        if error:
            self.logger.error(
                "Error moving axis %i to %f: %s", self.axis, position, error
            )
            
        return error
            
    def moveRelative(self, position):
        self.setTargetRelative()

        error = self.dll.PS10_MoveEx(
            self.controller, self.axis, c_double(position), 1
        )
        
        if error:
            self.logger.error(
                "Error moving axis %i a distance of %f: %s",
                self.axis, position, error
            )
            
        return error

    def setTargetAbsolute(self):
        self.targetMode = 1

    def setTargetRelative(self):
        self.targetMode = 0

    def stop(self):
        self.logger.info("Stopping axis %i", self.axis)
        error = self.dll.PS10_Stop(self.controller, self.axis)

        if error:
            self.logger.error("error stopping axis: %s", error)
