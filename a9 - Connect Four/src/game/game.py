"""
game module
"""

from random import choice

from src.board.board import Board
from src.game.game_exception import GameWonException, TieException


class Game:
    def __init__(self):
        self._board = Board()

    def board(self):
        return self._board

    def human_move(self, row, col):
        """
        this function checks if the move made by user is valid and if yes it updates the board
        :param row: chosen row by the user
        :param col: chosen col by the user
        """
        if self._board.full_board():
            raise TieException("The board is full. It is a draw!")
        self._board.move('X', row, col)
        if self._board.check_for_winner('X'):
            raise GameWonException(" Congrats! You won.. ")

    def computer_move(self):
        """
        this function searches what are the valid positions left after the human move and if there's any way the
        computer can win it makes the winning move
        """
        # checking the draw case
        if self._board.full_board():
            raise TieException("The board is full. It is a draw!")
        # searching the valid left positions
        positions = []
        for row in range(6):
            for col in range(7):
                if self._board.get_chip(row, col) is None:
                    if self._board.check_the_gravity(row, col):
                        positions.append([row, col])

        #AI

        # checking for the computer winning move
        for pos in positions:
            self._board.board()[pos[0]][pos[1]] = '0'
            if self._board.check_for_winner('0'):
                raise GameWonException(" Computer won... ")
            else:
                self._board.board()[pos[0]][pos[1]] = ' '

        # checking for the human winning move
        found_winner_move = False
        for pos in positions:
            self._board.board()[pos[0]][pos[1]] = 'X'
            found_winner_move = True
            if not self._board.check_for_winner('X'):
                self._board.board()[pos[0]][pos[1]] = ' '
                found_winner_move = False
            else:
                self._board.board()[pos[0]][pos[1]] = '0'
                self._board.less_free_squares()
                break

        # if there's not the case for a winning, it chooses randomly the move
        if not found_winner_move:
            pos = choice(positions)
            self._board.move('0', pos[0], pos[1])

        return pos

