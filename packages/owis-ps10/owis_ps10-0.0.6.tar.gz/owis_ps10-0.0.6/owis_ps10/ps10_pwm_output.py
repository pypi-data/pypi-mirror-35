# -*- coding: utf-8 -*-

### imports ###################################################################
import logging

#### logging ##################################################################
logging.getLogger('owis').addHandler(logging.NullHandler())

###############################################################################
class PwmOutput(object):
    def __init__(self, dll, controller, pin):
        self.logger = logging.getLogger('owis')

        self.dll = dll
        self.controller = controller
        self.pin = pin

    ### properties
    @property
    def value(self):
        self._value = self.dll.PS10_GetPwmOutput(self.controller, self.pin)
        error = self.dll.PS10_GetReadError(self.controller)
        
        if error:
            self.logger.error(
                "Error getting PWM output from pin %i: %i", self.pin, error
            )
        else:
            self.logger.debug("PWM pin %i: %s", self.pin, self._value)
                
        return self._value        

    @value.setter
    def value(self, value):

        error = self.dll.PS10_SetPwmOutput(self.controller, self.pin, value)

        if error:
            self.logger.error(
                "Error setting PWM pin %i to %s: %i", self.pin, value, error)
        else:
            self.logger.debug("PWM pin %i output: %s", self.pin, value)
