"""The module contains unit tests of the screen.py module."""
import time
import unittest
import pygame
from screen import Screen
from tie_fighter import TieFighter
from const import Consts

class ScreenTest(unittest.TestCase):
    """The class contains unit tests for the screen.py module."""

    def setUp(self):
        """Initializes the resources needed to run tests."""
        self.screen = pygame.display.set_mode((Consts.WINDOW_WIDTH, Consts.WINDOW_HEIGHT))
        self.ekran = Screen(self.screen)

    def test_tie_fighters_time(self):
        """Check if time for acceleration function is working."""
        self.current_time = time.time()
        self.assertEqual(self.ekran.tie_fighter_accelerattion(self.current_time),
                         self.current_time)
        self.assertEqual(self.ekran.tie_fighter_accelerattion(self.current_time-10),
                         self.current_time)
        self.assertEqual(self.ekran.tie_fighter_accelerattion(self.current_time-5),
                         self.current_time-5)
        self.assertEqual(self.ekran.tie_fighter_accelerattion(self.current_time-15),
                         self.current_time-5)

    def test_tie_fighters_acceleration(self):
        """Check acceleration by the time play."""
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

    def test_lose_condition(self):
        """Check losing condition"""
        self.ekran.life_points = 5
        self.ekran.have_i_lost()
        self.assertTrue(self.ekran.running)
        self.ekran.life_points = 0
        self.ekran.have_i_lost()
        self.assertFalse(self.ekran.running)
        self.ekran.life_points = -5
        self.ekran.have_i_lost()
        self.assertFalse(self.ekran.running)

    def test_generate_tie_fighters(self):
        """Check is objects are generating properly"""
        self.ekran.generate_tie_fighters()
        self.assertTrue(isinstance(self.ekran.tie_fighters[0], TieFighter))

if __name__ == '__main__':
    unittest.main()
