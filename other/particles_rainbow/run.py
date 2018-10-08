import pygame
import sys
import time

from random import randint

RES_X = 1000
RES_Y = 1000

SIZE = 50


class Particle(pygame.sprite.Sprite):

    def __init__(self, x, y, screen):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(x, y, SIZE, SIZE)

    def random_color(self):
        self.rgb = randint(0,255), randint(0, 255), randint(0, 255)
        return self.rgb

    def update(self):
        pygame.draw.rect(self.screen, self.random_color(), self.rect)


pygame.init()

screen = pygame.display.set_mode((RES_X, RES_Y))

particles = pygame.sprite.Group()

rects = []

for x in range(0, RES_X, RES_X//SIZE):
    for y in range(0, RES_Y, RES_Y//SIZE):
        rect = Particle(x, y, screen)
        rects.append(rect)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    screen.fill((255, 255, 255))

    for rect in rects:
        rect.update()

    pygame.display.flip()


