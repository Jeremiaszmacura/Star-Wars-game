"""The module includes the Text class."""
import pygame
from const import Consts

class Text:
    """The subtitle class on the screen."""
    # pylint: disable=too-few-public-methods, too-many-instance-attributes

    def __init__(self, score, life_points):
        self.font = pygame.font.Font('freesansbold.ttf', Consts.FONT_SIZE_H1)
        self.text = self.font.render('Star Wars', True, Consts.MENU_FONT_COLOR)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (Consts.WINDOW_WIDTH // 2, Consts.WINDOW_HEIGHT //
                                 2 - Consts.FONT_SIZE_H2*2)

        self.font_02 = pygame.font.Font('freesansbold.ttf', Consts.FONT_SIZE_H2)
        self.text_02 = self.font_02.render("Select a level:", True, Consts.MENU_FONT_COLOR)
        self.text_rect_02 = self.text_02.get_rect()
        self.text_rect_02.center = (Consts.WINDOW_WIDTH // 2, Consts.WINDOW_HEIGHT // 2)

        self.font_03 = pygame.font.Font('freesansbold.ttf', Consts.FONT_SIZE_H3)
        self.text_03 = self.font_03.render("1-easy | 2-hard", True, Consts.MENU_FONT_COLOR)
        self.text_rect_03 = self.text_03.get_rect()
        self.text_rect_03.center = (Consts.WINDOW_WIDTH // 2, Consts.WINDOW_HEIGHT //
                                    2 + Consts.FONT_SIZE_H3*2)

        self.text_04 = self.font_03.render('Score: {}'.format(score), True,
                                           Consts.MENU_FONT_COLOR)
        self.text_rect_04 = self.text.get_rect()
        self.text_rect_04.center = (160, Consts.WINDOW_HEIGHT - Consts.FONT_SIZE_H3)

        self.text_05 = self.font_03.render('Life points: {}'.format(life_points),
                                           True, Consts.MENU_FONT_COLOR)
        self.text_rect_05 = self.text.get_rect()
        self.text_rect_05.center = (160, Consts.WINDOW_HEIGHT)

        self.text_06 = self.font_02.render('Your score: {}'.format(score)
                                           , True, Consts.MENU_FONT_COLOR)
        self.text_rect_06 = self.text_06.get_rect()
        self.text_rect_06.center = (Consts.WINDOW_WIDTH // 2, Consts.WINDOW_HEIGHT //
                                    2 - Consts.FONT_SIZE_H3*2)

        self.text_07 = self.font_03.render('Replay - wcisnij 3', True, Consts.MENU_FONT_COLOR)
        self.text_rect_07 = self.text_07.get_rect()
        self.text_rect_07.center = (Consts.WINDOW_WIDTH // 2, Consts.WINDOW_HEIGHT // 2)

        self.text_08 = self.font_03.render('Exit - wcisnij 4', True, Consts.MENU_FONT_COLOR)
        self.text_rect_08 = self.text_08.get_rect()
        self.text_rect_08.center = (Consts.WINDOW_WIDTH // 2, Consts.WINDOW_HEIGHT //
                                    2 + Consts.FONT_SIZE_H3*2)

    def score_and_life_points(self, score, life_points):
        """The method assigns content to the subtitles during the game."""
        self.text_04 = self.font_03.render('Score: {}'.format(score), True, Consts.MENU_FONT_COLOR)
        self.text_05 = self.font_03.render('Life points: {}'.format(life_points), True,
                                           Consts.MENU_FONT_COLOR)

    def end_menu_text(self, score):
        """The method displays the scored points on the end screen."""
        self.text_06 = self.font_02.render('Your score: {}'.format(score),
                                           True, Consts.MENU_FONT_COLOR)
