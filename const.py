"""Moduł zawiera zasoby i stałe potrzebne do gry"""
import pygame

class Assets:
    """Przechowuje zasoby graficzne"""
    # pylint: disable=too-few-public-methods
    MENU_FONT_COLOR = (255, 255, 0)
    FONT_SIZE_H1 = 64
    FONT_SIZE_H2 = 32
    FONT_SIZE_H3 = 24
    FPS = 120
    WINDOW_WIDTH = 800  # szerokosc okna
    WINDOW_HEIGHT = 800
    ACCELERATION = 5
    BACKGROUND = pygame.image.load("assets/night_sky_2.png")  # Backgorund
    ICON = pygame.image.load("assets/rebel-alliance.png")  # Ikona gry
    tie_fighter_img = pygame.image.load("assets/mysliwiec.png")
    tie_fighter_size = {"x": 64, "y": 64}
    bullet_img = pygame.image.load("assets/bullet_01.png")
    player_img = pygame.image.load("assets/millennium_falcon.png")
    player_size = {"x": 64, "y": 64}

