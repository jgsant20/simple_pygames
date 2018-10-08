import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Emulates and creates an alien ship"""

    def __init__(self, screen, settings):
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen = screen
        self.settings = settings

        # Loads the alien image, scales it, then set its rect attribute
        self.image = pygame.image.load('images/alien_ship_grey.png')
        self.image = pygame.transform.scale(self.image, (int(self.settings.width/25), int(self.settings.width/25)))
        self.rect = self.image.get_rect()

        # Start alien ship at top left of screen
        self.rect.x = self.settings.width/10
        self.rect.y = self.settings.height/10

        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Updates position of alien"""
        self.x += self.settings.alien_speed_factor * self.settings.fleet_direction
        self.rect.x = self.x

    def blitme(self):
        """Draws the alien sprite"""
        self.screen.blit(self.image, self.rect)