"""Moduł zwiera klasę Tie_fighter (myśliwca)."""
import random

from const import Consts, Assets

class TieFighter:
    """Klasa wrogich myśliwców."""

    def __init__(self, speed_x=2, speed_y=1):
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.position_x = random.randint(1, Consts.WINDOW_WIDTH - 1 - Consts.TIE_FIGHTER_WIDTH)
        self.position_y = 50 - Consts.TIE_FIGHTER_HEIGHT

    def draw_tie_fighter(self, game_board):
        """Funkcja rysuje obiekt myśliwa na ekranie."""
        game_board.screen.blit(Assets.tie_fighter_img, (self.position_x, self.position_y))
        if self.position_y >= Consts.WINDOW_HEIGHT:
            return True
        return False

    def move_tie_fighter(self):
        """Funkcja zmienia koordynaty obiektu myśliwca."""
        self.position_x += self.speed_x
        self.position_y += self.speed_y

    def move_limitation(self):
        """Funkcja oragnicze pole po którym może się poruszać obiekt myśliwca."""
        if self.position_x <= 0:
            self.speed_x *= -1
        elif self.position_x >= Consts.WINDOW_WIDTH - Consts.TIE_FIGHTER_WIDTH:
            self.speed_x *= -1
