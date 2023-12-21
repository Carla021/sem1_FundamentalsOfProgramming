import unittest
from src.game.game import Game


class Test(unittest.TestCase):

    def setUp(self) -> None:
        print("set up")
        self._game = Game()

    def tearDown(self) -> None:
        print("tear down")

    def test_human_move(self):
        print("test")
        self._game.human_move(5, 1)
        self.assertTrue(self._game.board().get_chip(5, 1) == 'X')

    def test_computer_move(self):
        print("test")
        self._game.computer_move()
        self.assertTrue(self._game.board().free_squares() == 41)

    def test_ai(self):
        print("test")
        self._game.human_move(5, 1)
        self._game.human_move(5, 3)
        self._game.human_move(5, 4)
        self._game.computer_move()
        self.assertTrue(self._game.board().get_chip(5, 2) == '0')


