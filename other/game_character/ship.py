import pygame

class Ship():
    """Creates and updates ship"""

    def __init__(self, screen, settings):
        """Creates game sprite and scales it according to window size"""
        self.screen = screen
        self.settings = settings

        # Loads image then gets rect of image
        self.image = pygame.image.load('images/cirno.png')
        self.image = pygame.transform.scale(self.image, (int(screen.get_width()/10), int(screen.get_width()/10)))
        self.rect = self.image.get_rect(center=(int(screen.get_width()/2), int(screen.get_height()/2)))
        self.screen_rect = self.screen.get_rect()

        # Flags for movement
        self.left_movement_flag = False
        self.right_movement_flag = False
        self.up_movement_flag = False
        self.down_movement_flag = False

        # Sprite's Speed
        self.speed = settings.ship_speed

        # Float ver of rect positions, because rect's store ints
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

    def update(self):
        if self.left_movement_flag and self.rect.left > 0:
            self.centerx -= self.speed
            self.rect.centerx = self.centerx
        if self.right_movement_flag and self.rect.right < self.screen_rect.right:
            self.centerx += self.speed
            self.rect.centerx = self.centerx
        if self.up_movement_flag and self.centery:
            self.centery -= self.speed and self.rect.top > 0
            self.rect.centery = self.centery
        if self.down_movement_flag and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.speed
            self.rect.centery = self.centery


    def blitme(self):
        """Updates location of sprite"""
        # first arg determines sprite image, second arg determines location
        self.screen.blit(self.image, self.rect)