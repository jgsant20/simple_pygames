"""Displays a sprite in the middle of window with pygame, then move it"""

import pygame

import game_character.game_functions as gf
from pygame.sprite import Group
from game_character.settings import Settings
from game_character.ship import Ship


def run():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.width, settings.height))
    pygame.display.set_caption("Game Character: Literally Useless")

    ship = Ship(screen, settings)
    bullets = Group()

    while True:
        gf.check_events(screen, settings, ship, bullets)
        ship.update()
        gf.update_screen(screen, ship, bullets, settings)


run()