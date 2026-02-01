"""
File: extension4_MidpointKarel.py
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
    Post-condition: Karel is facing East, on the midpoint of line
    """
    if front_is_clear():
        put_beeper()
        move_to_end()
        put_beeper()
        while on_beeper():
            pick_and_turn()
            move_next_beeper()
        while not facing_east():
            turn_left()
        put_beeper()
    else:
        put_beeper()


def move_to_end():
    """
    Pre-condition: Karel is facing East, on the (1, 1)
    Post-condition: Karel is facing East, on the end of line
    """
    while front_is_clear():
        move()


def pick_and_turn():
    """
    Pre-condition: Karel is facing East, on the end of line
    Post-condition: Karel is facing West, one step past on the original position
    """
    if on_beeper():
        pick_beeper()
        turn_around()
        move()
        if not on_beeper():
            put_beeper()
        else:
            pick_beeper()


def move_next_beeper():
    """
    Pre-condition: Karel is facing West, on the one of the beepers
    Post-condition: Karel is facing West, on the opposite beeper
    """
    if on_beeper():
        move()
        while not on_beeper():
            if front_is_clear():
                move()


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
