import sys
import pygame as pg

from pong import general_functions as gf


class Pong:

    def __init__(self, screen, bot=0):
        """
        Initializes Pong game
        :param screen: Display object
        :param bot: Determines whether it is one player or two player, also determines difficulty
            (bot = 0 Two player, bot = 1 One Player Easy, bot = 2 One Player Med, bot = 3 One Player Hard)
        :return:
        """

        # Settings
        self.pong_player_one_size = .15
        self.pong_player_two_size = .15
        self.pong_speed = .5

        self.screen = screen
        self.bot = bot
        self.resolution_size = screen.get_size()
        self.running = True

        self.top_bar = pg.Rect(0, 0, self.resolution_size[0], self.resolution_size[1] * .02)
        self.bottom_bar = pg.Rect(0, 0, self.resolution_size[0], self.resolution_size[1] * .02)
        self.top_bar.center = self.resolution_size[0] / 2, self.resolution_size[1] * .01
        self.bottom_bar.center = self.resolution_size[0] / 2, self.resolution_size[1] * .99

        self.middle_boxes = gf.rect_even_vertical(screen, (21, 21), (0.5, 0.5), .03, 17)

        self.left_paddle = pg.Rect(0, 0, self.resolution_size[0] * .01, self.resolution_size[1] * self.pong_player_one_size)
        self.left_paddle.center = self.resolution_size[0] * .03, self.resolution_size[1] * .5

        self.right_paddle = pg.Rect(0, 0, self.resolution_size[0] * .01, self.resolution_size[1] * self.pong_player_one_size)
        self.right_paddle.center = self.resolution_size[0] * .97, self.resolution_size[1] * .5

        self.paddles = [self.right_paddle, self.left_paddle]

        # 0 - Static, 1 - Up, 2 - Down
        self.p1_vertical_movement_direction = 0
        self.p2_vertical_movement_direction = 0

        self.p1_loc_centery = self.left_paddle.centery

    def run(self):

        # Runs the pong program
        while self.running:
            self.event_handler()
            self.logic()
            self.draw()
            pg.display.flip()

    def event_handler(self):

        # Iterates through each event object
        for ev in pg.event.get():
            if ev.type == pg.QUIT:                              # Exits out if 'esc' key is pressed
                sys.exit()
            if ev.type == pg.KEYDOWN:
                if ev.key == pg.K_w:                            # Changes movement of first player to up
                    self.p1_vertical_movement_direction = 1
                if ev.key == pg.K_s:                            # Changes movement of first player to down
                    self.p1_vertical_movement_direction = 2
            elif ev.type == pg.KEYUP:
                if ev.key == pg.K_w or ev.key == pg.K_s:
                    self.p1_vertical_movement_direction = 0

    def logic(self):

        # Movement
        if self.p1_vertical_movement_direction == 1:
            self.p1_loc_centery -= self.pong_speed
        if self.p1_vertical_movement_direction == 2:
            self.p1_loc_centery += self.pong_speed

        self.left_paddle.centery = self.p1_loc_centery

        # Restricts paddle from moving past the top and bottom bar
        if self.left_paddle.top < self.top_bar.bottom:     # Restricts for top
            self.left_paddle.top = self.top_bar.bottom
        elif self.left_paddle.bottom > self.bottom_bar.top:   # Restricts for bottom
            self.left_paddle.bottom = self.bottom_bar.top

    def draw(self):
        self.screen.fill((0, 0, 0))
        pg.draw.rect(self.screen, (200, 200, 200), self.top_bar)
        pg.draw.rect(self.screen, (200, 200, 200), self.bottom_bar)
        gf.listdrawme(self.screen, (200, 200, 200), self.middle_boxes)

        pg.draw.rect(self.screen, (255, 255, 255), self.left_paddle)
        pg.draw.rect(self.screen, (255, 255, 255), self.right_paddle)

        pass

    class Ball:
    """Class to represent ball"""

        def __init__(self, position):
            # Position, 0: left, 1: right
