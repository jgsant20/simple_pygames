import pygame
import glob

import logic_testing.animation.sprites


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
    """Settings for the game"""

    def __init__(self):
        self.res_x = 1000
        self.res_y = 1000
        self.resolution = self.res_x, self.res_y
        self.FPS = 60

        # Ship settings
        self.ship_speed = 5
        self.ship_slow_speed = 2
        self.ship_scale = .5


class App:
    """Initializes the game"""

    def __init__(self):
        pygame.init()
        self.running = True
        self.paused = False

        self.settings = Settings()
        self.screen = pygame.display.set_mode(self.settings.resolution)
        self.ship = logic_testing.animation.sprites.Ship(self.settings, self.screen)
        self.clock = pygame.time.Clock()

    def run(self):
        """Runs the app"""

        while self.running:
            self.event_listener()
            self.ship.update()

            self.screen.fill((100, 100, 100))
            self.ship.blitme()
            pygame.display.flip()

            self.clock.tick(self.settings.FPS)

    def event_listener(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                self.running = False
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


    def paused(self):
        """Pauses the game"""

        while self.paused:
            print()
            #todo

    @staticmethod
    def on_exit():
        pygame.quit()


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