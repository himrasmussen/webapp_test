'''
Helper functions.
'''


import shutil
import openpyxl

#TODO: Header to Letters

def check_max_parameter(parameter, csv_data, max_value=1):
    try:
        if max(csv_data[parameter]) >= max_value:
            return "Max " + raise_warning(
                                    parameter,
                                    report_value = max(csv_data[parameter])
                                    )
    except KeyError:
        return "No such parameter ({})\n".format(parameter)
    else:
        return ''

def check_min_parameter(parameter, csv_data, min_value=1):
    try:
        if min(csv_data[parameter]) <= min_value:
            return "Min " + raise_warning(
                                    parameter,
                                    report_value = min(csv_data[parameter])
                                    )
    except KeyError:
        return "No such parameter ({})\n".format(parameter)
    else:
        return ''

def check_yes_parameter(parameter, csv_data):
    try:
        if "Yes" in csv_data[parameter]:
            return raise_warning(parameter, report_value="Yes")
    except KeyError:
        return "No such parameter ({})\n".format(parameter)
    else:
        return ''

def raise_warning(parameter, report_value=''):
    return "{0}: {1}\n".format(parameter, report_value)
