import math
import pygame

class Bullet:
    def __init__(self, player_position_x, player_position_y, player_size, speed = 4):
        self.bullet_img = pygame.image.load("assets/bullet_01.png")
        self.speed_y = speed
        self.position_x = player_position_x + player_size["x"] // 4
        self.position_y = player_position_y

    def draw_bullet(self, game_board):
        self.position_y -= self.speed_y
        game_board.screen.blit(self.bullet_img, (self.position_x, self.position_y))
        if(self.position_y <= 0):
            return True
        return False

    # def is_collision(self, enemy_position_x, enemy_position_y):  #funkcja sprawdzajaca czy doszlo do kolizji
    #     distance = math.sqrt((math.pow(enemy_position_x - self.position_x, 2) + math.pow(enemy_position_y - self.position_y, 2)))
    #     if distance < 25:
    #         return True
    #     else:
    #         return False