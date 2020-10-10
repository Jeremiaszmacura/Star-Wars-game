"""The module contains the Player class."""
import pygame
from const import Consts

class Player:
    """The player's class contains the methods needed to draw a player's object, change its coordinates,
     movement restriction, keyboard controls (controls)."""

    def __init__(self):
        self.position_x = Consts.WINDOW_WIDTH // 2 - Consts.PLAYER_WIDTH // 2
        self.position_y = Consts.WINDOW_HEIGHT - Consts.PLAYER_HEIGHT * 2
        self.speed_x = 0
        self.speed_y = 0

    def draw_player(self, game_board, images):
        """The method draws the player's object on the screen."""
        game_board.screen.blit(images.PLAYER_IMG, (self.position_x, self.position_y))

    def move_player(self):
        """The method changes the player's coordinates."""
        self.position_x += self.speed_x
        self.position_y += self.speed_y

    def move_limitation(self):
        """The method limits the space on which the player can move."""
        if self.position_x <= 0:
            self.position_x = 0
        elif self.position_x >= Consts.WINDOW_WIDTH - Consts.PLAYER_WIDTH:
            self.position_x = Consts.WINDOW_WIDTH - Consts.PLAYER_WIDTH
        if self.position_y >= Consts.WINDOW_HEIGHT - Consts.PLAYER_HEIGHT:
            self.position_y = Consts.WINDOW_HEIGHT - Consts.PLAYER_HEIGHT
        elif self.position_y <= 0:
            self.position_y = 0

    # key control
    def key_control(self, ekran):
        """The method supports the control of the player's object using the keyboard."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ekran.closing_menu = False
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.speed_x -= Consts.ACCELERATION
                if event.key == pygame.K_RIGHT:
                    self.speed_x += Consts.ACCELERATION
                if event.key == pygame.K_DOWN:
                    self.speed_y += Consts.ACCELERATION
                if event.key == pygame.K_UP:
                    self.speed_y -= Consts.ACCELERATION
                if event.key == pygame.K_SPACE:
                    ekran.initiate_bullets(self.position_x, self.position_y)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.speed_x = 0
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    self.speed_y = 0
        return True
