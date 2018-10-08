import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Creates and emulates bullet functions"""

    def __init__(self, screen, settings, ship):
        """Creates bullet object at the ship's current position"""
        super().__init__()
        self.screen = screen

        # Creates bullet at top-center of ship
        self.rect = pygame.Rect(ship.rect.centerx, ship.rect.top,
            settings.bullet_width, settings.bullet_height)

        # Stores bullet position in a float
        self.y = float(ship.rect.y)

        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor

    def update(self):
        """Moves the bullet up the screen"""
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """Draws bullet onto screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)