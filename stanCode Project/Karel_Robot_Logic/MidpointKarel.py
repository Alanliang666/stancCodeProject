"""
File: MidpointKarel.py
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
    Post-condition: Karel is facing West, on the midpoint of the line
    """
    fill_one_line()
    pick_every_beepers()
    go_to_midpoint()


def fill_one_line():
    """
    Pre-condition: Karel is facing East, on the (1, 1)
    Post-condition: Karel is facing East, on the end of the line
    """
    while front_is_clear():
        put_beeper()
        if front_is_clear():
            move()
    put_beeper()


def pick_every_beepers():
    """
    Pre-condition: Karel is facing East, on the end of the line
    Post-condition: Karel is facing West, on the beginning of the line
    """
    turn_around()
    while front_is_clear():  # Pick Beepers back to first pile
        pick_beeper()
        move_to_end()
        put_beeper()
        turn_around()
        while on_beeper():
            move()
        turn_around()
        move()


def move_to_end():
    """
    Pre-condition: Karel is facing a direction with a clear way, at any position
    Post-condition: Karel is facing the wall, at end of the line
    """
    while front_is_clear():
        move()


def turn_around():
    """
    Pre-condition: Karel facing any direction
    Post-condition: Karel is facing the opposite direction ( which mean turn 180 degrees)
    """
    turn_left()
    turn_left()


def go_to_midpoint():
    """
    Pre-condition: Karel is facing West, on the beginning of the line
    Post-condition: Karel is facing West, on the midpoint of the line
    """
    while on_beeper():
        division_beepers()
    else:
        turn_west()
        if front_is_clear():
            move()
            put_beeper()
        else:
            put_beeper()


def division_beepers():
    """
    Pre-condition: Karel is facing West, on the beginning of the line
    Post-condition: Karel is facing East, on the first pile past the midpoint.
    """
    turn_east()
    pick_beeper()  # Karel follows the pattern pick-check-pick-move-put
    if front_is_clear():
        if on_beeper():
            pick_beeper()
            if on_beeper():
                move()
                put_beeper()
                turn_west()
                move()
            else:  # When remainder is 0 move and put
                move()
                put_beeper()
        else:  # When remainder is 1 then move
            move()


def turn_east():
    """
    Pre-condition: Karel is facing any direction
    Post-condition: Karel is facing East, on the same position
    """
    while not facing_east():
        turn_left()


def turn_west():
    """
    Pre-condition: Karel is facing any direction
    Post-condition: Karel is facing West, on the same position
    """
    while not facing_west():
        turn_left()

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
