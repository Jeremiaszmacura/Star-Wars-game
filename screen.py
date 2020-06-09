"""Moduł zawiera klasę Screen."""
import math

import pygame

from tie_fighter import TieFighter
from bullet import Bullet

class Screen:
    """Najbardziej obszerna klasa programu, która zawiera w sobie metody związane
       z tłem ekranu, myśliwcami przeciwnika, pociskami, obsługą menu."""
    # pylint: disable=too-many-instance-attributes

    # Backgound
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.menu_running = True
        self.closing_menu = True
        self.score = 0
        self.life_points = 5
        self.bullets = []
        self.tie_fighters = []
        self.number_of_tie_fighters = 0
        self.number_limit_of_tie_fighters = 2

    # Tie Fighters
    def generate_tie_fighters(self):
        """Metoda generuje wrogie myśliwce i umieszcza je w tablicy tie_fighters."""
        while self.number_of_tie_fighters < self.number_limit_of_tie_fighters:
            self.tie_fighters.append(TieFighter())
            self.number_of_tie_fighters += 1

    def draw_tie_fighters(self):
        """Metoda rysuje wrogie myśliwce na ekranie."""
        to_del = []
        for i in range(len(self.tie_fighters)):
            # rysuje i przypisuje true/false do out_of_gameboard
            out_of_gameboard = self.tie_fighters[i].draw_tie_fighter(self)
            if out_of_gameboard:
                to_del.append(i)
                self.life_points -= 1
        for j in reversed(to_del):
            del self.tie_fighters[j]
            self.number_of_tie_fighters -= 1

    def move_tie_fighters(self):
        """Metoda zmienia koordynaty wrogich myśliwców."""
        for i in range(len(self.tie_fighters)):
            self.tie_fighters[i].move_tie_fighter()

    def move_limit_tie_fighters(self):
        """Metoda ogranicza pole po jakim mogą się przemieszczać wrogie mysliwce."""
        for i in range(len(self.tie_fighters)):
            self.tie_fighters[i].move_limitation()

    # Bullets
    def draw_bullets(self):
        """Metoda rysuje na ekranie pociski wystrzelone przez gracza."""
        to_del = []
        for i in range(len(self.bullets)):
            # rysuje i przypisuje true/false do out_of_gameboard
            out_of_gameboard = self.bullets[i].draw_bullet(self)
            if out_of_gameboard:
                to_del.append(i)
        for j in reversed(to_del):
            del self.bullets[j]

    def initiate_bullets(self, player_position_x, player_position_y, player_size):
        """Metoda inicjuje obiekty pocisków o obecnych koordynatach gracza."""
        self.bullets.append(Bullet(player_position_x, player_position_y, player_size))

    def is_collision(self):
        """Metoda sprawdza czy doszło do kolizji pomiędzy pociskami, a wrogim myśliwcami"""
        to_del_tie_fighters = []
        to_del_bullets = []
        for i in range(len(self.tie_fighters)):
            for j in range(len(self.bullets)):
                distance = math.sqrt(math.pow(self.tie_fighters[i].position_x -
                                              self.bullets[j].position_x, 2) +
                                     math.pow(self.tie_fighters[i].position_y -
                                              self.bullets[j].position_y, 2))
                if distance < 25:
                    to_del_tie_fighters.append(i)
                    to_del_bullets.append(j)
                    self.score += 1
        for i in reversed(to_del_tie_fighters):
            del self.tie_fighters[i]
            self.number_of_tie_fighters -= 1
        for j in reversed(to_del_bullets):
            del self.bullets[j]

    def menu_key_control(self):
        """Metoda dodaje sterowanie menu przy pomocy przycisków klawiatury."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.menu_running = False
                self.running = False
                self.closing_menu = False
                return False
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

    def have_i_lost(self):
        """Metoda sprawdza czy został spełniony warunek przegranej."""
        if self.life_points <= 0:
            self.running = False
