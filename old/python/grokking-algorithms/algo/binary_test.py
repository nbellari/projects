import unittest
import binary_search

class test_binary(unittest.TestCase):
    def test_binary_empty(self):
        list = []
        result = binary_search.binary_search(list, 1)
        self.assertEqual(None, result)
    
    def test_binary_one_present(self):
        list = [1]
        result = binary_search.binary_search(list, 1)
        self.assertEqual(0, result)

    def test_binary_one_absent(self):
        list = [1]
        result = binary_search.binary_search(list, 2)
        self.assertEqual(None, result)

    def test_binary_two_present1(self):
        list = [10, 20]
        result = binary_search.binary_search(list, 10)
        self.assertEqual(0, result)

    def test_binary_two_present2(self):
        list = [11, 33]
        result = binary_search.binary_search(list, 33)
        self.assertEqual(1, result)

    def test_binary_two_absent(self):
        list = [10, 34]
        result = binary_search.binary_search(list, 22)
        self.assertEqual(None, result)

    def test_binary_many_none(self):
        list = [1, 2, 3, 4, 5, 6]
        result = binary_search.binary_search(list, 9)
        self.assertEqual(None, result)

    def test_binary_many_present(self):
        list = [-10, -4, -1, 0, 4, 12, 56, 98]
        result = binary_search.binary_search(list, -1)
        self.assertEqual(2, result)


if __name__ == "__main__":
    unittest.main()