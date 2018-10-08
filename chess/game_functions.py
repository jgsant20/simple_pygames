import pygame as pg
from chess.constants import *


def load_image(dr, extension):
    """Loads a list of files ending with 'extension' from directory 'dr' as screens"""
    scale = .10 * SCALE

    image = pg.image.load(dr + "" + extension)
    image = pg.transform.scale(image, (int(scale * RES[0]), int(scale * RES[1])))

    return image
