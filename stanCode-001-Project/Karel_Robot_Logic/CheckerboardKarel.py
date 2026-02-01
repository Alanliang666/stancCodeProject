"""
File: CheckerboardKarel.py
Name: Alan
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *


def main():
    """
    Karel fills the world with a checkerboard pattern
    Pre-condition: Karel is facing East, at (1, 1)
    Post-condition: Karel is facing North, at the northwestern-most corner (Street_MAX, 1)
    """
    if front_is_clear():
        while front_is_clear():
            fill_odd_line()
            if front_is_clear():  # Checks if Karel has reached the top wall before running fill_even_line()
                fill_even_line()
    else:  # Handles the special case of a world that is only 1 avenue wide (e.g.1x1 or 8x1 worlds)
        turn_left()
        fill_odd_line()


def fill_odd_line():
    """
    Pre-condition: Karel is facing East, at the beginning of the odd-numbered line (e.g. (1, 1) or (3, 1))
    Post-condition: Karel is facing East, at the beginning of the even-numbered line (e.g. (2, 1) or (4, 1))
    """

    put_beeper()  # Ensure a beeper is placed first, Karel puts a beeper every 2 steps and odd-numbered require a beeper
    while front_is_clear():  # If clear, Karel follows the pattern: move, move, put beeper.
        move()
        if front_is_clear():  # Check for walls before every move, and put a beeper after moving.
            move()
            put_beeper()
    go_to_next_line()


def fill_even_line():
    """
    Pre-condition: Karel is facing East, at the beginning of the even-numbered line (e.g. (2, 1) or (4, 1))
    Post-condition: Karel is facing East, at the beginning of the odd-numbered line (e.g. (1, 1) or (3, 1))
    """
    move()  # Ensure move first, Karel puts a beeper every 2 steps and even-numbered require a beeper
    put_beeper()
    while front_is_clear():  # If clear, Karel follows the pattern: move, move, put beeper.
        move()
        if front_is_clear():  # Check for walls before every move, and put a beeper after moving.
            move()
            put_beeper()
    go_to_next_line()


def go_to_next_line():
    """
    Pre-condition: Karel is facing a wall, at the end of the line
    Post-condition:
        - If a next line exists (to the North), Karel is at its beginning (Avenue 1), facing East
        - If at top of the wall, Karel is at the west end of the line (Avenue 1), facing North
    """
    if not facing_north():  # Prevents the function from running if Karel is already facing North.
        turn_around()
        move_to_the_end()
        up_to_next_line()


def turn_around():
    """
    Pre-condition: Karel facing any direction
    Post-condition: Karel is facing the opposite direction ( which mean turn 180 degrees)
    """
    if not front_is_clear():  # Make sure Karel didn't face a wall
        for i in range(2):
            turn_left()


def move_to_the_end():
    """
    Pre-condition: Karel is facing a direction with a clear way, at any position
    Post-condition: Karel is facing the wall, at end of the line
    """
    while front_is_clear():
        move()


def up_to_next_line():
    """
    Pre-condition: Karel is facing West, at beginning (Avenue 1) of the line
    Post-condition:
        - If a next line is exist (to the North), Karel is at its beginning (Avenue 1), facing East
        - Otherwise Karel remain at its position, facing North
    """
    turn_north()
    if front_is_clear():
        move()
        turn_east()


def turn_east():
    """
    Pre-condition: Karel is facing any direction
    Post-condition: Karel is facing East, on the same position
    """
    while not facing_east():
        turn_left()


def turn_north():
    """
    Pre-condition: Karel is facing any direction
    Post-condition: Karel is facing North, on the same position
    """
    while not facing_north():
        turn_left()

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
