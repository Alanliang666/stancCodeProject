"""
File: bouncing_ball.py
Name: Alan
-------------------------
This program implement an interactive bouncing ball simulation using campy graphics library.
It feature a physics-based animation loop where a ball accelerates under gravity and loses energy upon bouncing.

Interaction flow:
 1. Start: The user click the mouse to release the ball from the top-left.
 2. Animation: The ball bounced across the screen until it exits the right edge.
 3. Reset: Once off-screen, the ball reset to the start, and the life count decrease.
 4. Game Over: After 3 runs, mouse clicks are ignored, and the game ends.
"""

from campy.graphics.gobjects import GOval, GLabel
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# Global variable
window = GWindow(800, 500, title='bouncing_ball.py')
is_fall = False
count = 0
vy = 3


def main():
    """
    Initialize the game window, the ball and the life counter.
    It enters an animation while loop that:
        - Updates vertical velocity.
        - Check for collisions with the floor.
        - Check if the ball travels off-screen.
    """
    global vy, is_fall, count
    ball = GOval(SIZE, SIZE)
    ball.filled = True
    life = GLabel(f'Lives left: {3 - count}')
    life.font = '-50'
    window.add(life, x=(window.width-life.width) / 2, y=(window.height-life.height) / 2)
    window.add(ball, START_X, START_Y)
    onmouseclicked(fall)
    while True:
        if is_fall:
            vy += GRAVITY  # Update vertical velocity
            ball.move(VX, vy)
            if ball.y + ball.height >= window.height:  # Reverse direction on impact
                vy = -vy * REDUCE
            if ball.x + ball.width > window.width:  # Check if ball is off-screen
                is_fall = False
                count += 1  # Reset and increment count
                vy = 3  # Reset vertical velocity
                window.remove(ball)
                window.add(ball, START_X, START_Y)

                # Update the label to show remaining lives.
                if count < 3:
                    life.text = f'Lives left: {3 - count}'
                else:
                    life.text = "Game Over"
                    break
        pause(DELAY)


def fall(_):
    """
    Checks how many runs have finished.
    If the user clicks and the count is less than 3, switches the state to falling.
    """
    global is_fall, count
    if count < 3:
        is_fall = True


if __name__ == "__main__":
    main()
