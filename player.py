"""Moduł zawiera klasę Player"""
import pygame

class Player:
    """Klasa gracza zawiera metody potrzebne do rysowania obiektu gracza, zmiane jego koordynantów,
     ograniczenie ruchu, kontrole klawiatury (sterowanie)."""

    def __init__(self, window_width=800, window_height=600):
        self.player_img = pygame.image.load("assets/millennium_falcon.png")
        self.player_size = {"x": 64, "y": 64}
        self.position_x = int(window_width / 2 - self.player_size["x"] / 2)
        self.position_y = int(window_height - self.player_size["y"] * 2)
        self.speed_x = 0
        self.speed_y = 0
        self.acceleration = 5 # przyspieszenie

    def draw_player(self, game_board):
        """Metoda rysuje obiekt gracza na ekranie."""
        game_board.screen.blit(self.player_img, (self.position_x, self.position_y))

    def move_player(self):
        """Metoda zmienia koordynanty gracza."""
        self.position_x += self.speed_x
        self.position_y += self.speed_y

    def move_limitation(self, window_width=800, window_height=600):
        """Metoda ogranicza przestrzeń, po której może się przemieszczać gracz."""
        if self.position_x <= 0:
            self.position_x = 0
        elif self.position_x >= window_width - self.player_size["x"]:
            self.position_x = window_width - self.player_size["x"]
        if self.position_y >= window_height - self.player_size["y"]:
            self.position_y = window_height - self.player_size["y"]
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
                    self.speed_x -= self.acceleration
                if event.key == pygame.K_RIGHT:
                    self.speed_x += self.acceleration
                if event.key == pygame.K_DOWN:
                    self.speed_y += self.acceleration
                if event.key == pygame.K_UP:
                    self.speed_y -= self.acceleration
                if event.key == pygame.K_SPACE:
                    ekran.initiate_bullets(self.position_x, self.position_y, self.player_size)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.speed_x = 0
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    self.speed_y = 0
        return True
