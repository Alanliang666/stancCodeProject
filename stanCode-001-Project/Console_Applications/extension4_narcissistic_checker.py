"""
File: extension4_narcissistic_checker.py
Name:
------------------------
This program asks our user for input and checks if the input is a
narcissistic number or not.

A positive integer is called a narcissistic number if it
is equal to the sum of its own digits each raised to the
power of the number of digits.

Example: 153 is narcissistic because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
Note that by this definition all single digit numbers are narcissistic.

Students are recommended to use // and % to complete this program.

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
    """
    Input
        User can enter any positive integer, or -100 to quit
    Output
        Determine if the input is narcissistic number
    """
    print('Welcome to the narcissistic number checker!')
    while True:
        n = int(input('n: '))
        place_value = 1  # Initialize place value to 1 for the multiplication
        count = 0   # Initialize count to 0 for the count digits
        answer = 0  # Initialize answer to 0 for the sequence sum
        temp_n = n
        if n == EXIT:
            break
        while True:  # Count the number of digits
            if n // place_value > 0:
                place_value *= 10
                count += 1
            else:
                break
        while True:
            if temp_n == 0:
                break
            else:  # Get each digit from n and calculate the answer
                digit = temp_n % 10
                digit_power = digit ** count
                answer += digit_power
                temp_n //= 10
        if answer == n:
            print(str(n) + ' is a narcissistic number')
        else:
            print(str(n) + ' is not a narcissistic number')
    print('Have a good one!')


if __name__ == '__main__':
    main()
