# -*- coding: utf-8 -*-
from tile import Tile
from bag import Bag
import random


class Board(object):
    """Where the tiles live"""
    size = None
    cells = None

    def __init__(self, size):
        super(Board, self).__init__()

        #Set some params
        self.size = size

        #Seed the Board
        self.seed()

    def __repr__(self):
        strng = ""+str(self.bag)+"\n"
        for row in self.cells:
            vals = [x.__repr__() for x in row]
            strng += '\t'.join(vals)+'\n'
        return strng

    def shift(self, direction):
        new_tile_places = []
        any_merged = False

        if direction == 'left':
            for blob_i, blob_j, food_i, food_j in self.left_indices():
                moved, merged = self.move_cells(blob_i, blob_j, food_i, food_j)
                if moved or self.startup:
                    new_tile_places.append((self.size-1, blob_j))
                if merged:
                    any_merged = True

        elif direction == 'right':
            for blob_i, blob_j, food_i, food_j in self.right_indices():
                moved, merged = self.move_cells(blob_i, blob_j, food_i, food_j)
                if moved or self.startup:
                    new_tile_places.append((0, blob_j))
                if merged:
                    any_merged = True

        elif direction == 'down':
            for blob_i, blob_j, food_i, food_j in self.down_indices():
                moved, merged = self.move_cells(blob_i, blob_j, food_i, food_j)
                if moved or self.startup:
                    new_tile_places.append((blob_i, 0))
                if merged:
                    any_merged = True

        elif direction == 'up':
            for blob_i, blob_j, food_i, food_j in self.up_indices():
                moved, merged = self.move_cells(blob_i, blob_j, food_i, food_j)
                if moved or self.startup:
                    new_tile_places.append((blob_i, self.size-1))
                if merged:
                    any_merged = True

        else:
            raise Exception('What is this direction? {0}'.format(direction))
        if len(new_tile_places) > 0:
            x, y = random.choice(new_tile_places)
            self.cells[y][x] = Tile(self.bag.draw(self.max_val))

        return any_merged

    def left_indices(self):
        for i in range(0, self.size-1):
            for j in range(0, self.size):
                yield i, j, i+1, j

    def right_indices(self):
        for i in range(1, self.size)[::-1]:
            for j in range(0, self.size):
                yield i, j, i-1, j

    def up_indices(self):
        for j in range(0, self.size-1):
            for i in range(0, self.size):
                yield i, j, i, j+1

    def down_indices(self):
        for j in range(1, self.size)[::-1]:
            for i in range(0, self.size):
                yield i, j, i, j-1

    def move_cells(self, blob_i, blob_j, food_i, food_j):
        self.cells[blob_j][blob_i], \
            self.cells[food_j][food_i], \
            moved, merged = \
            self.cells[blob_j][blob_i].merge(self.cells[food_j][food_i])

        return moved, merged

    @property
    def max_val(self):
        max_tile = 0
        for row in self.cells:
            for t in row:
                if t.value > max_tile:
                    max_tile = t.value
        return max_tile

    def seed(self):
        self.bag = Bag()
        self.cells = [
            [Tile() for i in range(0, self.size)]
            for j in range(0, self.size)
        ]

        self.startup = True
        directions = ['up', 'down', 'left', 'right']
        any_merged = False
        for turn in range(0, 9):
            choice = random.choice(directions)
            merged = self.shift(choice)
            if merged:
                any_merged = True

        if any_merged:
            self.seed()
        else:
            self.startup = False
