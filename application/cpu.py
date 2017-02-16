'''
'''

import helpers

def main(csv_data):
    message = ''
    
    #thermal throttling
    param_names = ["Core #0 Thermal Throttling [Yes/No]",
                   "Core #1 Thermal Throttling [Yes/No]",
                   "Core #2 Thermal Throttling [Yes/No]",
                   "Core #3 Thermal Throttling [Yes/No]"]
    for parameter in param_names:
        message += helpers.check_yes_parameter(parameter, csv_data)

    #temp
    param_names = ["Core #0 [°C]",
    	           "Core #1 [°C]",
                   "Core #2 [°C]",
                   "Core #3 [°C]"]
    try:
        data = [i for parameter in param_names for i in csv_data[parameter]]
    except KeyError:
        message += "No core temp data.\n"
    else:
        message += "Max cpu core temp: {}\n".format(max(data))

    #Vcore
    parameter = "Vcore [V]"
    try:
        data = csv_data[parameter]
    except KeyError:
        message += "Key error: {} not found.\n".format(parameter)
    else:
        message += "Vcore min: {}\n".format(min(data))
        message += "Vcore max: {}\n".format(max(data))

    param_names = ["Core #0 Clock [MHz]",
                   "Core #1 Clock [MHz]",
                   "Core #2 Clock [MHz]",
                   "Core #3 Clock [MHz]"]

    for parameter in param_names:
        try:
            data = csv_data[parameter]
        except KeyError:
            message += "Key Error: {} not found.\n".format(parameter)
        else:
            message += "{0} average hz: {1}\n".format(parameter, round(sum(data)/len(data)))


    return message
