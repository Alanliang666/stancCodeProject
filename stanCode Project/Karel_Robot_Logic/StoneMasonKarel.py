"""
File: StoneMasonKarel.py
Name: Alan
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *


def main():
    """
    Pre-condition: Karel is facing East, on (1, 1)
    Post-condition: Karel is facing East, on the bottom-right corner of the world
    """
    while front_is_clear():
        fix_pillar()
        go_to_next_pillar()
    if not front_is_clear():  # Make sure last pillar is fixed
        fix_pillar()
        turn_around()
        move_to_the_end()
        turn_left()


def fix_pillar():
    """
    Pre-condition: Karel is facing East, on the bottom of the pillar
    Post-condition: Karel is facing North, on the top of the pillar
    """
    turn_left()
    while front_is_clear():
        if on_beeper():
            move()
        else:
            put_beeper()
            move()
    if not on_beeper():
        put_beeper()


def go_to_next_pillar():
    """
    Pre-condition: Karel is facing North, on the top of the pillar
    Post-condition: Karel is facing East, at the bottom of the next pillar (4 avenues away)
    """
    turn_around()
    move_to_the_end()
    go_to_next()


def go_to_next():
    """
    Pre-condition: Karel is facing South, at the bottom of the pillar
    Post-condition: Karel is facing East, at the next bottom of the pillar (4 avenue away)
    """
    turn_left()
    for i in range(4):
        move()


def turn_around():
    """
    Pre-condition: Karel facing any direction
    Post-condition: Karel is facing the opposite direction ( which mean turn 180 degrees)
    """
    for i in range(2):
        turn_left()


def move_to_the_end():
    """
    Pre-condition: Karel is facing a direction with a clear way, at any position
    Post-condition: Karel is facing the wall, at end of the line
    """
    while front_is_clear():
        move()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
