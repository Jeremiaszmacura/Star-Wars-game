"""Moduł zawiera główne pętle programu."""
import pygame

from const import Assets
from text import Text
from player import Player
from screen import Screen

def start_menu(ekran, tekst, screen, background):
    """Funkcja zawiera pętle menu startowego."""
    while ekran.menu_running:
        screen.blit(background, (0, 0))  # Background image
        screen.blit(tekst.text, tekst.text_rect)  # napisy poczatkowe
        screen.blit(tekst.text_02, tekst.text_rect_02)
        screen.blit(tekst.text_03, tekst.text_rect_03)
        ekran.menu_key_control()  # kontrola klawiatury
        pygame.display.update() # aktualizacja zmian pygame

def game_loop(ekran, tekst, clock, gracz, screen, background):
    """Funkcja zawiera główną pętlę rozgrywki."""
    while ekran.running:
        # klatkowanie
        clock.tick(Assets.FPS)
        # generowanie obiektow
        ekran.generate_tie_fighters()
        # kontrola klawiszy
        ekran.running = gracz.key_control(ekran)
        # rysowanie na ekranie
        screen.blit(background, (0, 0))  # Background image
        gracz.draw_player(ekran)
        ekran.draw_tie_fighters()
        # przemieszczanie sie
        gracz.move_player()
        ekran.move_tie_fighters()
        # pociski
        ekran.draw_bullets()
        # ograniczenia ruchu
        gracz.move_limitation()
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

def end_menu(ekran, tekst, screen, background):
    """Funkcja zawiera pętlę końcowego menu."""

    while ekran.closing_menu:
        screen.blit(background, (0, 0))  # Background image
        ekran.closing_menu = ekran.menu_key_control()  # kontrola klawiatury
        screen.blit(tekst.text_06, tekst.text_rect_06)
        pygame.display.update()

def main():
    """Funkcja main programu."""
    pygame.init()

    screen = pygame.display.set_mode((Assets.WINDOW_WIDTH, Assets.WINDOW_HEIGHT))
    pygame.display.set_caption("Star Wars")  # nazwa gry
    pygame.display.set_icon(Assets.ICON)
    background = pygame.transform.scale(Assets.BACKGROUND, (Assets.WINDOW_WIDTH, Assets.WINDOW_HEIGHT))

    clock = pygame.time.Clock() # zegar do klatkowania
    ekran = Screen(screen)  # tworzenie okienka
    gracz = Player()  # tworzenie obiektu gracz
    tekst = Text(ekran.score, ekran.life_points)
    start_menu(ekran, tekst, screen, background) # pętla menu start
    game_loop(ekran, tekst, clock, gracz, screen, background) # pętla rozgrywki
    end_menu(ekran, tekst, screen, background) # pętla menu end

if __name__ == '__main__':
    main()
