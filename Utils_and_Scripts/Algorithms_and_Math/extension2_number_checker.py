"""
File: extension2_number_checker.py
Name:
------------------------
This program asks our user for input and checks if the input is a
perfect number、deficient number or an abundant number.

A number is said to be perfect if it is equal to the sum of all its
factors (for obvious reasons the list of factors being considered does
not include the number itself).

A number is considered to be abundant if the sum of its factors
(aside from the number) is greater than the number itself.

And a number is said to be deficient if it is bigger than the sum of all its
factors(aside from the number itself).

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
    """
    Input
        User can enter any positive integer, or -100 to quit
    Output
        Determine if the input is perfect number or deficient number or abundant number
    """
    print('Welcome to the number checker!')
    while True:
        n = int(input('n: '))
        star = 1  # Initialize result to 1 for multiplication
        answer = n
        if n == EXIT:
            break
        while True:
            if star == n-1:  # Break at n-1 since the formula not use n
                break
            if n % star == 0:
                answer -= star  # If n - sum(factors) == 0, it's a perfect number
            star += 1  # Increment to check the next number
        if answer == 0:
            print(str(n) + ' is a perfect number')
        elif answer < 0:
            print(str(n) + ' is a abundant number')
        else:
            print(str(n) + ' is a deficient number')
    print('Have a good one!')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
