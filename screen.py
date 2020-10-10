"""The module contains the Screen class."""
import math
import time
import pygame
from tie_fighter import TieFighter
from bullet import Bullet

class Screen:
    """The most extensive class of a program that includes related methods
       with screen background, enemy fighters, missiles, menu operation."""
    # pylint: disable=too-many-instance-attributes

    # Backgound
    def __init__(self, screen):
        self.restart = False
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
        self.tie_fighter_speed_x = 2
        self.tie_fighter_speed_y = 1

    # Tie Fighters
    def generate_tie_fighters(self):
        """The method generates enemy tie fighters and places them in the tie_fighters array."""
        while self.number_of_tie_fighters < self.number_limit_of_tie_fighters:
            self.tie_fighters.append(TieFighter(self.tie_fighter_speed_x, self.tie_fighter_speed_y))
            self.number_of_tie_fighters += 1

    def draw_tie_fighters(self, images):
        """The method draws enemy fighters on the screen."""
        to_del = []
        for i in range(len(self.tie_fighters)):
            # draw and assign true/false to out_of_gameboard
            out_of_gameboard = self.tie_fighters[i].draw_tie_fighter(self, images)
            if out_of_gameboard:
                to_del.append(i)
                self.life_points -= 1
        for j in reversed(to_del):
            del self.tie_fighters[j]
            self.number_of_tie_fighters -= 1

    def move_tie_fighters(self):
        """The method changes the coordinates of enemy fighters."""
        for i in range(len(self.tie_fighters)):
            self.tie_fighters[i].move_tie_fighter()

    def tie_fighter_accelerattion(self, current_time):
        """Acceleration of tie fighters along with the duration of the game."""
        if time.time() - current_time >= 10:
            self.tie_fighter_speed_x += 1
            self.tie_fighter_speed_y += 1
            return current_time + 10
        return current_time

    def move_limit_tie_fighters(self):
        """The method limits the field on which enemy tie fighters can move."""
        for i in range(len(self.tie_fighters)):
            self.tie_fighters[i].move_limitation()

    # Bullets
    def draw_bullets(self, images):
        """The method draws projectiles fired by the player on the screen."""
        to_del = []
        for i in range(len(self.bullets)):
            # rysuje i przypisuje true/false do out_of_gameboard
            out_of_gameboard = self.bullets[i].draw_bullet(self, images)
            if out_of_gameboard:
                to_del.append(i)
        for j in reversed(to_del):
            del self.bullets[j]

    def initiate_bullets(self, player_position_x, player_position_y):
        """The method initializes missile objects with the player's current coordinates."""
        self.bullets.append(Bullet(player_position_x, player_position_y))

    def is_collision(self):
        """The method checks if there was a collision between missiles and enemy fighters."""
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
        """The method adds menu control with keyboard buttons."""
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
                    self.restart = True
                    return False
                if event.key == pygame.K_4:
                    self.closing_menu = False
                    return False
        return True

    def have_i_lost(self):
        """The method checks whether the failure condition has been met."""
        if self.life_points <= 0:
            self.running = False
