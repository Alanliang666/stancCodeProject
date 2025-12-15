"""
File: extension3_triangular_checker.py
Name:
--------------------------
This program asks our user for input and checks if the input is an
triangular number or not.

The triangular number (Tn) is a number that can be represented in the form of a triangular
grid of points where the first row contains a single element and each subsequent row contains 
one more element than the previous one.

We can just use the fact that the nth triangular number can be found by using a formula: Tn = n(n + 1) / 2.

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
    """
    Input
        User can enter any positive integer, or -100 to quit
    Output
        Determine if the input is triangular number
    """
    print('Welcome to the triangular number checker')
    while True:
        n = int(input('n: '))
        star = 1
        answer = 1  # Initialize answer to 1 for the sequence sum
        if n == EXIT:
            break
        while True:
            if answer >= n:  # Stop when the total matches or passes n
                break
            star += 1  # Increment the value to add next
            answer += star
        tn = star * (star + 1) / 2
        if tn == n:
            print(str(n) + ' is a triangular number')
        else:
            print(str(n) + ' is not a triangular number')
    print('Have a good one!')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
