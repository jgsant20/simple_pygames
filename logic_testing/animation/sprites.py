from logic_testing.animation import run


class Ship:
    # millisecond between frames
    frame_timer = 300

    def __init__(self, settings, screen):
        self.screen = screen
        self.timer = run.Timer()

        self.images = run.find_file_type('./jellyfish/*', '.png', .5)
        self.index = 0
        self.current_image = self.images[self.index]
        self.rect = self.current_image.get_rect(center=(300, 300))

        self.ship_speed = settings.ship_speed
        self.ship_slow_speed = settings.ship_slow_speed
        self.forward = False
        self.backward = False
        self.leftward = False
        self.rightward = False

        self.x = float(self.rect.centerx)
        self.y = float(self.rect.centery)

    def update(self):
        """Updates the ship's image and movement"""
        self.movement()

        if self.timer.get_last() >= self.frame_timer:
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.current_image = self.images[self.index]
            self.timer.reset_timer()

    def movement(self):
        if self.forward:
            self.y -= self.ship_speed
            self.rect.centery = self.y
        if self.backward:
            self.y += self.ship_speed
            self.rect.centery = self.y
        if self.leftward:
            self.x -= self.ship_speed
            self.rect.centerx = self.x
        if self.rightward:
            self.x += self.ship_speed
            self.rect.centerx = self.x

    def blitme(self):
        """Blits the ship onto the board"""
        self.screen.blit(self.current_image, self.rect)
