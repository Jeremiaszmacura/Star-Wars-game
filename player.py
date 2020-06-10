"""Moduł zawiera klasę Player."""
import pygame
from const import Consts

class Player:
    """Klasa gracza zawiera metody potrzebne do rysowania obiektu gracza, zmiane jego koordynantów,
     ograniczenie ruchu, kontrole klawiatury (sterowanie)."""

    def __init__(self):
        self.position_x = Consts.WINDOW_WIDTH // 2 - Consts.PLAYER_WIDTH // 2
        self.position_y = Consts.WINDOW_HEIGHT - Consts.PLAYER_HEIGHT * 2
        self.speed_x = 0
        self.speed_y = 0

    def draw_player(self, game_board, images):
        """Metoda rysuje obiekt gracza na ekranie."""
        game_board.screen.blit(images.PLAYER_IMG, (self.position_x, self.position_y))

    def move_player(self):
        """Metoda zmienia koordynanty gracza."""
        self.position_x += self.speed_x
        self.position_y += self.speed_y

    def move_limitation(self):
        """Metoda ogranicza przestrzeń, po której może się przemieszczać gracz."""
        if self.position_x <= 0:
            self.position_x = 0
        elif self.position_x >= Consts.WINDOW_WIDTH -Consts.PLAYER_WIDTH:
            self.position_x = Consts.WINDOW_WIDTH - Consts.PLAYER_WIDTH
        if self.position_y >= Consts.WINDOW_HEIGHT - Consts.PLAYER_HEIGHT:
            self.position_y = Consts.WINDOW_HEIGHT - Consts.PLAYER_HEIGHT
        elif self.position_y <= 0:
            self.position_y = 0

    # key control
    def key_control(self, ekran):
        """Metoda obsługuję sterowani,e przy pomocy klawiatury, obiektem gracza."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ekran.closing_menu = False
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.speed_x -= Consts.ACCELERATION
                if event.key == pygame.K_RIGHT:
                    self.speed_x += Consts.ACCELERATION
                if event.key == pygame.K_DOWN:
                    self.speed_y += Consts.ACCELERATION
                if event.key == pygame.K_UP:
                    self.speed_y -= Consts.ACCELERATION
                if event.key == pygame.K_SPACE:
                    ekran.initiate_bullets(self.position_x, self.position_y)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.speed_x = 0
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    self.speed_y = 0
        return True
