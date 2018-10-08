"""Shoot aliens down with Cirno-chan!"""

import pygame

import alien_invasion.game_functions as gf
from alien_invasion.settings import Settings
from alien_invasion.ship import Ship
from pygame.sprite import Group

def run_game():
    """"Runs the game"""

    pygame.init()
    settings = Settings()

    screen = pygame.display.set_mode((settings.width, settings.height))
    pygame.display.set_caption("Alien Invasion: Cirno Edition")

    # Make a ship
    ship = Ship(screen, settings)

    # Make a group for bullets and aliens, used for storing
    bullets = Group()
    aliens = Group()

    gf.create_fleet(settings, screen, ship, aliens)

    while True:
        gf.check_events(screen, settings, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_aliens(settings, aliens)
        gf.remove_bullet(bullets)
        gf.update_screen(settings, screen, ship, aliens, bullets)
        gf.check_mouse_collision(aliens, bullets)


run_game()