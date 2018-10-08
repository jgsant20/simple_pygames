import pygame

class Ship():
    """Creates and emulates the user's ship"""


    def __init__(self, screen, settings):
        """Creates the user's ship"""
        self.screen = screen
        self.settings = settings

        # Loads image of ship to game, then scales according to window
        self.image = pygame.image.load('images/cirno.png')
        self.image = pygame.transform.scale(self.image, (int(screen.get_width()/10), int(screen.get_width()/10)))
        self.rect = self.image.get_rect()

        # Sets image to bottom center according to screen
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center
        self.center = float(self.rect.centerx)

        # Movement flag
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """Update's the ship's position based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed_factor

        # Update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Updates the user's ship"""
        self.screen.blit(self.image, self.rect)