'''
Voltage checks.
'''

'''
"The ripple limits, according to the ATX specification, are 120mV for the +12V and -12V rails, and 50mV for the remaining rails (5V, 3.3V and 5VSB).
'''

from application import helpers
#TODO: So you'd need vcore, dram voltage, anything with a + in front of it such as +5v

def main(csv_data):
    message = ''


    parameter = "+3.3V [V]"
    try:
        message += helpers.check_max_parameter(parameter, csv_data, max_value=3.47)
        message += helpers.check_min_parameter(parameter, csv_data, min_value=3.14)
    except KeyError:
        message += "Key error: {}".format(parameter)

    parameter = "+5V [V]"
    try:
        message += helpers.check_max_parameter(parameter, csv_data, max_value=5.25)
        message += helpers.check_min_parameter(parameter, csv_data, min_value=4.75)
    except KeyError:
        message += "Key error: {}".format(parameter)

    parameter = "+12V [V]"
    try:
        message += helpers.check_max_parameter(parameter, csv_data, max_value=12.60)
        message += helpers.check_min_parameter(parameter, csv_data, min_value=11.40)
    except KeyError:
        message += "Key error: {}".format(parameter)




    return message
