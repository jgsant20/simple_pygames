import sys
import math
import pygame


class Settings:
    FPS = 120
    RES_X = 1000
    RES_Y = 1000
    RES = RES_X, RES_Y
    RGB_bg = 30, 30, 30

    #ball
    ball_RGB = 200, 200, 200
    ball_friction = .005


class Ball(pygame.sprite.Sprite):

    def __init__(self, settings, screen, pos_x, pos_y, radius):
        super().__init__()
        self.settings = settings
        self.screen = screen

        # Shape
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.radius = radius

        # Movement
        self.friction = self.settings.ball_friction
        self.speed_x = 0
        self.speed_y = 0

        # Flags
        self.held_by_mouse = False

    def update(self):

        if not self.held_by_mouse:
            self.update_movement()
            self.check_mouse_collision()
            self.check_wall_collision()
        else:
            self.mouse_hold()

    def update_movement(self):
        if self.speed_x != 0:
            if self.friction != 0:
                self.speed_x = self.update_friction(self.speed_x)
            self.pos_x += self.speed_x
        if self.speed_y != 0:
            if self.friction != 0:
                self.speed_y = self.update_friction(self.speed_y)
            self.pos_y += self.speed_y

    #todo
    def update_friction(self, speed):
        def check_if_positive():
            return True if speed >= 0 else False

        original_pos = check_if_positive()

        speed -= self.friction if original_pos else self.friction*-1
        speed = 0 if check_if_positive() != original_pos else speed

        return speed

    def mouse_hold(self):
        self.speed_x = 0
        self.speed_y = 0

        self.pos_x, self.pos_y = pygame.mouse.get_pos()

    def check_mouse_collision(self):
        # Uses the distance formula in order to check if within radius
        x, y = pygame.mouse.get_pos()
        rel_x, rel_y = self.pos_x - x, self.pos_y - y

        dist = math.sqrt((rel_x ** 2 + rel_y ** 2))

        # Changes speed according to how close the pointer is
        if dist < self.radius:
            self.speed_x += rel_x / 100
            self.speed_y += rel_y / 100

    def check_wall_collision(self):

        # Separate in-case ball decides to clip into wall and endless loop
        if self.settings.RES_X < self.pos_x + self.radius:
            self.speed_x *= -1 if self.speed_x > 0 else 1
        elif 0 > self.pos_x - self.radius:
            self.speed_x *= -1 if self.speed_x < 0 else 1
        if self.settings.RES_Y < self.pos_y + self.radius:
            self.speed_y *= -1 if self.speed_y > 0 else 1
        elif 0 > self.pos_y - self.radius:
            self.speed_y *= -1 if self.speed_y < 0 else 1

    def draw(self):
        pygame.draw.circle(self.screen, self.settings.ball_RGB, (int(self.pos_x), int(self.pos_y)), self.radius)


class App:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(self.settings.RES)
        self.clock = pygame.time.Clock()

        self.balls = pygame.sprite.Group()
        self.ball = Ball(self.settings, self.screen,
                         self.settings.RES_X // 2, self.settings.RES_X // 2, 100)
        self.balls.add(self.ball)

    def run(self):

        while True:
            self.event_handler()
            self.balls.update()
            self.screen.fill(self.settings.RGB_bg)
            self.ball.draw()
            pygame.display.flip()
            self.clock.tick(self.settings.FPS)

    def event_handler(self):

        for event in pygame.event.get():
            sys.exit(0) if event.type == pygame.QUIT else None
            if event.type == pygame.MOUSEBUTTONDOWN:
                for ball in self.balls:
                    ball.held_by_mouse = True
            if event.type == pygame.MOUSEBUTTONUP:
                for ball in self.balls:
                    ball.held_by_mouse = False


if __name__ == "__main__":
    app = App()
    app.run()