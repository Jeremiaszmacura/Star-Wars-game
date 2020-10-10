"""The module contains the main program loops."""
import time
import pygame
from const import Consts, Assets
from text import Text
from player import Player
from screen import Screen

def clear(ekran):
    """The function clears arrays."""
    ekran.bullets.clear()
    ekran.tie_fighters.clear()

def start_menu(ekran, tekst, screen, background):
    """The function includes start menu loop."""
    while ekran.menu_running:
        screen.blit(background, (0, 0))  # Background image
        screen.blit(tekst.text, tekst.text_rect)  # opening credits
        screen.blit(tekst.text_02, tekst.text_rect_02)
        screen.blit(tekst.text_03, tekst.text_rect_03)
        ekran.menu_key_control()  # keyboard control
        pygame.display.update() # updated pygame changes

def game_loop(ekran, tekst, clock, gracz, screen, background, czas_rozgrywki, images):
    """The function includes game loop."""
    while ekran.running:
        # frames
        clock.tick(Consts.FPS)
        # generating objects
        ekran.generate_tie_fighters()
        # key control
        ekran.running = gracz.key_control(ekran)
        # drawing on the screen
        screen.blit(background, (0, 0))  # Background image
        gracz.draw_player(ekran, images)
        ekran.draw_tie_fighters(images)
        # moving
        gracz.move_player()
        ekran.move_tie_fighters()
        # bullets
        ekran.draw_bullets(images)
        # traffic restrictions
        gracz.move_limitation()
        ekran.move_limit_tie_fighters()
        # collision
        ekran.is_collision()
        # subtitles
        ekran.screen.blit(tekst.text_04, tekst.text_rect_04)
        ekran.screen.blit(tekst.text_05, tekst.text_rect_05)
        tekst.score_and_life_points(ekran.score, ekran.life_points)
        # failure conditions
        ekran.have_i_lost()
        czas_rozgrywki = ekran.tie_fighter_accelerattion(czas_rozgrywki)
        # makes any new updates on the screen visible
        pygame.display.update()

def end_menu(ekran, tekst, screen, background):
    """The function includes an end menu loop."""

    while ekran.closing_menu:
        screen.blit(background, (0, 0))  # Background image
        ekran.closing_menu = ekran.menu_key_control() # keyboard control
        screen.blit(tekst.text_06, tekst.text_rect_06)
        screen.blit(tekst.text_07, tekst.text_rect_07)
        screen.blit(tekst.text_08, tekst.text_rect_08)
        tekst.end_menu_text(ekran.score)
        if ekran.restart:
            main()
        pygame.display.update()

def main():
    """The main function of the program."""
    pygame.init()
    images = Assets()
    images.load()
    screen = pygame.display.set_mode((Consts.WINDOW_WIDTH, Consts.WINDOW_HEIGHT))
    pygame.display.set_caption("Star Wars")  # game name
    pygame.display.set_icon(images.ICON)
    background = pygame.transform.scale(images.BACKGROUND, (Consts.WINDOW_WIDTH,
                                                            Consts.WINDOW_HEIGHT))
    clock = pygame.time.Clock() # frame clock
    ekran = Screen(screen)  # creating a popup
    gracz = Player()  # creating a player object
    tekst = Text(ekran.score, ekran.life_points)
    start_menu(ekran, tekst, screen, background) # start menu loop
    czas_rozgrywki = time.time()
    # gameplay loop
    game_loop(ekran, tekst, clock, gracz, screen, background, czas_rozgrywki, images)
    end_menu(ekran, tekst, screen, background) # pętla menu end
    clear(ekran)

if __name__ == '__main__':
    main()
