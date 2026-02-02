"""
File: coin_flip_runs.py
Name:
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
	"""
	Simulates coin flips and stops execution once the number of runs input by the user is reached.
	"""
	print("Let's flip a coin!")
	num_run = int(input('Number of runs: '))
	hit = 0
	can_count = True
	old_run = r.randrange(0, 2)
	coin_flip(old_run)
	while hit != num_run:
		new_run = r.randrange(0, 2)
		if old_run == new_run:
			if can_count:
				hit += 1
				can_count = False
		else:
			can_count = True
		old_run = new_run
		coin_flip(old_run)


def coin_flip(run):
	"""
	Prints the character corresponding to the input number.
	:param run: int, the coin flip result
	"""
	if run == 0:
		print('H', end='')
	elif run == 1:
		print('T', end='')


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
