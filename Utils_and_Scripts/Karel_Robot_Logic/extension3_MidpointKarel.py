"""
File: extension3_MidpointKarel.py
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
        put_double_beepers()
        while front_is_clear():
            move_twice()
            back_to_slower()
            move_one()
            back_to_faster()
        pick_beeper()
        if on_beeper():
            pick_beeper()
        else:
            back_to_slower()
            pick_beeper()
    put_beeper()


def put_double_beepers():
    """
    Pre-condition: Karel is facing East, on the (1, 1)
    Post-condition: Karel is facing East, on the (1, 1) with 2 beepers
    """
    put_beeper()
    put_beeper()


def move_twice():
    """
    Pre-condition: Karel is facing East, on the (1, 1)
    Post-condition: Karel is facing East, on the even-numbered avenue (e.g. (1, 3), (1, 5))
    """
    if on_beeper():
        pick_beeper()
        if front_is_clear():
            move()
            if front_is_clear():
                move()
                put_beeper()
            else:
                put_beeper()


def back_to_slower():
    """
    Pre-condition: Karel is facing East, on the even-numbered avenue (e.g. (1, 3), (1, 5))
    Post-condition: Karel is facing East, on the first of beeper
    """
    turn_around()
    if front_is_clear():
        move()
        while not on_beeper():
            if front_is_clear():
                move()
        turn_around()


def move_one():
    """
    Pre-condition: Karel is facing East, on the first of beeper
    Post-condition: Karel is facing East, one step past on the original position
    """
    pick_beeper()
    if front_is_clear():
        move()
        put_beeper()


def back_to_faster():
    """
    Pre-condition: Karel is facing East, on the first of beeper
    Post-condition: Karel is facing East, on the second of beeper
    """
    if front_is_clear():
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
