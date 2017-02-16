'''
'''

import csv

from application import gpu
from application import cpu
from application import voltage
from application import helpers

def main(filename):
    with open(filename, newline='', encoding='latin1') as f:
        reader = csv.DictReader(f)
        headers = next(reader)

        data_dict = {header: [] for header in headers}
        for row in reader:
            for header in headers:
                cell = row[header]
                if cell != header:
                    try:
                        data_dict[header].append(float(cell))
                    except ValueError:
                        data_dict[header].append(cell)

        message = ''

        #CPU stuff
        message += cpu.main(data_dict)

        #GPU stuff
        message += gpu.main(data_dict)

        #voltages
        message += voltage.main(data_dict)

        #Drive stuff
        #drive activity
        #param_names = ["Total Activity [%]"]
        #trigger_value = 65
        #message += helpers.check_max_parameter([param_names, 65])

        #cpu overclocked
        #amd
        #intel

    # add max recorded value to warning message?
    #
        return message

if __name__ == '__main__':
    from tkinter.filedialog import askopenfilename
    filename = ""
    while not filename.lower().endswith("csv"):
        filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file

    print(main(filename))
