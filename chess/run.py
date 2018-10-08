import pygame as pg
from chess.pieces import *

class App:

    def __init__(self):
        pg.init()

        self.screen = pg.display.set_mode(RES)
        self.board = Board(self.screen)

    def run(self):

        while True:
            self.event_listener()
            self.logic()
            pg.display.flip()

    def logic(self):
        for elements in self.board.board_rect:
            for element in elements:
                element.draw()

        for elements in self.board.board:
            for element in elements:
                if not isinstance(element, int):
                    element.update()
                    element.blitme()

    def event_listener(self):
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                pg.quit()
            if ev.type == pg.KEYDOWN:
                pass


class Board:

    def __init__(self, screen):
        self.screen = screen
        self.board = [[0 for i in range(BOARD_SIZE_X)] for j in range(BOARD_SIZE_Y)]
        self.board_rect = [[0 for i in range(BOARD_SIZE_X)] for j in range(BOARD_SIZE_Y)]
        self.set_up_board()
        self.set_up_pieces()

    def set_up_pieces(self):
        self.board = [[0 for i in range(BOARD_SIZE_X)] for j in range(BOARD_SIZE_Y)]
        print(self.board)
        for i in range(BOARD_SIZE_Y):
            self.board[1][i] = Pawn(WHITE, (1, i), self.screen, self.board_rect)

        for i in range(BOARD_SIZE_Y):
            self.board[BOARD_SIZE_X - 2][i] = Pawn(BLACK, (BOARD_SIZE_X - 2, i), self.screen, self.board_rect)

        self.board[0] = [Rook(WHITE, (0, 0), self.screen, self.board_rect),
                         Knight(WHITE, (0, 1), self.screen, self.board_rect),
                         Bishop(WHITE, (0, 2), self.screen, self.board_rect),
                         Queen(WHITE, (0, 3), self.screen, self.board_rect),
                         King(WHITE, (0, 4), self.screen, self.board_rect),
                         Bishop(WHITE, (0, 5), self.screen, self.board_rect),
                         Knight(WHITE, (0, 6), self.screen, self.board_rect),
                         Rook(WHITE, (0, 7), self.screen, self.board_rect)]

        self.board[BOARD_SIZE_X - 1] = [Rook(BLACK, (BOARD_SIZE_X - 1, 0), self.screen, self.board_rect),
                                        Knight(BLACK, (BOARD_SIZE_X - 1, 1), self.screen, self.board_rect),
                                        Bishop(BLACK, (BOARD_SIZE_X - 1, 2), self.screen, self.board_rect),
                                        Queen(BLACK, (BOARD_SIZE_X - 1, 3), self.screen, self.board_rect),
                                        King(BLACK, (BOARD_SIZE_X - 1, 4), self.screen, self.board_rect),
                                        Bishop(BLACK, (BOARD_SIZE_X - 1, 5), self.screen, self.board_rect),
                                        Knight(BLACK, (BOARD_SIZE_X - 1, 6), self.screen, self.board_rect),
                                        Rook(BLACK, (BOARD_SIZE_X - 1, 7), self.screen, self.board_rect)]

        white_pieces = []
        black_pieces = []

        for arr in self.board:
            for element in arr:
                if not isinstance(element, int):
                    if element.team == WHITE:
                        white_pieces.append(element)
                        element.available_movements(self.board)
                    elif element.team == BLACK:
                        black_pieces.append(element)
                        element.available_movements(self.board)

    def set_up_board(self):
        """Sets up the rects for the board"""

        flip = True

        # I got tired of coding
        for i in range(BOARD_SIZE_X):
            for j in range(BOARD_SIZE_Y):
                if flip:
                    flip = False
                    self.board_rect[i][j] = (BoardRect(self.screen, RGB_0,
                                                       (i * RES[0]/8 + RES[0]/16, j * RES[1]/8 + RES[0]/16), (i, j)))
                else:
                    flip = True
                    self.board_rect[i][j] = (BoardRect(self.screen, RGB_1,
                                                       (i * RES[0]/8 + RES[0]/16, j * RES[1]/8 + RES[0]/16), (i, j)))
            if flip:
                flip = False
            else:
                flip = True


class BoardRect:

    def __init__(self, screen, rgb, loc, coordinate):
        self.screen = screen
        self.rgb = rgb
        self.loc = loc
        self.coordinate = coordinate

        self.Rect = pg.Rect(loc, ((RES[0] / 8), (RES[1] / 8)))
        self.Rect.centerx = loc[0]
        self.Rect.centery = loc[1]

    def draw(self):
        pg.draw.rect(self.screen, self.rgb, self.Rect)


if __name__ == "__main__":
    app = App()
    app.run()
