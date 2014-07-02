# -*- coding: utf-8 -*-
from math import log


class Tile(object):
    """An element that sits on a board and merges with other tiles"""
    def __init__(self, value=0):
        super(Tile, self).__init__()
        self.value = value

    def __repr__(self):
        return "{0} tile".format(self.value)

    def score(self):
        if self.value < 3:
            return 0
        else:
            exp = log(self.value/3, 2)
            return 3**(exp + 1)

    def merge(self, tile):
        """ Returns two tiles, one for the slot this tile is in and one for the slot this tile is absorbing, and whether a nonzero tile moved.  """

        if self.value == 0:
            return Tile(tile.value), Tile(), tile.value != 0

        elif self.value == 1:
            if tile.value == 2:
                return Tile(3), Tile(), True
            else:
                return Tile(self.value), Tile(tile.value), False

        elif self.value == 2:
            if tile.value == 1:
                return Tile(3), Tile(), True
            else:
                return Tile(self.value), Tile(tile.value), False

        else:
            if self.value == tile.value:
                return Tile(self.value*2), Tile(), True
            else:
                return Tile(self.value), Tile(tile.value), False
