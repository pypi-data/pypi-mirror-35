# -*- coding: utf-8 -*-

### imports ###################################################################
import logging

#### logging ##################################################################
logging.getLogger('owis').addHandler(logging.NullHandler())

###############################################################################
class AnalogInput(object):
    def __init__(self, dll, controller, pin):
        self.logger = logging.getLogger('owis')
        self.dll = dll
        self.controller = controller
        self.pin = pin
        self.verbosity = 1
        
        self._value = None

    @property
    def value(self):
        self._previousValue = self._value
        self._value = self.dll.PS10_GetAnalogInput(self.controller, self.pin)
        error = self.dll.PS10_GetReadError(self.controller)
        
        if error:
            self.logger.error(
                "Error getting analog input from pin %i: %i", self.pin, error
            )
            
        elif self.verbosity == 1:
            if self._value != self._previousValue:
                self.logger.debug(
                    "Analog input pin %i: %i", self.pin, self._value
                )
                
                self._previousValue = self._value

        elif self.verbosity == 2:
            self.logger.debug(
                "Analog input pin %i: %i", self.pin, self._value
            )
               
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        
        self.dll.analogInput[self.pin - 1] = value
