from threes import Bag
import unittest


class BagTest(unittest.TestCase):
    """Check that the bag works as expected"""

    def setUp(self):
        self.bag = Bag()

    def test_bag_pool(self):
        self.assertEqual(
            self.bag.pool, [x for x in range(1, 4) for i in range(0, 4)]
        )

    def test_bag_shuffle(self):
        self.bag.shuffle()
        test = []
        while not self.bag.queue.empty():
            test.append(self.bag.queue.get_nowait())
        test.sort()
        self.bag.pool.sort()
        self.assertEqual(test, self.bag.pool)
