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

    def __repr__(self):
        return "Next: {0}. {1} remain.".format(self.next, self.queue.qsize())

    def draw(self, max_val):
        """ Takes the next value from the basic tile queue."""
        if self.queue.empty():
            self.shuffle()

        if self.next is None:
            value = self.queue.get_nowait()
        else:
            value = self.next

        self.next = self.queue.get()
        return value

    def shuffle(self):
        """ Re-fills the bag from the pool, stashing the numbers in a queue """
        sample_pool = list(self.pool)

        while sample_pool:
            tile = choice(sample_pool)
            self.queue.put_nowait(tile)
            del sample_pool[sample_pool.index(tile)]
