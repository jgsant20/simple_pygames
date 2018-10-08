import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class to create a bullet to be sbot from the top of ship's image"""

    def __init__(self, screen, settings, ship):
        super().__init__()

        self.screen = screen

        spawn_x = ship.rect.centerx
        spawn_y = ship.rect.top

        self.rect = pygame.Rect(spawn_x, spawn_y, settings.bullet_width, settings.bullet_height)

        # Float ver of y coordinate for more precise movement
        self.y = float(spawn_y)

        self.speed = settings.bullet_speed
        self.rgb = settings.bullet_rgb

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(self.screen, self.rgb, self.rect)