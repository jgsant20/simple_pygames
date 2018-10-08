from chess.constants import *
import chess.game_functions as gf


def check_area(loc, board):
    """Checks if there is a piece located at given location (loc)
        -2 for index error
        -1 for no team at space
        BLACK for black
        WHITE for white
        """

    # Because Python is weird and -1 is equal to last index
    if loc[0] < 0 or loc[1] < 0:
        return -2

    try:
        team = board[loc[0]][loc[1]].team
    except AttributeError:
        return -1
    except IndexError:
        return -2

    return team


def check_line(loc, board, x, y, max=100):
    """Returns a list of possible locations in a line, with given original location (loc)
        Will by x/y amount for every integer (Ex. go diagonally if input x and y, go left/right if x +/- and y = 0)
        """

    elements = []
    i = 1
    flag = check_area((loc[0] + x * i, loc[1] + y * i), board)

    # max - 1 because it appends before adding
    while flag == -1 and i <= max - 1:
        elements.append((loc[0] + x * i, loc[1] + y * i))
        i += 1
        flag = check_area((loc[0] + x * i, loc[1] + y * i), board)

    if flag not in (board[loc[0]][loc[1]].team, -2):
        elements.append((loc[0] + x * i, loc[1] + y * i))

    return elements


def check_area_move(loc, board, x, y):
    """Returns an element if movement is possible, by moving x and y distance"""

    if check_area((loc[0] + x, loc[1] + y), board) not in [-2, board[loc[0]][loc[1]].team]:
        return loc[0] + x, loc[1] + y


def check_list_line(loc, board, possible_moves, max=100):
    """Uses check_line with a list of (x, y)'s"""

    elements = []

    for possible_move in possible_moves:
        elements.extend(check_line(loc, board, possible_move[0], possible_move[1], max))

    # Gets ride of Nonetypes
    elements = [element for element in elements if element is not None]

    return elements


def check_list_area(loc, board, possible_moves):
    """Uses check_area_move, but returns a list that does not contain Nonetypes"""

    elements = []

    for possible_move in possible_moves:
        elements.append(check_area_move(loc, board, possible_move[0], possible_move[1]))

    # Gets ride of Nonetypes
    elements = [element for element in elements if element is not None]

    return elements


class ChessPiece:

    def __init__(self, team, loc, screen, board_rect):
        self.team = team
        self.loc = loc
        self.screen = screen
        self.board_rect = board_rect
        self.number_of_moves = 0
        self.available_moves = []
        self.possible_moves = []
        self.image()
        self.Rect = self.image.get_rect()

    def available_movements(self, board):
        pass

    def image(self):
        pass

    def update(self):
        self.Rect.centerx = self.board_rect[self.loc[0]][self.loc[1]].loc[0]
        self.Rect.centery = self.board_rect[self.loc[0]][self.loc[1]].loc[1]

    def blitme(self):
        self.screen.blit(self.image, self.Rect)


class King(ChessPiece):

    def __init__(self, team, loc, screen, board_rect):
        super().__init__(team, loc, screen, board_rect)
        self.possible_moves = [(1, -1), (1, 0), (1, 1), (0, -1),
                               (0, 1), (-1, -1), (-1, 0), (-1, 1)]

    def available_movements(self, board):
        """Returns list of available movements in (x, y) form"""

        elements = []
        elements.extend(check_list_area(self.loc, board, self.possible_moves))
        self.available_moves = elements

    def image(self):
        if self.team == WHITE:
            self.image = gf.load_image('./textures/White_Bishop', '.png')
        elif self.team == BLACK:
            self.image = gf.load_image('./textures/Black_Bishop', '.png')


class Queen(ChessPiece):

    def __init__(self, team, loc, screen, board_rect):
        super().__init__(team, loc, screen, board_rect)
        self.possible_moves = [(1, 0), (0, 1), (-1, 0), (0, -1),
                               (1, 1), (1, -1), (-1, 1), (-1, -1)]
        self.possible_moves_2 = [(1, -1), (1, 0), (1, 1), (0, -1),
                               (0, 1), (-1, -1), (-1, 0), (-1, 1)]

    def available_movements(self, board):
        """Returns list of available movements in (x, y) form"""
        elements = []
        elements.extend(check_list_line(self.loc, board, self.possible_moves))
        elements.extend(check_list_area(self.loc, board, self.possible_moves_2))
        self.available_moves = elements

    def image(self):
        if self.team == WHITE:
            self.image = gf.load_image('./textures/White_Queen', '.png')
        elif self.team == BLACK:
            self.image = gf.load_image('./textures/Black_Queen', '.png')


