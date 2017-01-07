__author__ = 'Perkel'

import moving_variable_settings
import moving_variablesB

moving_variable_settings.counter2 = 50
moving_variable_settings.Mem.counter = 10
moving_variablesB.do_something()

print moving_variable_settings.Mem.counter
print moving_variable_settings.counter2