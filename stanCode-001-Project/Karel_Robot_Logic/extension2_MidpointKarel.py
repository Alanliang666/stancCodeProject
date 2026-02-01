"""
File: extension2_MidpointKarel.py
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
    Pre-condition: Karel facing East, on the (1, 1)
    Post-condition: Karel facing South, on the midpoint of line
    """
    while front_is_clear():  # Routine up and right until facing the wall
        go_up_twice()
        if not on_beeper():
            go_right_one()
    if on_beeper():
        pick_beeper()
    turn_and_move()
    put_beeper()


def go_up_twice():
    """
    Pre-condition: Karel facing East, on the (1, 1)
    Post-condition: Karel facing North, on the front of second pile
    """
    turn_north()
    if front_is_clear():  # Check modulo is 1 or 0
        move()
        if front_is_clear():
            move()
        else:  # Put a beeper to mark that Karel is in an odd-numbered or even-numbered world.
            put_beeper()


def turn_north():
    """
    Pre-condition: Karel is facing any direction
    Post-condition: Karel is facing North, on the same position
    """
    while not facing_north():
        turn_left()


def go_right_one():
    """
    Pre-condition: Karel facing North, on the odd-numbered line
    Post-condition: Karel facing North, on the adjacent pile to the right
    """
    turn_right()
    move()
    turn_north()


def turn_right():
    """
    Pre-condition: Karel is facing any direction
    Post-condition: Karel is facing 90 degrees to its right
    """
    for i in range(3):
        turn_left()


def turn_and_move():
    """
    Pre-condition: Karel facing any direction
    Post-condition: Karel is facing the opposite direction, and moves to the next pile
    """
    turn_around()
    while front_is_clear():
        move()
    while not facing_south():
        turn_left()


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
