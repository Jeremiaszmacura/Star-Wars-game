import pygame
import math
from tie_fighter_class import Tie_fighter
from bullet_class import Bullet

class Screen:

    # Backgound
    def __init__(self):
        self.window_width = 800  # szerokosc okna
        self.window_height = 800  # wysokosc okna
        self.screen = pygame.display.set_mode((self.window_width, self.window_height)) #generowanie ekranu gry
        pygame.display.set_caption("Star Wars") #nazwa gry
        self.icon = pygame.image.load("assets/rebel-alliance.png")  # Ikona gry
        pygame.display.set_icon(self.icon)
        self.running = True
        self.menu_running = True
        self.closing_menu = True
        self.score = 0
        self.life_points = 5
        self.FPS = 120
        self.bullets = []
        self.tie_fighters = []
        self.number_of_tie_fighters = 0
        self.number_limit_of_tie_fighters = 2

    def set_background(self):
        self.background = pygame.image.load("assets/night_sky_2.png")  # Backgorund
        self.background = pygame.transform.scale(self.background, (self.window_width, self.window_height))

    def drawing_background(self):
        self.screen.blit(self.background, (0, 0))  # Background image

    # Tie Fighters
    def generate_tie_fighters(self):
        while self.number_of_tie_fighters < self.number_limit_of_tie_fighters:
            self.tie_fighters.append(Tie_fighter())
            self.number_of_tie_fighters += 1

    def draw_tie_fighters(self):
        to_del = []
        for i in range(len(self.tie_fighters)):
            out_of_gameboard = self.tie_fighters[i].draw_tie_fighter(self)  # rysuje i przypisuje true/false do out_of_gameboard
            if out_of_gameboard:
                to_del.append(i)
                self.life_points -= 1
        for j in reversed(to_del):
            del self.tie_fighters[j]
            self.number_of_tie_fighters -= 1

    def move_tie_fighters(self):
        for i in range(len(self.tie_fighters)):
            self.tie_fighters[i].move_tie_fighter()

    def move_limit_tie_fighters(self):
        for i in range(len(self.tie_fighters)):
            self.tie_fighters[i].move_limitation(self.window_width)

    # Bullets
    def draw_bullets(self):
        to_del = []
        for i in range(len(self.bullets)):
            out_of_gameboard = self.bullets[i].draw_bullet(self)  # rysuje i przypisuje true/false do out_of_gameboard
            if out_of_gameboard:
                to_del.append(i)
        for j in reversed(to_del):
            del self.bullets[j]

    def initiate_bullets(self, player_position_x, player_position_y, player_size):
        self.bullets.append(Bullet(player_position_x, player_position_y, player_size))

    def is_collision(self): # funkcja sprawdza czy doszlo do kolizji pomiedzy pociskiem, a mysliwcem
        to_del_tie_fighters = []
        to_del_bullets = []
        for i in range(len(self.tie_fighters)):
            for j in range(len(self.bullets)):
                distance = math.sqrt(math.pow(self.tie_fighters[i].position_x - self.bullets[j].position_x, 2) + math.pow(self.tie_fighters[i].position_y - self.bullets[j].position_y,2))
                if distance < 25:
                    to_del_tie_fighters.append(i)
                    to_del_bullets.append(j)
                    self.score += 1
        for i in reversed(to_del_tie_fighters):
            del self.tie_fighters[i]
            self.number_of_tie_fighters -= 1
        for j in reversed(to_del_bullets):
            del self.bullets[j]

    # menu
    def show_menu(self, tekst):
        self.screen.blit(tekst.text, tekst.textRect)  # napisy poczatkowe
        self.screen.blit(tekst.text_02, tekst.textRect_02)
        self.screen.blit(tekst.text_03, tekst.textRect_03)

    def menu_key_control(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.menu_running = False
                self.running = False
                self.closing_menu = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.number_limit_of_tie_fighters = 2
                    self.menu_running = False
                if event.key == pygame.K_2:
                    self.number_limit_of_tie_fighters = 3
                    self.menu_running = False
                if event.key == pygame.K_3:
                    self.menu_running = True
                    self.running = True
                    return True
                if event.key == pygame.K_4:
                    self.closing_menu = False
                    return False
        return True

    def haveILost(self):
        if self.life_points <= 0:
            self.running = False