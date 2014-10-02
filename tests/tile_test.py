import unittest

from threes import Tile


class TileTest(unittest.TestCase):
    """Check that tiles work as expected"""

    def setUp(self):
        pass

    def test_tile_scoring(self):
        self.assertEqual(Tile().score(), 0)
        self.assertEqual(Tile(1).score(), 0)
        self.assertEqual(Tile(2).score(), 0)
        self.assertEqual(Tile(3).score(), 3)
        self.assertEqual(Tile(6).score(), 9)
        self.assertEqual(Tile(384).score(), 6561)
        self.assertEqual(Tile(6144).score(), 531441)

    def test_tile_merge(self):
        blob, food, moved, merged = Tile(3).merge(Tile())
        self.assertEqual(
            (blob.value, food.value, moved, merged),
            (Tile(3).value, Tile(0).value, False, False)
        )

        blob, food, moved, merged = Tile(1).merge(Tile(2))
        self.assertEqual(
            (blob.value, food.value, moved, merged),
            (Tile(3).value, Tile(0).value, True, True)
        )

        blob, food, moved, merged = Tile(2).merge(Tile(1))
        self.assertEqual(
            (blob.value, food.value, moved, merged),
            (Tile(3).value, Tile(0).value, True, True)
        )

        blob, food, moved, merged = Tile(3).merge(Tile(3))
        self.assertEqual(
            (blob.value, food.value, moved, merged),
            (Tile(6).value, Tile(0).value, True, True)
        )

        blob, food, moved, merged = Tile(0).merge(Tile(0))
        self.assertEqual(
            (blob.value, food.value, moved, merged),
            (Tile(0).value, Tile(0).value, False, False)
        )

        blob, food, moved, merged = Tile(0).merge(Tile(3))
        self.assertEqual(
            (blob.value, food.value, moved, merged),
            (Tile(3).value, Tile(0).value, True, False)
        )
