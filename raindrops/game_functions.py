import sys
import pygame
import random

from raindrops.rain import Rain


def event_listener():
    """Checks for events from keypresses and mouse movements"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(1)


def create_raindrops(screen, settings, raindrops):
    """Randomizes amount of raindrop dropped at a time"""
    total_raindrop = random.randint(0, 10)

    for raindrop_num in range(0, total_raindrop):
        new_raindrop = Rain(screen, settings)
        raindrops.add(new_raindrop)


def updates(screen, settings, raindrops):
    """Updates screen"""
    screen.fill(settings.rgb_colors)
    raindrops_update(settings, raindrops)
    pygame.display.flip()


def raindrops_update(settings, raindrops):
    """Updates raindrops"""
    # updates speed of raindrop
    raindrops.update()

    # deletes raindrop if out of sight, else draws onto screen
    for raindrop in raindrops:
        if raindrop.rect.y >= settings.window_height:
            raindrops.remove(raindrop)
        else:
            raindrop.draw_rd()