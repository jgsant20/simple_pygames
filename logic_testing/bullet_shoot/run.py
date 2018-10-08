from logic_testing.bullet_shoot.game import *
import pygame, sys, glob


def find_file_type(dr, extension, scale=1):
    """Loads a list of files ending with 'extension' from directory 'dr' as screens"""
    file_names = glob.glob(dr)
    images = []

    for file_name in file_names:
        if file_name.endswith(extension):
            image = pygame.image.load(file_name)
            image = pygame.transform.scale(image, (int(scale*1000), int(scale*1000)))
            images.append(image)

    return images


class Settings:

    def __init__(self):
        self.FPS = 120
        self.RES_X = 1280
        self.RES_Y = 720
        self.RES = self.RES_X, self.RES_Y
        self.BG_RGB = 30, 30, 30

        # Bullet Settings
        self.b_x = 3
        self.b_y = 5
        self.b_vel = 10
        self.b_delay = 100
        self.b_rgb = 200, 200, 200
        self.b_limit = 100

        # Bullet Settings
        self.b_x_2 = 12
        self.b_y_2 = 30
        self.b_vel_2 = 10
        self.b_delay_2 = 100
        self.b_limit_2 = 100

        # Enemy Settings
        self.e_x = 50
        self.e_y = 50
        self.e_vel = .1
        self.e_spawn_delay = 25
        self.e_rgb = 0, 0, 0
        self.e_scale = .05
        self.e_limit = 1000
        self.e_rad_spawn = self.RES_Y / 2

        # Ship settings
        self.ship_x = self.RES_X / 2
        self.ship_y = self.RES_Y / 2
        self.ship_vel = 5
        self.ship_slow_vel = 2
        self.ship_scale = .1


class App:
    """Class to initialize the game"""

    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode(self.settings.RES)
        self.game = Game(self)
        self.clock = pygame.time.Clock()

        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.ship = Ship(self.settings, self.screen)

    def run(self):
        """Runs the game"""
        while True:
            self.event_handler()
            self.game.logic()
            self.enemies.update()
            self.ship.update()
            self.bullets.update()

            self.screen.fill(self.settings.BG_RGB)

            # Draws onto screen
            for bullet in self.bullets:
                # For efficiency, I put check if bullet is outside of window for deletion in here
                if not (0 < bullet.x < self.settings.RES_X and
                        0 < bullet.y < self.settings.RES_Y):
                    self.bullets.remove(bullet)
                bullet.draw()

            for enemy in self.enemies:
                enemy.draw()

            self.ship.blitme()

            # Shows screen
            pygame.display.flip()

            # FPS
            self.clock.tick(self.settings.FPS)

    def event_handler(self):
        """Handles key-presses and mouse movements for the game"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.game.shooting = True
            elif event.type == pygame.MOUSEBUTTONUP:
                self.game.shooting = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w: self.ship.forward = True
                if event.key == pygame.K_s: self.ship.backward = True
                if event.key == pygame.K_a: self.ship.leftward = True
                if event.key == pygame.K_d: self.ship.rightward = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w: self.ship.forward = False
                if event.key == pygame.K_s: self.ship.backward = False
                if event.key == pygame.K_a: self.ship.leftward = False
                if event.key == pygame.K_d: self.ship.rightward = False


class Timer:
    """Contains a timer that runs continuously and a limited timer"""

    def __init__(self):
        self.accumulated_time = 0
        self.accumulated_time_last = 0
        self.start_time = pygame.time.get_ticks()
        self.start_time_last = pygame.time.get_ticks()
        self.running = True

    def pause(self):
        if not self.running:
            raise Exception('Time is already paused')
        self.running = False
        self.accumulated_time += pygame.time.get_ticks() - self.start_time

    def resume(self):
        if self.running:
            raise Exception('Time is currently running')
        self.running = True
        self.start_time = pygame.time.get_ticks()
        self.start_time_last = pygame.time.get_ticks() - self.start_time_last

    def get(self):
        """Gets total time accumulated"""
        if self.running:
            return self.accumulated_time + pygame.time.get_ticks() - self.start_time
        else:
            return self.accumulated_time

    def get_last(self):
        """Gets the time accumulated since last reset"""
        self.accumulated_time_last = pygame.time.get_ticks() - self.start_time_last
        return self.accumulated_time_last

    def reset_timer(self):
        """Resets the timer"""
        self.start_time_last = pygame.time.get_ticks()


if __name__ == "__main__":
    app = App()
    app.run()
