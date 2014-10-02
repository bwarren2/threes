from board import Board
from tile import Tile
from unittest import TestCase


class TestBoard(TestCase):

    def setUp(self):
        self.board = Board(4)

    def test_left_shift(self):
        self.flush_board()
        self.board.shift('left')
        self.assertEqual(self.board.cells[0][0].value, 1)
        self.assertEqual(self.board.cells[1][0].value, 1)
        self.assertEqual(self.board.cells[2][1].value, 1)
        self.assertEqual(self.board.cells[3][2].value, 1)

    def test_down_shift(self):
        self.flush_board()
        self.board.shift('down')
        self.assertEqual(self.board.cells[3][3].value, 1)
        self.assertEqual(self.board.cells[3][2].value, 1)
        self.assertEqual(self.board.cells[2][1].value, 1)
        self.assertEqual(self.board.cells[1][0].value, 1)

    def test_up_shift(self):
        self.flush_board()
        self.board.shift('up')
        self.assertEqual(self.board.cells[0][0].value, 1)
        self.assertEqual(self.board.cells[0][1].value, 1)
        self.assertEqual(self.board.cells[1][2].value, 1)
        self.assertEqual(self.board.cells[2][3].value, 1)

    def test_right_shift(self):
        self.flush_board()
        self.board.shift('right')
        self.assertEqual(self.board.cells[3][3].value, 1)
        self.assertEqual(self.board.cells[2][3].value, 1)
        self.assertEqual(self.board.cells[1][2].value, 1)
        self.assertEqual(self.board.cells[0][1].value, 1)

    def flush_board(self):
        for row_key in range(len(self.board.cells)):
            for col_key in range(len(self.board.cells[row_key])):
                self.board.cells[row_key][col_key] = Tile()
        for i in range(0, 4):
            self.board.cells[i][i] = Tile(1)