class Rook(ChessPiece):

    def __init__(self, team, loc, screen, board_rect):
        super().__init__(team, loc, screen, board_rect)
        self.possible_moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def available_movements(self, board):
        """Returns list of available movements in (x, y) form"""
        elements = []
        elements.extend(check_list_line(self.loc, board, self.possible_moves))
        self.available_moves = elements

    def image(self):
        if self.team == WHITE:
            self.image = gf.load_image('./textures/White_Rook', '.png')
        elif self.team == BLACK:
            self.image = gf.load_image('./textures/Black_Rook', '.png')


class Bishop(ChessPiece):

    def __init__(self, team, loc, screen, board_rect):
        super().__init__(team, loc, screen, board_rect)
        self.possible_moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    def available_movements(self, board):
        """Returns list of available movements in (x, y) form"""
        elements = []
        elements.extend(check_list_line(self.loc, board, self.possible_moves))
        self.available_moves = elements

    def image(self):
        if self.team == WHITE:
            self.image = gf.load_image('./textures/White_Bishop', '.png')
        elif self.team == BLACK:
            self.image = gf.load_image('./textures/Black_Bishop', '.png')


class Knight(ChessPiece):

    def __init__(self, team, loc, screen, board_rect):
        super().__init__(team, loc, screen, board_rect)
        self.possible_moves = ((1, 2), (1, -2), (-1, 2), (-1, -2),
                               (2, 1), (2, -1), (-2, 1), (-2, -1))

    def available_movements(self, board):
        """Returns list of available movements in (x, y) form"""
        elements = []
        elements.extend(check_list_area(self.loc, board, self.possible_moves))
        self.available_moves = elements

    def image(self):
        if self.team == WHITE:
            self.image = gf.load_image('./textures/White_Knight', '.png')
        elif self.team == BLACK:
            self.image = gf.load_image('./textures/Black_Knight', '.png')


class Pawn(ChessPiece):

    def __init__(self, team, loc, screen, board_rect):
        super().__init__(team, loc, screen, board_rect)

    def available_movements(self, board):
        """Returns list of available movements in (x, y) form"""

        elements = []

        if self.number_of_moves == 0:
            if self.team == WHITE:
                elements.extend(check_line(self.loc, board, 1, 0, 2))
            if self.team == BLACK:
                elements.extend(check_line(self.loc, board, -1, 0, 2))
        else:
            if self.team == WHITE:
                if check_area((self.loc[0] + 1, self.loc[1] - 1), board) not in [-2, self.team]:
                    elements.append((self.loc[0] + 1, self.loc[1] - 1))
                if check_area((self.loc[0] + 1, self.loc[1] + 1), board) not in [-2, self.team]:
                    elements.append((self.loc[0] + 1, self.loc[1] + 1))
                if check_area((self.loc[0] + 1, self.loc[1]), board) not in [-2, self.team]:
                    elements.append((self.loc[0] + 1, self.loc[1]))
            if self.team == BLACK:
                if check_area((self.loc[0] - 1, self.loc[1] + 1), board) not in [-2, self.team]:
                    elements.append((self.loc[0] - 1, self.loc[1] + 1))
                if check_area((self.loc[0] - 1, self.loc[1]), board) not in [-2, self.team]:
                    elements.append((self.loc[0] - 1, self.loc[1]))
                if check_area((self.loc[0] - 1, self.loc[1] - 1), board) not in [-2, self.team]:
                    elements.append((self.loc[0] - 1, self.loc[1] - 1))

        self.available_moves = elements

    def image(self):
        if self.team == WHITE:
            self.image = gf.load_image('./textures/White_Pawn', '.png')
        elif self.team == BLACK:
            self.image = gf.load_image('./textures/Black_Pawn', '.png')
