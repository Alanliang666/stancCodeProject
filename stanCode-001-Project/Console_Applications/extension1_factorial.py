"""
File: extension1_factorial.py
Name: 
-------------------
This program will continually ask our user to give a number
and will calculate the factorial result of the number and print it on the console.

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
	"""
	Input
		User can enter any positive integer, or -100 to quit
	Output
		The factorial of the input number.
	"""
	print('Welcome to stanCode factorial master!')
	while True:
		n = int(input('Give me a number, and I will list the answer of factorial: '))
		star = 1  # Initialize result to 1 for multiplication
		answer = n
		if n == EXIT:
			break
		while True:
			if star == n-1:  # Break at n-1 since the formula already includes n
				break
			if star < n:
				star += 1
				answer *= star
		print('Answer:' + str(answer))
	print('- - - - - - See ya!- - - - - - ')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
	main()