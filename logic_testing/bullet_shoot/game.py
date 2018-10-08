from logic_testing.bullet_shoot.run import *
import pygame, random, math


class Game:
    """Class for the game functions"""

    def __init__(self, app):
        self.app = app
        self.timer_spawn = Timer()
        self.timer_shoot = Timer()

        # Flags
        self.shooting = False

        # Vars
        self.radians = 0

    def logic(self):
        #self.shoot()
        self.shoot_2()

    def shoot(self):
        if self.timer_shoot.get_last() >= self.app.settings.b_delay and\
           self.app.settings.b_limit >= len(self.app.bullets):

            if self.shooting:
                self.get_angle(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                self.app.bullets.add(Bullet(self.app.settings, self.app.screen,
                                            self.app.ship.x, self.app.ship.y, self.radians))
                self.timer_shoot.reset_timer()

    def shoot_2(self):
        if self.timer_shoot.get_last() >= self.app.settings.b_delay and\
           self.app.settings.b_limit >= len(self.app.bullets):

            if self.shooting:
                self.get_angle(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                self.app.bullets.add(Bullet2(self.app.settings, self.app.screen,
                                              self.app.ship.x, self.app.ship.y, self.radians))
                self.app.bullets.add(Bullet2(self.app.settings, self.app.screen,
                                              self.app.ship.x, self.app.ship.y, self.radians + (math.pi / 12)))
                self.app.bullets.add(Bullet2(self.app.settings, self.app.screen,
                                              self.app.ship.x, self.app.ship.y, self.radians - (math.pi / 12)))
                self.timer_shoot.reset_timer()

    def get_angle(self, x, y):
        """Finds angle between ship and x, y coordinates, 0 rad starting at 12 o clock"""
        try:
            self.radians = math.atan((x - self.app.ship.x) / (self.app.ship.y - y))
        except ZeroDivisionError:
            self.radians = 0

        if y > self.app.ship.y:
            self.radians += math.pi


class Bullet(pygame.sprite.Sprite):
    """Class for bullets"""

    def __init__(self, settings, screen, x, y, radian):
        super().__init__()
        self.settings = settings
        self.screen = screen
        self.rect = pygame.Rect(x, y, self.settings.b_x, self.settings.b_y)

        self.vel_x = self.settings.b_vel * math.sin(radian)
        self.vel_y = self.settings.b_vel * math.cos(radian)

        self.x = self.rect.x
        self.y = self.rect.y

    def update(self):
        self.x += self.vel_x
        self.y -= self.vel_y

        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(self.screen, self.settings.b_rgb, self.rect)


class Bullet2(pygame.sprite.Sprite):
    """Class for special rainbow bullets"""

    def __init__(self, settings, screen, x, y, radian):
        super().__init__()
        self.settings = settings
        self.screen = screen
        self.timer = Timer()
        self.rect = pygame.Rect(x, y, self.settings.b_x_2, self.settings.b_y_2)

        self.vel_x = self.settings.b_vel * math.sin(radian)
        self.vel_y = self.settings.b_vel * math.cos(radian)

        self.x = self.rect.x
        self.y = self.rect.y

    def update(self):
        self.x += self.vel_x
        self.y -= self.vel_y

        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(self.screen, self.get_rgb(), self.rect)

    def get_rgb(self):
        rgb = (self.rect.x + self.timer.get() * 30) % 255, \
              (self.rect.x + self.timer.get() / 30) % 255, (self.rect.x + self.timer.get()) % 255
        return rgb


class Ship:
    # millisecond between frames
    frame_timer = 300

    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen
        self.timer = Timer()

        self.images = find_file_type('./jellyfish/*', '.png', self.settings.ship_scale)
        self.index = 0
        self.current_image = self.images[self.index]
        self.rect = self.current_image.get_rect(center=(self.settings.ship_x, self.settings.ship_y))

        self.ship_vel = self.settings.ship_vel
        self.ship_slow_vel = self.settings.ship_slow_vel
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
            self.y -= self.ship_vel
            self.rect.centery = self.y
        if self.backward:
            self.y += self.ship_vel
            self.rect.centery = self.y
        if self.leftward:
            self.x -= self.ship_vel
            self.rect.centerx = self.x
        if self.rightward:
            self.x += self.ship_vel
            self.rect.centerx = self.x

    def blitme(self):
        """Blits the ship onto the board"""
        self.screen.blit(self.current_image, self.rect)
