"""Contains class for raindrops"""

import pygame
import random
import time

from pygame.sprite import Sprite


class Rain(Sprite):
    """Creates a raindrop"""

    def __init__(self, screen, settings):
        super().__init__()

        self.screen = screen
        self.scale = random.random() * 2

        loc_x = random.randint(0, settings.window_width)

        self.rect = pygame.Rect(loc_x, 0, settings.raindrop_width*self.scale, settings.raindrop_height*self.scale)
        
        # Attributes from settings
        self.gravity = settings.gravity
        self.speed = settings.raindrop_speed*self.scale
        self.rgb = settings.raindrop_rgb

        # Float vers of rect counterparts for more precise logging
        self.y = float(-100)
        self.width = float(settings.raindrop_width)

        self.start_time = time.clock()

    def update(self):
        """Updates the size and location of the raindrop"""
        self.velocity()
        # location
        self.y += self.speed
        self.rect.y = self.y

    def velocity(self):
        self.speed += (time.clock() - self.start_time) * self.gravity
        print(self.speed)

    def draw_rd(self):
        """Draws the raindrop"""
        pygame.draw.rect(self.screen, self.rgb, self.rect)