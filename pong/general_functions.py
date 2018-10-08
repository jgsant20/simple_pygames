import pygame as pg

# source and surface are interchangeable keywords in this


class Surf:
    """Class that contains it's surface and location"""

    def __init__(self, surface, loc):
        self.surface = surface
        self.loc = loc

    def new_loc(self, x, y):
        self.loc = x, y

    def blitme(self, base):
        base.blit(self.surface, self.loc)


def listblitme(base, surfs):
    """Blits a list of surfaces"""
    for s in surfs:
        s.blitme(base)


def surf_loc(base, source, dest):
    """
    Creates a text object with a location
    :param base: Base surface
    :param source: Surface to blit onto base
    :param dest: Places source onto this scalable coordinate Ex. (0.5, 0.5) places it in the middle of base's x, y
    :return: Text object
    """

    source_size = source.get_size()
    base_size = base.get_size()

    x = base_size[0] * dest[0] - source_size[0] / 2
    y = base_size[1] * dest[1] - source_size[1] / 2

    return Surf(source, (x, y))


def surf_mid(base, dest, spacing, *source):
    """
    creates a text object with a location, middle adjusted
    :param base: Base surface
    :param dest: Places source onto this scalable coordinate, Ex. (0.5, 0.5) places it in the middle of base's x, y
    :param spacing: Spacing between surfaces
    :param source: Surface to blit onto base
    :return: Text object(s)
    """

    source_len = len(source)

    # I think there is something wrong with the spacing, not sure
    surfs = []
    for i in range(source_len):
        surfs.append(surf_loc(base, source[i], (dest[0], dest[1] + spacing*i)))

    return surfs


def surf_left_adjust(base, dest, offset, spacing, *surface):
    """
    Left adjusts objects a group of surface objects, centered at dest
    Used for surfaces of similar height
    Similar to left justifying text
    Every variable is based on a 0-1 scale
    :param base: Base surface
    :param dest: Center of group of surface objects
    :param offset: Offset distance from left
    :param spacing: Vertical distance between objects
    :param surface: Groups of surface objects
    :return: Text object(s)
    """

    scale_basex = base.get_width()
    scale_basey = base.get_height()

    offset_num = offset * scale_basex
    spacing_num = spacing * scale_basey
    dest_num = dest[0] * scale_basex, dest[1] * scale_basey
    surface_len = len(surface)
    surface_height = surface[0].get_height()

    # total length of each text combined
    width = max(surface, key=lambda s: s.get_width()).get_width()
    height = surface_len * (surface_height + spacing_num) - spacing_num

    # location of texts
    x = dest_num[0] - ((width + offset_num) / 2) + offset_num
    y = dest_num[1] - height / 2

    surfs = []

    for i in range(surface_len):
        surfs.append(Surf(surface[i], (x, y + (spacing_num + surface[0].get_height()) * i)))

    return surfs


def surf_right_adjust(base, dest, offset, spacing, *source):
    pass


def listdrawme(surface, color, rects):
    for rect in rects:
        pg.draw.rect(surface, color, rect)


def rect_even_vertical(base, size, dest, spacing, num):
    """
    Centers a number of rects around dest point, vertically
    :param base: Used only for scaling
    :param size: Size of blocks
    :param dest: Destination of center of rects, input number from 0-1, scales from resolution of screen
    :param spacing: Spacing between, input number from 0-1 scaled from res of screen
    :param num: Number of rects
    :return: A list of similarly sized rects
    """

    scale_basex = base.get_width()
    scale_basey = base.get_height()

    dest_num = dest[0] * scale_basex, dest[1] * scale_basey
    spacing_num = spacing * scale_basey

    # Initializes rects, will determine number
    vertical_distance = (num - 1) * (size[1] + spacing_num)

    print(size[0], size[1])

    rects = []
    for i in range(num):
        rect = pg.Rect(0, 0, size[0], size[1])
        rect.center = (dest_num[0], (dest_num[1] - vertical_distance / 2) + i * (spacing_num + size[1]))
        rects.append(rect)

    return rects


class Timer:
    """Contains a timer that runs continuously and a limited timer"""

    def __init__(self):
        self.accumulated_time = 0
        self.accumulated_time_last = 0
        self.start_time = pg.time.get_ticks()
        self.start_time_last = pg.time.get_ticks()
        self.running = True

    def pause(self):
        if not self.running:
            raise Exception('Time is already paused')
        self.running = False
        self.accumulated_time += pg.time.get_ticks() - self.start_time

    def resume(self):
        if self.running:
            raise Exception('Time is currently running')
        self.running = True
        self.start_time = pg.time.get_ticks()
        self.start_time_last = pg.time.get_ticks() - self.start_time_last

    def get(self):
        """Gets total time accumulated"""
        if self.running:
            return self.accumulated_time + pg.time.get_ticks() - self.start_time
        else:
            return self.accumulated_time

    def get_last(self):
        """Gets the time accumulated since last reset"""
        self.accumulated_time_last = pg.time.get_ticks() - self.start_time_last
        return self.accumulated_time_last

    def reset_timer(self):
        """Resets the timer"""
        self.start_time_last = pg.time.get_ticks()

