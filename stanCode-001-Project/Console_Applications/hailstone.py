"""
File: hailstone.py
Name: Alan
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    Pre-condition:
        - if input is odd-numbered, then n*3+1
        - if input is even-numbered, then n/2
    Post-condition: Prints the hailstone sequence and outputs the total number of steps to reach 1
    """
    steps = 0
    print('This program computes the hailstone sequences.')
    print('')
    n = int(input('Enter your number: '))
    while n != 1:  # Last number must be 1
        steps = steps + 1  # Count the steps during execution
        if n % 2 == 1:  # Check odd or even number first
            odd_n = 3 * n + 1
            print(str(n)+' is odd,so I make 3n+1: '+str(odd_n))
            n = odd_n  # Update n for the next iteration
        elif n % 2 == 0:
            even_n = n // 2
            print(str(n) + ' is even,so I take half : '+str(even_n))
            n = even_n
        else:
            break
    print('It took ' + str(steps) + ' steps to reach 1.')

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == "__main__":
    main()
