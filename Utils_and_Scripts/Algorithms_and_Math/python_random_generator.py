"""
File: python_random_generator.py
Name: Alan
———————————————————————————————————
This program simulates a certain number of die-roll results and calculates
how many consecutive number (defined as runs) appears.
"""


import random


NUM_ROLLS = 15


def main():
    """
    Simulates dice rolls and calculates the number of runs.
    Uses a counter to track consecutive matches and only counts the run
    at the first instance of a match.
    """
    a_list = []
    run = 0
    num_checker = 0
    # Generate random rolls and store them in a list
    for i in range(NUM_ROLLS):
        a = random.randrange(1, 7)
        a_list += str(a)

    # Print each roll result to the console
    for ch in a_list:
        print('Rolls: ' + ch)

    # Identify consecutive matches and count a run only at the start of the sequence
    for i in range(len(a_list) - 1):
        if a_list[i] == a_list[i + 1]:
            # Increment the consecutive match counter
            num_checker += 1
        else:
            # Reset the counter when the sequence is broken
            num_checker = 0

            # Count the run only when the match counter is exactly 1 (the start of a run)
        if num_checker == 1:
            run += 1

    print('Number of run: ' + str(run))


if __name__ == '__main__':
    main()
