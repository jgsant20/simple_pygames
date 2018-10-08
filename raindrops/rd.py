import pygame

from pygame.sprite import Group
from raindrops.settings import Settings
import raindrops.game_functions as gf
from raindrops.rain import Rain


def run_game():
    """Displays raindrops falling"""

    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.window_width, settings.window_height))
    raindrops = Group()

    while True:
        gf.event_listener()
        gf.create_raindrops(screen, settings, raindrops)
        gf.updates(screen, settings, raindrops)


run_game()