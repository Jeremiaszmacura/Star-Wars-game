import pygame

class Text:
    """Klasa napisów na ekranie."""

    """Jest odpowiedzialna za treść, która pojawia się na ekranie startowego menu, na ekranie
    podczas rozgrywki oraz na ekranie końcowego menu. Metody klasy to: konstruktor, closing_subtitles,
    scoreAndLifePoints. Atrybutami klasy są: font, text, textRect, font_02, text_02, textRect_02, font_03, text_03,
    textRect_03, text_04, textRect_04, text_05, textRect_05."""

    yellow = (255, 255, 0)

    def __init__(self, window_width, window_height, score, life_points, font_size_h1 = 64, font_size_h2 = 32, font_size_h3 = 24):
        self.font = pygame.font.Font('freesansbold.ttf', font_size_h1)  # font = pygame.font.Font(None, size)
        self.text = self.font.render('Star Wars', True, self.yellow)
        self.textRect = self.text.get_rect()
        self.textRect.center = (window_width // 2, window_height // 2 - font_size_h2*2)

        self.font_02 = pygame.font.Font('freesansbold.ttf', font_size_h2)
        self.text_02 = self.font_02.render("Wybierz poziom:", True, self.yellow)
        self.textRect_02 = self.text_02.get_rect()
        self.textRect_02.center = (window_width // 2, window_height // 2)

        self.font_03 = pygame.font.Font('freesansbold.ttf', font_size_h3)
        self.text_03 = self.font.render("1-łatwy | 2-trudny", True, self.yellow)
        self.textRect_03 = self.text_03.get_rect()
        self.textRect_03.center = (window_width // 2, window_height // 2 + font_size_h2*2)

        #self.font_04 = pygame.font.Font('freesansbold.ttf', font_size_h3)  # font = pygame.font.Font(None, size)
        self.text_04 = self.font_03.render('Wynik: ' + str(score), True, (255, 255, 0))
        self.textRect_04 = self.text.get_rect()
        self.textRect_04.center = (160, window_height - font_size_h3)

        #self.font_05 = pygame.font.Font('freesansbold.ttf', font_size_h3)  # font = pygame.font.Font(None, size)
        self.text_05 = self.font_03.render('Punkty zycia: ' + str(life_points), True, (255, 255, 0))
        self.textRect_05 = self.text.get_rect()
        self.textRect_05.center = (160, window_height)

    def closing_subtitles(self, window_width, window_height):
        """Metoda przypisuje treść napisom końcowego menu."""
        pass

    def scoreAndLifePoints(self, score, life_points):
        """Metoda przypisuje treść napisom podczas rozgrywki."""
        self.text_04 = self.font_03.render('Wynik: ' + str(score), True, (255, 255, 0))
        self.text_05 = self.font_03.render('Punkty zycia: ' + str(life_points), True, (255, 255, 0))