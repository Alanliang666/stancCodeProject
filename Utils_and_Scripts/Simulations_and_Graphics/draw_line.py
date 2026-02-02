"""
File: draw_line.py
Name: Alan
-------------------------
This program implements an interactive line-drawing tool using the
campy graphics library. It detects mouse clicks to define line segments.

Interaction flow:
 1. First click (Odd): Marks the starting point with a temporary circle.
 2. Second click (Even): Draws a line from the start point to the current position
    and removes the temporary circle.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 10

# Global variable part
window = GWindow()
start_x = 0
start_y = 0
is_odd_click = True
circle_object = None


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(mouse):
    """
    :param mouse: The mouse event object containing the x and y coordinates of the click.
    Respond to mouse clicks to draw a line between two points.
    On an odd click, draws a small circle to mark the start point and records the coordinates.
    On an even click, remove the circle and draws a line from the start point to the current mouse position.
    """
    global start_x, start_y, is_odd_click, circle_object
    circle = GOval(SIZE, SIZE, x=mouse.x - SIZE / 2, y=mouse.y - SIZE / 2)
    if is_odd_click:
        window.add(circle)
        start_x = mouse.x
        start_y = mouse.y
        circle_object = circle
        is_odd_click = False
    else:
        window.remove(circle_object)
        line = GLine(start_x, start_y, x1=mouse.x, y1=mouse.y)
        window.add(line)
        is_odd_click = True


if __name__ == "__main__":
    main()
