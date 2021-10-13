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

class test_binary(unittest.TestCase):
    def test_binary_empty(self):
        list = []
        result = recurse.binary_search(list, 1)
        self.assertEqual(None, result)
    
    def test_binary_one_present(self):
        list = [1]
        result = recurse.binary_search(list, 1)
        self.assertEqual(0, result)

    def test_binary_one_absent(self):
        list = [1]
        result = recurse.binary_search(list, 2)
        self.assertEqual(None, result)

    def test_binary_two_present1(self):
        list = [10, 20]
        result = recurse.binary_search(list, 10)
        self.assertEqual(0, result)

    def test_binary_two_present2(self):
        list = [11, 33]
        result = recurse.binary_search(list, 33)
        self.assertEqual(1, result)

    def test_binary_two_absent(self):
        list = [10, 34]
        result = recurse.binary_search(list, 22)
        self.assertEqual(None, result)

    def test_binary_many_none(self):
        list = [1, 2, 3, 4, 5, 6]
        result = recurse.binary_search(list, 9)
        self.assertEqual(None, result)

    def test_binary_many_present(self):
        list = [-10, -4, -1, 0, 4, 12, 56, 98]
        result = recurse.binary_search(list, -1)
        self.assertEqual(2, result)

if __name__ == "__main__":
    unittest.main()