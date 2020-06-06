"""Moduł zawiera główne pętle programu"""
import pygame

from text import Text
from player import Player
from screen import Screen

def start_menu(ekran, tekst):
    """Funkcja zawiera pętle menu startowego"""
    while ekran.menu_running:
        ekran.drawing_background()  # rysowanie obrazu jako tlo
        ekran.show_menu(tekst) # wyswietlenie menu
        ekran.menu_key_control()  # kontrola klawiatury
        pygame.display.update() # aktualizacja zmian pygame

def game_loop(ekran, tekst, clock, gracz):
    """Funkcja zawiera główną pętlę rozgrywki"""
    while ekran.running:
        # klatkowanie
        clock.tick(ekran.fps)
        # generowanie obiektow
        ekran.generate_tie_fighters()
        # kontrola klawiszy
        ekran.running = gracz.key_control(ekran)
        # rysowanie na ekranie
        ekran.drawing_background()
        gracz.draw_player(ekran)
        ekran.draw_tie_fighters()
        # przemieszczanie sie
        gracz.move_player()
        ekran.move_tie_fighters()
        # pociski
        ekran.draw_bullets()
        # ograniczenia ruchu
        gracz.move_limitation(ekran.window_width, ekran.window_height)
        ekran.move_limit_tie_fighters()
        # kolizja
        ekran.is_collision()
        # napisy
        ekran.screen.blit(tekst.text_04, tekst.text_rect_04)
        ekran.screen.blit(tekst.text_05, tekst.text_rect_05)
        tekst.score_and_life_points(ekran.score, ekran.life_points)
        # warunki przegranej
        ekran.have_i_lost()
        # makes any new updates on the screen visible
        pygame.display.update()

def end_menu(ekran, tekst):
    """Funkcja zawiera pętlę końcowego menu"""

    while ekran.closing_menu:
        ekran.drawing_background()
        ekran.closing_menu = ekran.menu_key_control()  # kontrola klawiatury
        ekran.show_closing_menu(tekst)
        pygame.display.update()

def main():
    """Funkcja main programu"""
    pygame.init()
    clock = pygame.time.Clock() # zegar do klatkowania
    ekran = Screen()  # tworzenie okienka
    gracz = Player(ekran.window_width, ekran.window_height)  # tworzenie obiektu gracz
    tekst = Text(ekran.window_width, ekran.window_height, ekran.score, ekran.life_points)
    start_menu(ekran, tekst) # pętla menu start
    game_loop(ekran, tekst, clock, gracz) # pętla rozgrywki
    end_menu(ekran, tekst) # pętla menu end

if __name__ == '__main__':
    main()
