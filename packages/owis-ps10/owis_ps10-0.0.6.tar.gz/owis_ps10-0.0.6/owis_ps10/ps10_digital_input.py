# -*- coding: utf-8 -*-

### imports ###################################################################
import logging

###############################################################################
class DigitalInput(object):
    def __init__(self, dll, controller, pin):
        self.logger = logging.getLogger('owis')
        self.dll = dll
        self.controller = controller
        self.pin = pin
        self.verbosity = 1
        
        self._previousValue = None
        self._value = None

    @property
    def value(self):
        self._previousValue = self._value
        self._value = self.dll.PS10_GetDigitalInput(self.controller, self.pin)
        error = self.dll.PS10_GetReadError(self.controller)
        
        if error:
            self.logger.error(
                "Error getting digital input from pin %i: %i", self.pin, error
            )
            
        elif self.verbosity == 1:
            if self._value != self._previousValue:
                self.logger.debug(
                    "Digital input pin %i: %i", self.pin, self._value
                )
                
                self._previousValue = self._value

        elif self.verbosity == 2:
            self.logger.debug(
                "Digital input pin %i: %i", self.pin, self._value
            )
               
        return self._value


    @value.setter
    def value(self, value):
        if hasattr(self.dll, 'digitalInput'):
            self._value = value
            self.dll.digitalInput[self.pin - 1] = value
