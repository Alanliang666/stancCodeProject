"""
File: quadratic_solver.py
Name:
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	Pre-condition: user input a, b, c number
	Post-condition: distinguish discriminant range
		- if greater than 0 output "two roots"
		- if equal 0 output "one roots"
		- if less than 0 output "No real roots"
	"""
	print('stanCode Quadratic Solver!')
	a = int(input('Enter a:'))
	b = int(input('Enter b:'))
	c = int(input('Enter c:'))

	while a == 0:  # Check for error: if a == 0, ask to re-enter
		print("The value of 'a' cannot be 0. Please enter a different number.")
		a = int(input('Enter a:'))
	discriminant = b * b - 4 * a * c
	if discriminant > 0:
		x1 = (-b + math.sqrt(discriminant)) / (2 * a)
		x2 = (-b - math.sqrt(discriminant)) / (2 * a)
		print('Two roots ' + str(x1) + ', ' + str(x2))
	elif discriminant == 0:
		x1 = (-b + math.sqrt(discriminant)) / (2 * a)
		print('One roots ' + str(x1))
	else:
		print('No real roots')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
