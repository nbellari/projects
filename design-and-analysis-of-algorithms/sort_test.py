import selection_sort
import bubble_sort
import unittest

class sort_test(unittest.TestCase):
    def test_sort_empty_list(self):
        list = []
        sort(list)
        self.assertEqual([], list)

    def test_sort_singleton(self):
        list = [1]
        sort(list)
        self.assertEqual([1], list)

    def test_sort_doubleton1(self):
        list = [10, 11]
        sort(list)
        self.assertEqual([10, 11], list)

    def test_sort_doubleton2(self):
        list = [-2, -3]
        sort(list)
        self.assertEqual([-3, -2], list)

    def test_sort_same_elems(self):
        list = [2, 2, 2, 2, 2]
        sort(list)
        self.assertEqual([2, 2, 2, 2, 2], list)

    def test_sort_sorted_elems(self):
        list = [1, 2, 3, 4, 5, 6, 7]
        sort(list)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7], list)

    def test_sort_reverse_sorted_elems(self):
        list = [6, 5, 4, 3, 2, 1]
        sort(list)
        self.assertEqual([1, 2, 3, 4, 5, 6], list)

    def test_sort_many_elems(self):
        list = [2, 48, 2, 59, 127, 10, -28, 26, 32]
        sort(list)
        self.assertEqual([-28, 2, 2, 10, 26, 32, 48, 59, 127], list)

if __name__ == "__main__":
    sort = bubble_sort.bubble_sort
    unittest.main()
