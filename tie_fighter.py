"""The module contains the Tie_fighter class."""
import random
from const import Consts

class TieFighter:
    """Enemy fighter class."""

    def __init__(self, speed_x, speed_y):
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.position_x = random.randint(1, Consts.WINDOW_WIDTH - 1 - Consts.TIE_FIGHTER_WIDTH)
        self.position_y = 50 - Consts.TIE_FIGHTER_HEIGHT

    def draw_tie_fighter(self, game_board, images):
        """The function draws the fighter object on the screen."""
        game_board.screen.blit(images.TIE_FIGHTER_IMG, (self.position_x, self.position_y))
        if self.position_y >= Consts.WINDOW_HEIGHT:
            return True
        return False

    def move_tie_fighter(self):
        """The function changes the coordinates of the fighter object."""
        self.position_x += self.speed_x
        self.position_y += self.speed_y

    def move_limitation(self):
        """Organizational function the field over which the fighter's object can move."""
        if self.position_x <= 0:
            self.speed_x *= -1
        elif self.position_x >= Consts.WINDOW_WIDTH - Consts.TIE_FIGHTER_WIDTH:
            self.speed_x *= -1
