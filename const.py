"""Moduł zawiera zasoby i stałe potrzebne do gry."""
import pygame

class Consts:
    """Przechowuje stałe."""
    # pylint: disable=too-few-public-methods
    MENU_FONT_COLOR = (255, 255, 0)
    FONT_SIZE_H1 = 64
    FONT_SIZE_H2 = 32
    FONT_SIZE_H3 = 24
    FPS = 120
    WINDOW_WIDTH = 800  # szerokosc okna
    WINDOW_HEIGHT = 800
    ACCELERATION = 5
    TIE_FIGHTER_WIDTH = 64
    TIE_FIGHTER_HEIGHT = 64
    PLAYER_WIDTH = 64
    PLAYER_HEIGHT = 64

class Assets:
    """Przechowuje zasoby graficzne."""
    # pylint: disable=too-few-public-methods

    @classmethod
    def load(cls):
        cls.BACKGROUND = pygame.image.load("assets/night_sky_2.png")  # Backgorund
        cls.ICON = pygame.image.load("assets/rebel-alliance.png")  # Ikona gry
        cls.TIE_FIGHTER_IMG = pygame.image.load("assets/mysliwiec.png")
        cls.BULLET_IMG = pygame.image.load("assets/bullet_01.png")
        cls.PLAYER_IMG = pygame.image.load("assets/millennium_falcon.png")

