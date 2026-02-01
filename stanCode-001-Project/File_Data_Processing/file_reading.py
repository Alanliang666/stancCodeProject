"""
File: file_reading.py
Name: Alan
—————————————————————————————————
This program reads input from a file named “data.txt” and 
processes each line to extract all numerical digits. 
After collecting the digits, the program calculates and 
displays the maximum, minimum, and average values on the console.
"""


FILE = 'data.txt'
FILE1 = 'data_1.txt'


def main():
    """
    Reads data from the file to calculate maximum, minimum, and average values.
    It handles 'Nan' strings by skipping them.
    """
    count = 0
    total_sum = 0
    with open(FILE, 'r') as f:
        for line in f:
            if line != 'Nan\n':  # Skip 'Nan' lines
                total_sum += float(line)
                count += 1
                if count == 1:  # Initialize max/min with the first valid value
                    maximum = float(line)
                    minimum = float(line)
                else:
                    if maximum < float(line):
                        maximum = float(line)
                    elif minimum > float(line):
                        minimum = float(line)
        if count == 0:  # Check if we processed any valid data
            print('No data in this file', end='')
        else:
            print('MAX:' + str(maximum))
            print('MIN:' + str(minimum))
            print('Avg:' + str(total_sum / count))


if __name__ == '__main__':
    main()
