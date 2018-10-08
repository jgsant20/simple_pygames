import sys
import time

import pygame as pg
import logic_testing.bullet_dodge.game_functions as gf


class Settings:

    def __init__(self):
        # Window
        self.RES = 600, 600
        self.RES_X = self.RES[0]
        self.RES_Y = self.RES[1]
        self.BG_Color = 30, 30, 30


class App:

    def __init__(self):
        pg.init()
        self.settings = Settings()
        self.screen = pg.display.set_mode(self.settings.RES_X, self.settings.RES_Y)

    def run(self):

        while True:
            self.screen.fill(self.settings.BG_Color)

            pg.display.flip()

