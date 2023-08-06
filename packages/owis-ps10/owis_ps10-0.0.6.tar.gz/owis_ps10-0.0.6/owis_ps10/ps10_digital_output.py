# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 13:51:22 2015

@author: twagner
"""

### imports ###################################################################
import logging

#### logging ##################################################################
logging.getLogger('owis').addHandler(logging.NullHandler())

###############################################################################
class DigitalOutput(object):
    def __init__(self, dll, controller, pin):
        self.logger = logging.getLogger('owis')

        self.dll = dll
        self.controller = controller
        self.pin = pin
        self._previousValue = 0
        self._value = 0
        self.verbosity = 2

    ### properties
    @property
    def value(self):
        self._previousValue = self._value
        self._value = self.dll.PS10_GetDigitalOutput(self.controller, self.pin)
        error = self.dll.PS10_GetReadError(self.controller)
        
        if error:
            self.logger.error(
                "Error getting digital output %i: %i", self.pin, error
            )

        elif self.verbosity == 1:
            if self._value != self._previousValue:
                self.logger.debug(
                    "Digital output pin %i: %i -> %i",
                    self.pin, self._previousValue, self._value
                )

        elif self.verbosity == 2:
            self.logger.debug(
                "Digital output pin %i: %i", self.pin, self._value
            )
                
        return self._value

    @value.setter
    def value(self, state):
        error = self.dll.PS10_SetDigitalOutput(
            self.controller, self.pin, state
        )
        
        if error:
            self.logger.error(
                "Error setting digital output pin %i: %i", self.pin, error
            )
        else:
            self._value = state
            self.logger.debug("Digital output pin %i: %i", self.pin, state)
