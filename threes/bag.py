from Queue import Queue
from random import choice


class Bag(object):
    """The things that holds the random tiles"""
    queue = None

    def __init__(self):
        super(Bag, self).__init__()
        self.queue = Queue()
        self.next = None
        self.pool = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
        self.has_plus = False

    def __repr__(self):
        next_display = self.next if self.next < 4 else '+'
        return "Next: {0}. {1} remain.".format(
            next_display,
            self.queue.qsize()
        )

    def draw(self, max_val):
        """ Takes the next value from the basic tile queue."""
        if self.queue.empty():
            self.shuffle(max_val)

        if self.next is None:
            value = self.queue.get_nowait()
        else:
            value = self.next

        self.next = self.queue.get()
        return value

    def shuffle(self, max_val):
        """ Re-fills the bag from the pool, stashing the numbers in a queue """
        sample_pool = list(self.pool)

        if max_val >= 48 and not self.has_plus:
            max_choice = max_val / 8
            max_exp = max_choice / 6
            plus_tile_options = [
                3*2**x for x in range(1, max_exp+1) if 3*2**x <= max_choice
            ]
            plus_tile = choice(plus_tile_options)
            sample_pool.append(plus_tile)
            self.has_plus = True

        if max_val >= 48 and self.has_plus:
            self.has_plus = False

        while sample_pool:
            tile = choice(sample_pool)
            self.queue.put_nowait(tile)
            del sample_pool[sample_pool.index(tile)]
