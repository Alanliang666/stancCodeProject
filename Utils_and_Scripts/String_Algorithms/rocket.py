"""
File: rocket.py
Name: Alan
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 3 Handout.

"""

# This constant determines rocket size.
SIZE = 3


def main():
    """
    Drawing of the rocket by calling functions for each section (head, belt, upper body, lower body)
    """
    head()
    belt()
    upper()
    lower()
    belt()
    head()


def head():
    """
    Prints the cone shape used for the rocket's head and tail.
    """
    for i in range(SIZE):
        for j in range(SIZE-i):
            print(' ', end='')
        for j in range(i+1):
            print('/', end='')
        for j in range(i+1):
            print('\\', end='')
        print('')


def belt():
    """
    Prints the horizontal divider belt appearing between sections.
    """
    for i in range(1):
        for j in range(1):  # First and last position need put '+'
            print('+', end='')
        for j in range(2 * SIZE):  # A least need 2 '=' to connect the '+'
            print('=', end='')
        for j in range(1):
            print('+', end='')
        print('')


def upper():
    """
    Prints the upper body of the rocket.
    """
    for i in range(SIZE):
        for j in range(1):  # First and last position need put '|'
            print('|', end='')
        for j in range(SIZE-i-1):
            print('.', end='')
        for j in range(i+1):
            print('/', end='')
            print('\\', end='')
        for j in range(SIZE-i-1):
            print('.', end='')
        for j in range(1):
            print('|', end='')
        print('')


def lower():
    """
    Prints the lower body of the rocket.
    """
    for i in range(SIZE):
        for j in range(1):  # First and last position need put '|'
            print('|', end='')
        for j in range(i):
            print('.', end='')
        for j in range(SIZE-i):
            print('\\', end='')
            print('/', end='')
        for j in range(i):
            print('.', end='')
        for j in range(1):
            print('|', end='')
        print('')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
