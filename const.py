"""The module contains the resources and constants needed for the game."""
import pygame

class Consts:
    """Keeps constant values."""
    # pylint: disable=too-few-public-methods
    MENU_FONT_COLOR = (255, 255, 0)
    FONT_SIZE_H1 = 64
    FONT_SIZE_H2 = 32
    FONT_SIZE_H3 = 24
    FPS = 120
    WINDOW_WIDTH = 800  # window width
    WINDOW_HEIGHT = 800
    ACCELERATION = 5
    TIE_FIGHTER_WIDTH = 64
    TIE_FIGHTER_HEIGHT = 64
    PLAYER_WIDTH = 64
    PLAYER_HEIGHT = 64

class Assets:
    """It stores graphic resources."""
    # pylint: disable=too-few-public-methods

    @classmethod
    def load(cls):
        cls.BACKGROUND = pygame.image.load("assets/night_sky.png")  # Backgorund
        cls.ICON = pygame.image.load("assets/rebel_alliance.png")  # Game icon
        cls.TIE_FIGHTER_IMG = pygame.image.load("assets/tie_fighter.png")
        cls.BULLET_IMG = pygame.image.load("assets/bullet.png")
        cls.PLAYER_IMG = pygame.image.load("assets/millennium_falcon.png")

