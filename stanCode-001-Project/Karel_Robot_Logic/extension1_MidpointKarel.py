"""
File: extension1_MidpointKarel.py
Name: Alan
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *


def main():
    """
    Pre-condition: Karel is facing East, on the (1, 1)
    Post-condition: Karel is facing West, on the midpoint of line
    """
    fill_one_line()
    while on_beeper():
        pick_and_turn()
        move_to_end()
        move_back()
    facing_check()


def fill_one_line():
    """
    Pre-condition: Karel is facing East, on the (1, 1)
    Post-condition: Karel is facing West, on the end of the line
    """
    while front_is_clear():  # Leave the first pile empty to avoid an infinite loop
        move()
        put_beeper()
    turn_around()


def pick_and_turn():
    """
    Pre-condition: Karel is facing West, on the end of the line
    Post-condition: Karel is facing West, one position inward from the original position.
    """
    if on_beeper():
        pick_beeper()
        if front_is_clear():
            move()
        else:
            turn_around()
            if front_is_clear():
                move()


def move_to_end():
    """
    Pre-condition: Karel is facing West, on end of last beeper.
    Post-condition: Karel is facing West, one step past the opposite end of the beeper.
    """
    while on_beeper():
        move()


def move_back():
    """
    Pre-condition: Karel is facing West, one step past the other end of the beeper line.
    Post-condition: Karel is facing East, on the last beeper of the line
    """
    turn_around()
    if on_beeper():
        pick_beeper()
        move()
    else:
        move()


def facing_check():
    """
    Pre-condition:
        - if Karel is facing West, on the midpoint of line
        - if Karel is facing East, one step past the midpoint
    Post-condition: Karel is facing West, on the midpoint of line
    """
    if facing_west():
        put_beeper()
    elif facing_east:
        turn_around()
        move()
        put_beeper()


def turn_around():
    """
    Pre-condition: Karel facing any direction
    Post-condition: Karel is facing the opposite direction ( which mean turn 180 degrees)
    """
    turn_left()
    turn_left()

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
