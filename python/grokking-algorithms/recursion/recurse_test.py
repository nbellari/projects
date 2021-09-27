import recurse
import unittest

class sum_test(unittest.TestCase):
    def test_sum_empty(self):
        list = []
        sum = recurse.sum_recurse(list)
        self.assertEqual(0, sum)

    def test_sum_singleton(self):
        list = [18]
        sum = recurse.sum_recurse(list)
        self.assertEqual(18, sum)

    def test_sum_doubleton(self):
        list = [10, 24]
        sum = recurse.sum_recurse(list)
        self.assertEqual(34, sum)
    
    def test_sum_multiple(self):
        list = [10, -54, 24, 10, 19]
        sum = recurse.sum_recurse(list)
        self.assertEqual(9, sum)

class count_test(unittest.TestCase):
    def test_count_empty(self):
        list = []
        count = recurse.count_recurse(list)
        self.assertEqual(0, count)

    def test_count_singleton(self):
        list = [2]
        count = recurse.count_recurse(list)
        self.assertEqual(1, count)

    def test_count_doubleton(self):
        list = [1,3]
        count = recurse.count_recurse(list)
        self.assertEqual(2, count)
    
    def test_count_multiple(self):
        list = [12, 3, 212, 6, -2, 12]
        count = recurse.count_recurse(list)
        self.assertEqual(6, count)

class max_test(unittest.TestCase):
    def test_max_empty(self):
        list = []
        self.assertRaises(AssertionError, recurse.max_recurse, list)

    def test_max_singleton(self):
        list = [1]
        max = recurse.max_recurse(list)
        self.assertEqual(1, max)
    
    def test_max_doubleton(self):
        list = [20, 45]
        max = recurse.max_recurse(list)
        self.assertEqual(45, max)

    def test_max_multiple(self):
        list = [23, 82, -10]
        max = recurse.max_recurse(list)
        self.assertEqual(82, max)

    def test_max_negatives(self):
        list = [-12, -34, -18, -127, -38]
        max = recurse.max_recurse(list)
        self.assertEqual(-12, max)

if __name__ == "__main__":
    unittest.main()