import sys
import os
import pygame as pg

from pong import general_functions as gf
from pong.states import menu as m
from pong.states import game as g

# General Settings
res = 800, 450

# Calls all modules within pygame
pg.init()
screen = pg.display.set_mode(res)

# Text

dir_path = os.path.dirname(os.path.realpath(__file__))

font_title = pg.font.Font(dir_path + '\PressStart2P.ttf', int(res[0] / 12.8))
font_text001 = pg.font.Font(dir_path + '\PressStart2P.ttf', int(res[0] / 60))
font_text002 = pg.font.Font(dir_path + '\PressStart2P.ttf', int(res[0] / 100))

text001 = font_title.render("Pong", True, (255, 255, 255))
text002 = font_text001.render("One Player", True, (255, 255, 255))
text003 = font_text001.render("Two Player", True, (255, 255, 255))
text004 = font_text001.render("High Scores", True, (255, 255, 255))
text005 = font_text002.render("Special thanks to Pygame for being a pain in the ass to code with,"
                              , True, (255, 255, 255))
text006 = font_text002.render("but still being easy enough for me to use <3.", True, (255, 255, 255))

title = gf.surf_loc(screen, text001, (0.5, 0.2))
menu_texts = gf.surf_left_adjust(screen, (0.5, 0.5), .02, .035, text002, text003, text004)
bottomtexts = gf.surf_mid(screen, (0.5, 0.8), .03, text005, text006)

# Pointer for Text
pointers = gf.rect_even_vertical(screen, (10, 10), (0.4, 0.5), .055, 3)

menu_button = 0

# Menu
while True:

    # Event handler
    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            sys.exit(0)
        elif ev.type == pg.KEYDOWN:
            if ev.key == pg.K_s:
                menu_button += 1
            if ev.key == pg.K_w:
                menu_button -= 1
            if ev.key == pg.K_RETURN:
                if menu_button == 0:
                    pong = g.Pong(screen)
                    pong.run()
                if menu_button == 1:
                    pass
                if menu_button == 2:
                    pass
            elif ev.key == pg.K_F12:
                pass
                # possibly implement a fullscreen feature?

    # limits menu button num
    if menu_button < 0:
        menu_button = 0
    elif menu_button > 2:
        menu_button = 2

    screen.fill((0, 0, 0))
    pg.draw.rect(screen, (255, 255, 255), pointers[menu_button])

    # Blits all text
    title.blitme(screen)
    gf.listblitme(screen, menu_texts)
    gf.listblitme(screen, bottomtexts)

    pg.display.flip()
