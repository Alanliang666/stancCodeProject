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
    total = 0
    maximum = -float('inf')
    minimum = float('inf')
    f = open(FILE)
    for line in f:
        if line != 'Nan\n':
            data = float(line)
            if data > maximum:
                maximum = data
            if data < minimum:
                minimum = data
            total += data
            count += 1
    f.close()
    if count == 0:  # Check if we processed any valid data
        print('No data in this file', end='')
    else:
        print('MAX:' + str(maximum))
        print('MIN:' + str(minimum))
        print('Avg:' + str(total / count))


if __name__ == '__main__':
    main()
