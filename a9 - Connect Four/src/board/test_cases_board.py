import unittest

from src.board.board import Board


class board_tests(unittest.TestCase):

    def setUp(self) -> None:
        print("set up")
        self._board = Board()

    def tearDown(self) -> None:
        print("tear down")

    '''
    def test_move(self):
        print("test")
        self._board.move('X', 5, 1)
        self.assertEqual(self._board[5][1], 'X')
    '''

    def test_move_and_is_space_taken(self):
        print("test")
        self._board.move('X', 5, 3)
        self.assertTrue(self._board.isSpaceTaken(5, 3))

    def test_check_the_gravity(self):
        print("test")
        self.assertFalse(self._board.check_the_gravity(1, 3))

    def test_check_for_winner(self):
        print("test")
        self._board.move('X', 5, 0)
        self._board.move('X', 5, 1)
        self._board.move('X', 5, 2)
        self._board.move('X', 5, 3)
        self.assertTrue(self._board.check_for_winner('X'))

    def test_fullBoard(self):
        print("test")
        self.assertFalse(self._board.full_board())