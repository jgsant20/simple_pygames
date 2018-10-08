import pygame as pg
from chess.settings import *

class Buttons:
    """Universal buttons class
        Contains metadata such as picture, rect, etc
        Coordinate based"""
    def __init__(self):
        pass


class App:
    """Initializes pygame"""
    def __init__(self):
        pg.init()
        pg.mixer.init()

    def run(self):
        """After initialized, run this to launch the menu"""
        self.menu = Menu()


class Menu:
    """Launches the main menu of the game"""
    def __init__(self):
        self.running = True

        self.button_num = [0, 0]

        self.limit = [5]
        self.screen = pg.display.set_mode(res)
        self.create_buttons()

        self.run()

    def create_buttons(self):
        self.font = pg.font.SysFont(font, font_size)
        self.item_names = ["Start Game", "Continue", "Options", "Exit"]

    def run(self):
        """Runs the menu"""
        self.running = True

        while self.running:
            self.event_handler()
            self.logic()
            self.screen.fill(bg_color)
            pg.display.flip()

    def logic(self):

        # Provides the limit for button_num,
        # Changes depending on menu location
        if 0 > self.button_num[1]:
            self.button_num = 0
        if self.limit[self.button_num[0]] < self.button_num[0]:
            self.button_num = self.limit[1]

    def logic_forward(self):
        if self.button_num == [0, 1]:
            self.running = False
            self.start_game_flag = True

    def logic_back(self):


    def event_handler(self):
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                self.running = False
            elif ev.type == pg.KEYDOWN:
                if ev.key == pg.K_DOWN:
                    self.button_num += 1
                if ev.key == pg.K_UP:
                    self.button_num -= 1
                if ev.key == pg.K_ESCAPE:
                    self.logic_back()
                if ev.key == pg.K_KP_ENTER:
                    self.logic_forward()


if __name__ == "__main__":
    game = App()
    game.run()
