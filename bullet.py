"""Moduł zawiera klasę Bullet."""
from const import Consts

class Bullet:
    """Klasa definiująca pocisk wystrzeliwywany przez gracz."""
    # pylint: disable=too-few-public-methods

    def __init__(self, player_position_x, player_position_y, speed=4):
        self.speed_y = speed
        self.position_x = player_position_x + Consts.PLAYER_WIDTH // 4
        self.position_y = player_position_y

    def draw_bullet(self, game_board, images):
        """Metoda rysuje obiekt pocisku na ekranie."""
        self.position_y -= self.speed_y
        game_board.screen.blit(images.BULLET_IMG, (self.position_x, self.position_y))
        if self.position_y <= 0:
            return True
        return False
