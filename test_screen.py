"""Moduł zawiera testy jednostowe modułu screen.py."""
import time
import unittest
import pygame
from screen import Screen
from const import Consts

class Test_menu_control(unittest.TestCase):
    """Klasa zawiera testy jednostowe modułu screen.py."""

    def test_tie_fighters_time(self):
        """Check if time for acceleration function is working."""
        self.screen = pygame.display.set_mode((Consts.WINDOW_WIDTH, Consts.WINDOW_HEIGHT))
        self.ekran = Screen(self.screen)
        self.current_time = time.time()
        self.assertEqual(self.ekran.tie_fighter_accelerattion(self.current_time), self.current_time)
        self.assertEqual(self.ekran.tie_fighter_accelerattion(self.current_time-10), self.current_time)
        self.assertEqual(self.ekran.tie_fighter_accelerattion(self.current_time-5), self.current_time-5)
        self.assertEqual(self.ekran.tie_fighter_accelerattion(self.current_time-15), self.current_time-5)

    def test_tie_fighters_acceleration(self):
        """Check acceleration by the time play."""
        self.screen = pygame.display.set_mode((Consts.WINDOW_WIDTH, Consts.WINDOW_HEIGHT))
        self.ekran = Screen(self.screen)
        self.speed_x = self.ekran.tie_fighter_speed_x
        self.speed_y = self.ekran.tie_fighter_speed_y
        self.ekran.tie_fighter_accelerattion(time.time())
        self.assertEqual(self.ekran.tie_fighter_speed_x, self.speed_x)
        self.ekran.tie_fighter_accelerattion(time.time()-5)
        self.assertEqual(self.ekran.tie_fighter_speed_x, self.speed_x)
        self.ekran.tie_fighter_accelerattion(time.time()-10)
        self.assertEqual(self.ekran.tie_fighter_speed_x, self.speed_x+1)
        self.ekran.tie_fighter_accelerattion(time.time()-10)
        self.assertEqual(self.ekran.tie_fighter_speed_x, self.speed_x+2)

if __name__ == '__main__':
    unittest.main()
