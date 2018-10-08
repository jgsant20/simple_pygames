from logic_testing.bullet_shoot.run import *


class Enemy(pygame.sprite.Sprite):
    """Class to represent the enemies of the game"""
    frame_timer = 300

    def __init__(self, settings, screen, ship, x, y):
        super().__init__()
        self.settings = settings
        self.screen = screen
        self.ship = ship
        self.timer = Timer()

        self.images = find_file_type('./invader/*', '.png', self.settings.e_scale)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=(x, y))

        self.e_vel = self.settings.e_vel

        self.x = float(self.rect.centerx)
        self.y = float(self.rect.centery)

        self.radians = 0
        self.get_angle(x, y)

    def update(self):
        """Updates the ship's image and movement"""

        self.image = pygame.transform.rotate(self.image, 10)

        if self.timer.get_last() >= self.frame_timer:
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]
            self.timer.reset_timer()

    def get_angle(self, x, y):
        """Finds angle between ship and x, y coordinates"""
        try:
            self.radians = math.atan((x - self.ship.x) / (self.ship.y - y))
        except ZeroDivisionError:
            self.radians = 0

        if y > self.ship.y:
            self.radians += math.pi


    def spawn_enemy(self):
        #todo implement circle radius spawning with random on radians
        if self.timer_spawn.get_last() >= self.app.settings.e_spawn_delay and\
                self.app.settings.e_limit >= len(self.app.enemies):

            for i in range(1):
                # There's probably a better way to do this... But for now, choice is used so things can spawn either
                # on the side only, or on the top only

                choice = random.randint(0, 2)
                if choice == 0:
                    x = 0
                    y = random.randint(0, self.app.settings.RES_Y)
                elif choice == 1:
                    x = self.app.settings.RES_X - 100
                    y = random.randint(0, self.app.settings.RES_Y)
                else:
                    x = random.randint(0, self.app.settings.RES_X)
                    y = 0

                enemy = Enemy(self.app.settings, self.app.screen, self.app.ship, x, y)
                self.app.enemies.add(enemy)

                self.timer_spawn.reset_timer()
