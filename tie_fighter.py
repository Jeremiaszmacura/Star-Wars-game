"""Moduł zwiera klasę Tie_fighter (myśliwca)"""
import random
import pygame

class TieFighter:
    """Klasa wrogich myśliwców. Metody klasy to: konstruktor, draw_tie_fighter, move_tie_figher,
    move_limitation. Atrybutami klasy są: tie_fighter_img, tie_fighter_size, speed_x, speed_y,
    position_x, position_y."""

    def __init__(self, speed_x=2, speed_y=1, window_width=800):
        self.tie_fighter_img = pygame.image.load("assets/mysliwiec.png")
        self.tie_fighter_size = {"x": 64, "y": 64}
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.position_x = random.randint(1, window_width - 1 - self.tie_fighter_size["x"])
        self.position_y = 50 - self.tie_fighter_size["y"]

    def draw_tie_fighter(self, game_board):
        """Funkcja rysuje obiekt myśliwa na ekranie"""
        game_board.screen.blit(self.tie_fighter_img, (self.position_x, self.position_y))
        if self.position_y >= game_board.window_height:
            return True
        return False

    def move_tie_fighter(self):
        """Funkcja zmienia koordynaty obiektu myśliwca"""
        self.position_x += self.speed_x
        self.position_y += self.speed_y

    def move_limitation(self, window_width=800):
        """Funkcja oragnicze pole po którym może się poruszać obiekt myśliwca"""
        if self.position_x <= 0:
            self.speed_x *= -1
        elif self.position_x >= window_width - self.tie_fighter_size["x"]:
            self.speed_x *= -1
