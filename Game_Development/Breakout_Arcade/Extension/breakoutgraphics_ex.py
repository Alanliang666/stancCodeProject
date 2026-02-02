"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

This module defines the BreakoutGraphics class, which manages the graphical interface for the Breakout game.
It handles the initialization of game objects (window, paddle, ball, bricks) and manages physics interactions such as
collisions and velocity updates.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40  # Width of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 10  # Number of rows of bricks
BRICK_COLS = 10  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 75  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels)
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        """
        :param ball_radius: int, radius of the ball in pixels
        :param paddle_width: int, width of the paddle in pixels
        :param paddle_height: int, height of the paddle in pixels
        :param paddle_offset: int, gap between the paddle and the bottom of the window
        :param brick_rows: int, number of brick rows
        :param brick_cols: int, number of brick columns
        :param brick_width: int, width of a single brick
        :param brick_height: int, height of a single brick
        :param brick_offset: int, gap from the top of the window to the first row of bricks
        :param brick_spacing: int, spacing between adjacent bricks
        :param title: str, title text for the game window
        Initializes the graphical window and game objects (paddle, ball, bricks).
        """
        # Create a graphical window, with some extra space
        self._window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self._window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self._window_width, height=self._window_height, title=title)
        self.ball_radius = ball_radius

        # Create a paddle
        self.paddle_offset = paddle_offset
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, (self._window_width - paddle_width) / 2, self._window_height - paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius, ball_radius)
        self.ball.filled = True
        self.window.add(self.ball, (self._window_width - self.ball.width) / 2,
                        (self._window_height - self.ball.height) / 2)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        self.__is_ball_moved = False
        onmouseclicked(self.ball_reset)
        onmousemoved(self.paddle_move)

        # Make score board
        self.score = GLabel(f'Score: ')
        self.score.font = '-20'
        self.window.add(self.score, 0, self.window.height)

        # Store bonus gift
        self.cubes = []

        # Draw bricks
        self.__brick_count = brick_cols * brick_rows
        for row in range(brick_rows):
            for col in range(brick_cols):
                new_col = col * (brick_spacing + brick_width)
                new_row = row * (brick_spacing + brick_height)

                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True

                if row < brick_rows * 0.2:
                    self.brick.fill_color = 'red'
                    self.brick.score = 5
                elif row < brick_rows * 0.4:
                    self.brick.fill_color = 'orange'
                    self.brick.score = 4
                elif row < brick_rows * 0.6:
                    self.brick.fill_color = 'yellow'
                    self.brick.score = 3
                elif row < brick_rows * 0.8:
                    self.brick.fill_color = 'green'
                    self.brick.score = 2
                elif row < brick_rows * 1:
                    self.brick.fill_color = 'blue'
                    self.brick.score = 1

                self.window.add(self.brick, new_col, new_row + brick_offset)

        # Make lives count
        self.lives = GLabel(f'❤❤❤')
        self.lives.font = '-20'
        self.window.add(self.lives, self.window.width - self.lives.width, self.window.height)

    def paddle_move(self, event):
        """
        :param event: Mouse event containing the current x and y coordinates
        Updates the paddle's horizontal position to follow the mouse.
        The paddle stays fixed on the vertical axis.
        """
        if 0 <= event.x <= self._window_width - self.paddle.width:
            self.window.add(self.paddle, x=event.x, y=self._window_height - self.paddle_offset)

    def ball_reset(self, _):
        """
        :param _: Unused parameter required by the mouse listener.
        Sets the ball's initial to start the game.
        This is triggered by a mouse click and only executes if the ball is currently stationary.
        """
        if not self.__is_ball_moved:
            self.__dy = INITIAL_Y_SPEED
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx
        self.__is_ball_moved = True

    def restart_game(self):
        """
        Restart the ball to the center of the window and stops its movement.
        """
        self.window.remove(self.ball)
        self.window.add(self.ball, (self._window_width - self.ball.width) / 2,
                        (self._window_height - self.ball.height) / 2)
        self.__is_ball_moved = False
        self.__dx = 0
        self.__dy = 0

    def get_dx(self):
        """
        :return: int, the current horizontal velocity of the ball
        """
        return self.__dx

    def get_dy(self):
        """
        :return: int, the current vertical velocity of the ball
        """
        return self.__dy

    def get_brick_count(self):
        """
        :return: int, the total number of bricks initially created
        """
        return self.__brick_count

    def setter_dx(self, new_dx):
        """
        :param new_dx: int, the new horizontal velocity to apply
        Updates the ball's horizontal velocity.
        """
        self.__dx = new_dx

    def setter_dy(self, new_dy):
        """
        :param new_dy: int, the new vertical velocity to apply
        Updates the ball's vertical velocity.
        """
        self.__dy = new_dy

    def create_cube(self, x, y, brick_width, brick_height):
        """
        :param x: int, the x-coordinate of the broken brick.
        :param y: int, the y-coordinate of the broken brick.
        :param brick_width: int, the width of the brick.
        :param brick_height: int, the height of the brick.
        Spawns a bonus item at the location of a broken brick
        This item provides a power-up to the player when collected.
        """
        cube = GRect(10, 10)
        cube.filled = True
        cube_x = x + (brick_width - cube.width) / 2
        cube_y = y + (brick_height - cube.height) / 2
        self.window.add(cube, cube_x, cube_y)
        self.cubes.append(cube)

    def set_size(self, width, height):
        """
        :param width: int, the new width of the paddle
        :param height: int, the new height of the paddle
        Update the paddle's dimensions
        Replaces the existing paddle object with a new one while maintaining its current position.
        """
        old_x = self.paddle.x
        old_y = self.paddle.y

        if old_x + width > self._window_width:
            old_x = self._window_width - width

        self.window.remove(self.paddle)
        self.paddle = GRect(width, height)
        self.paddle.filled = True
        self.window.add(self.paddle, old_x, old_y)
