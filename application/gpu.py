'''
Tuples for GPU related checks.
'''
import random
import helpers

def main(csv_data):
    message = ''

    #memory error
    parameter = "GPU Memory Errors []"
    try:
        message += helpers.check_yes_parameter(parameter, csv_data)
    except KeyError:
        pass

    #g12v rail failiure
    parameter = "GPU VRM Voltage In (VIN/+12V) [V]"
    try:
        message += helpers.check_min_parameter(parameter, csv_data, 11.40)
        message += helpers.check_max_parameter(parameter, csv_data, 12.60)
    except KeyError:
        pass

    #Usage
    parameter = "GPU Utilization [%]"
    try:
        data = csv_data[parameter]
    except KeyError:
        message += "No GPU Utilization data.\n"
    else:
        message += "Gpu average usage: {}\n".format(sum(data)/len(data))

    #Temperature
    parameter = "GPU Thermal Diode [°C]"
    try:
        data = csv_data[parameter]
    except KeyError:
        message += "Gpu temp: Key error\n"
    else:
        message += "Gpu temp max: {}\n".format(max(data))
        message += "Gpu temps sample: {}\n".format(random.sample(data, 20))

    #Average hz
    try:
        data = csv_data["GPU Clock [MHz]"]
    except KeyError:
        message += "Gpu avg hz: Key not found.\n"
    else:
        message += "GPU avg hz: {}\n".format(sum(data) / len(data))

    return message
