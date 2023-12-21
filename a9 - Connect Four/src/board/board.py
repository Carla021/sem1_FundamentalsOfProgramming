"""
board module
"""
from texttable import Texttable

from src.board.board_exception import BoardException


class Board:
    def __init__(self):
        """
        Create the game board
        :return: the board
        """
        self._board = []
        self._rows = 6
        self._cols = 7
        self._free_squares = 42

        for x in range(self._rows):
            self._board.append([' ', ' ', ' ', ' ', ' ', ' ', ' '])

    def board(self):
        return self._board

    def rows(self):
        return self._rows

    def cols(self):
        return self._cols

    def free_squares(self):
        return self._free_squares

    def less_free_squares(self):
        # decrements the free squares after a move
        self._free_squares -= 1
        return self._free_squares

    def get_chip(self, row, col):
        # gets the chip on the given position
        chip = self._board[row][col]
        if chip == ' ':
            return None
        return chip

    def isSpaceTaken(self, row, col):
        # checks if the given space is free
        if self.get_chip(row, col) is not None:
            return True
        return False

    def check_the_gravity(self, row, col):
        # we calculate the space below

        spaceBelow = [None] * 2
        spaceBelow[0] = row + 1
        spaceBelow[1] = col

        if spaceBelow[0] == 6:
            return True

        if self.get_chip(spaceBelow[0], spaceBelow[1]) is not None:
            return True

        return False

    def move(self, chip, row, col):
        # the chip is placed on the given position only if it respects all the conditions

        if row not in [0, 1, 2, 3, 4, 5] or col not in [0, 1, 2, 3, 4, 5, 6]:
            raise BoardException("Move outside the board!")
        if chip not in ['X', '0', ' ']:
            raise BoardException("Invalid chip!")
        if self.get_chip(row, col) is not None:
            raise BoardException("Space already taken!")
        if self.check_the_gravity(row, col) == False:
            raise BoardException("Impossible move!")

        self._board[row][col] = chip
        self._free_squares -= 1

    def full_board(self):
        # checks if the board is full for a possible tie
        return self._free_squares == 0

    def check_for_winner(self, chip):
        # checks the spaces in search for a winner
        gb = self._board

        # check for horizontal spaces
        for x in range(self._rows):
            for y in range(self._cols - 3):
                if gb[x][y] == chip and gb[x][y + 1] == chip and gb[x][y + 2] == chip and gb[x][y + 3] == chip:
                    return True

        # check for vertical spaces
        for y in range(self._cols):
            for x in range(self._rows - 3):
                if gb[x][y] == chip and gb[x + 1][y] == chip and gb[x + 2][y] == chip and gb[x + 3][y] == chip:
                    return True

        # check for diagonal spaces (top-left <-> bottom-right)
        for x in range(self._rows - 3):
            for y in range(self._cols - 3):
                if gb[x][y] == chip and gb[x + 1][y + 1] == chip and gb[x + 2][y + 2] == chip and gb[x + 3][
                    y + 3] == chip:
                    return True

        # check for diagonal spaces (top-right <-> bottom-left)
        for x in range(self._rows - 3):
            for y in range(3, self._cols):
                if gb[x][y] == chip and gb[x + 1][y - 1] == chip and gb[x + 2][y - 2] == chip and gb[x + 3][
                    y - 3] == chip:
                    return True

        return False

    def create_board_as_string(self):
        # this function creates the representation of the board

        '''
        result = ""
        gb = self._board

        result += "\n    A   B   C   D   E   F   G  "
        result += "\n  +---+---+---+---+---+---+---+\n"

        for row in range(self._rows):
            result += str(row) + " | "
            for col in range(self._cols):
                if gb[row][col] == "X" or gb[row][col] == "0":
                    result += str(gb[row][col]) + " | "
                else:
                    result += "  | "
            result += "\n  +---+---+---+---+---+---+---+\n"

        return result
        '''

        t = Texttable()

        header = []
        for i in range(self._cols):
            header.append(chr(ord('A') + i))
        t.header(['/'] + header)

        for i in range(self._rows):
            rows = []
            for j in range(self._cols):
                if self._board[i][j] == 'X':
                    rows.append('X')
                elif self._board[i][j] == '0':
                    rows.append('0')
                else:
                    rows.append(' ')
            t.add_row([str(i)] + rows)

        return t.draw()
