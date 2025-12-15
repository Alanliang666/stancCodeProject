"""
File: prime_checker.py
Name:
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
	"""
	Input
		User can entry any positive integer, or -100 to quit
	Output
		Determine if the input is prime
	"""
	print("Welcome to the prime checker!")
	while True:
		star = 2
		n = int(input('n: '))
		if n == EXIT:
			break
		while True:
			if star == n-1 or n == 2 or star == 999:  # Define break conditions, n=2 is treated as an edge case
				break
			if n % star == 0:  # Check divisibility by every number from 2 to n-1
				star = 999
			if n // star > 0:  # Check for factor in the range from 2 to n-1
				star += 1
		if n == 2 or star != 999:
			print(str(n) + ' is a prime number')
		else:
			print(str(n) + ' is not a prime number')
	print('Have a good one!')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
