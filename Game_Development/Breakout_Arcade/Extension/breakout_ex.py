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
from breakoutgraphics_ex import BreakoutGraphics
import random

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    """
    The main entry point for the breakout game.
    It initializes the graphics window, manages the animation loop,
    and tracks game termination conditions (win/loss).
    """
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    broke_brick = 0
    score_sum = 0
    brick_count = graphics.get_brick_count()

    # Add the animation loop here!
    while True:
        dx = graphics.get_dx()
        dy = graphics.get_dy()

        # Update ball position
        graphics.ball.move(dx, dy)

        # Handle power-up drops: movement and collection
        for cube in graphics.cubes[:]:
            cube.move(0, 5)  # Move bonus item downwards at a constant speed
            if graphics.window.get_object_at(cube.x, cube.y + cube.height) is graphics.paddle:
                # Change paddle width
                new_paddle_width = graphics.paddle.width * 1.1
                height = graphics.paddle.height
                graphics.set_size(new_paddle_width, height)

                # Remove cube
                graphics.window.remove(cube)
                graphics.cubes.remove(cube)

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
            elif hitter is graphics.score:
                pass
            elif hitter is graphics.lives:
                pass
            elif hitter in graphics.cubes:
                # Ignore collisions between the ball and falling gifts
                # Let the gift continue falling for the paddle to catch
                pass
            else:
                graphics.setter_dy(-dy)
                graphics.window.remove(hitter)
                broke_brick += 1  # Track broken brick count
                score_sum += hitter.score

                # Create bonus gift
                if random.random() > 0.85:
                    graphics.create_cube(hitter.x, hitter.y, hitter.width, hitter.height)

                # Increase difficulty
                if broke_brick % 20 == 0:
                    new_dy = 1.2 * graphics.get_dy()
                    graphics.setter_dy(new_dy)

        # Update lives display
        if lives == 2:
            graphics.lives.text = '❤❤'
        if lives == 1:
            graphics.lives.text = '❤'
        if lives == 0:
            graphics.lives.font = '-50-bold'
            graphics.lives.color = 'red'
            graphics.lives.text = 'Game Over!!'
            graphics.window.add(graphics.lives, (graphics.window.width-graphics.lives.width)/2,
                                graphics.window.height/2)

        # Update score display
        graphics.score.text = f'Score: {score_sum}'

        # Pause
        pause(FRAME_RATE)

        # Game Over condition
        if lives == 0:
            graphics.lives.font = '-50-bold'
            graphics.lives.color = 'red'
            graphics.lives.text = 'Game Over!!'
            graphics.window.add(graphics.lives, (graphics.window.width - graphics.lives.width) / 2,
                                graphics.window.height / 2)
            break

        if broke_brick == brick_count:
            graphics.lives.font = '-50-bold'
            graphics.lives.color = 'blue'
            graphics.lives.text = 'You Win!!'
            graphics.window.add(graphics.lives, (graphics.window.width - graphics.lives.width) / 2,
                                graphics.window.height / 2)
            break


if __name__ == '__main__':
    main()
