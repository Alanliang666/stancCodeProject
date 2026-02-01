"""
File: CollectNewspaperKarel.py
Name: Alan
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def main():
    """
    Pre-condition: Karel is facing East, on (4, 3)
    Post-condition: Karel is facing East, on (4, 3) with the newspaper
    """
    move_to_newspaper()
    bring_it_back()


def move_to_newspaper():
    """
    Pre-condition: Karel is facing East, at the upper left of the house (4, 3)
    Post-condition: Karel is facing East, at the house front door (3, 6)
    """
    turn_right()
    move()
    turn_left()
    move_3times()
    pick_beeper()


def bring_it_back():
    """
    Pre-condition: Karel is facing East, at the house front door (3, 6)
    Post-condition: Karel is facing East, at the upper left of the house (4, 3)
    """
    turn_around()
    move_3times()
    turn_right()
    move()
    turn_right()
    put_beeper()


def turn_right():
    """
    Pre-condition: Karel is facing any direction
    Post-condition: Karel is facing 90 degrees to its right
    """
    for i in range(3):
        turn_left()


def move_3times():
    """
    Pre-condition: Karel is facing any direction that is not blocked, at any position
    Post-condition: Karel is facing same direction and has moved 3 steps forward
    """
    for i in range(3):
        move()


def turn_around():
    """
    Pre-condition: Karel facing any direction
    Post-condition: Karel is facing the opposite direction ( which means turn 180 degrees)
    """
    for i in range(2):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
