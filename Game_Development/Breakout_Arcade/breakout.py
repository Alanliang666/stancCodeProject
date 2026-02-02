"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This file runs the main game loop for the breakout game.
It handles user input (paddle movement, clicks), physics interactions (collisions, ball movement),
and game state management (lives, winning conditions).
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10  # 100 frames per second
NUM_LIVES = 3  # Number of attempts


def main():
    """
    The main entry point for the breakout game.
    It initializes the graphics window, manages the animation loop,
    and tracks game termination conditions (win/loss).
    """
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    brick_break = 0

    # Add the animation loop here!
    while True:
        dx = graphics.get_dx()
        dy = graphics.get_dy()

        # Update ball position
        graphics.ball.move(dx, dy)

        # Check for wall collisions
        if 0 >= graphics.ball.x or graphics.ball.x >= graphics.window.width - graphics.ball.width:
            graphics.setter_dx(-dx)
        if 0 >= graphics.ball.y:
            graphics.setter_dy(-dy)
        if graphics.ball.y >= graphics.window.height - graphics.ball.height:
            graphics.restart_game()
            lives -= 1

        # Identify the four corners of the ball for collision detection
        obj_left_top = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
        obj_right_top = graphics.window.get_object_at(graphics.ball.x + 2 * graphics.ball_radius, graphics.ball.y)
        obj_left_down = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + 2 * graphics.ball_radius)
        obj_right_down = graphics.window.get_object_at(graphics.ball.x + 2 * graphics.ball_radius,
                                                       graphics.ball.y + 2 * graphics.ball_radius)

        # Check if any corner has collided with an object
        hitter = None
        if obj_left_top is not None:
            hitter = obj_left_top
        elif obj_right_top is not None:
            hitter = obj_right_top
        elif obj_left_down is not None:
            hitter = obj_left_down
        elif obj_right_down is not None:
            hitter = obj_right_down

        # Detect collision with paddle or bricks
        if hitter is not None:
            if hitter is graphics.paddle:
                if dy > 0:  # Prevent the ball from getting stuck inside the paddle
                    graphics.setter_dy(-dy)
            else:
                graphics.setter_dy(-dy)
                graphics.window.remove(hitter)
                brick_break += 1  # Track score

        # Pause
        pause(FRAME_RATE)

        # Game Over condition
        brick_count = graphics.get_brick_count()
        if lives == 0 or brick_break == brick_count:
            break


if __name__ == '__main__':
    main()
