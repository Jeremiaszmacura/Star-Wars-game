"""Moduł zaweira klasę Text"""
import pygame

MENU_FONT_COLOR = (255, 255, 0)
FONT_SIZE_H1 = 64
FONT_SIZE_H2 = 32
FONT_SIZE_H3 = 24

class Text:
    """Klasa napisów na ekranie."""
    # pylint: disable=too-few-public-methods, too-many-instance-attributes

    def __init__(self, window_width, window_height, score, life_points):
        self.font = pygame.font.Font('freesansbold.ttf', FONT_SIZE_H1)
        self.text = self.font.render('Star Wars', True, MENU_FONT_COLOR)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (window_width // 2, window_height // 2 - FONT_SIZE_H2*2)

        self.font_02 = pygame.font.Font('freesansbold.ttf', FONT_SIZE_H2)
        self.text_02 = self.font_02.render("Wybierz poziom:", True, MENU_FONT_COLOR)
        self.text_rect_02 = self.text_02.get_rect()
        self.text_rect_02.center = (window_width // 2, window_height // 2)

        self.font_03 = pygame.font.Font('freesansbold.ttf', FONT_SIZE_H3)
        self.text_03 = self.font_03.render("1-łatwy | 2-trudny", True, MENU_FONT_COLOR)
        self.text_rect_03 = self.text_03.get_rect()
        self.text_rect_03.center = (window_width // 2, window_height // 2 + FONT_SIZE_H3*2)

        self.text_04 = self.font_03.render('Wynik: ' + str(score), True, (255, 255, 0))
        self.text_rect_04 = self.text.get_rect()
        self.text_rect_04.center = (160, window_height - FONT_SIZE_H3)

        self.text_05 = self.font_03.render('Punkty zycia: {}'.format(life_points),
                                           True, (255, 255, 0))
        self.text_rect_05 = self.text.get_rect()
        self.text_rect_05.center = (160, window_height)

        self.text_06 = self.font_02.render('Przegrales, Twoj wynik to: {}'.format(life_points)
                                           , True, (255, 255, 0))
        self.text_rect_06 = self.text.get_rect()
        self.text_rect_06.center = (window_width // 2, window_height // 2)

    def score_and_life_points(self, score, life_points):
        """Metoda przypisuje treść napisom podczas rozgrywki."""
        self.text_04 = self.font_03.render('Wynik: ' + str(score), True, (255, 255, 0))
        self.text_05 = self.font_03.render('Punkty zycia: ' + str(life_points), True, (255, 255, 0))
