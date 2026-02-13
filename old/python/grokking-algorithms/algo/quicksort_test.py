import quicksort
import unittest

from quicksort import qsort2 as qsort

class qsort_test(unittest.TestCase):
    def test_qsort_empty_list(self):
        list = []
        sorted_list = qsort(list)
        self.assertEqual([], sorted_list)

    def test_qsort_singleton(self):
        list = [1]
        sorted_list = qsort(list)
        self.assertEqual([1], sorted_list)

    def test_qsort_doubleton1(self):
        list = [10, 11]
        sorted_list = qsort(list)
        self.assertEqual([10, 11], sorted_list)

    def test_qsort_doubleton2(self):
        list = [-2, -3]
        sorted_list = qsort(list)
        self.assertEqual([-3, -2], sorted_list)
    
    def test_qsort_same_elems(self):
        list = [2, 2, 2, 2, 2]
        sorted_list = qsort(list)
        self.assertEqual([2, 2, 2, 2, 2], sorted_list)

    def test_qsort_sorted_elems(self):
        list = [1, 2, 3, 4, 5, 6, 7]
        sorted_list = qsort(list)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7], sorted_list)

    def test_qsort_reverse_sorted_elems(self):
        list = [6, 5, 4, 3, 2, 1]
        sorted_list = qsort(list)
        self.assertEqual([1, 2, 3, 4, 5, 6], sorted_list)

    def test_qsort_many_elems(self):
        list = [2, 48, 2, 59, 127, 10, -28, 26, 32]
        sorted_list = qsort(list)
        self.assertEqual([-28, 2, 2, 10, 26, 32, 48, 59, 127], sorted_list)

if __name__ == "__main__":
    unittest.main()