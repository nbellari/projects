import selection_sort
import unittest

class ssort_tester(unittest.TestCase):
    def test_ssort_empty_list(self):
        list = []
        selection_sort.ssort(list)
        self.assertEqual([], list)

    def test_ssort_singleton(self):
        list = [1]
        selection_sort.ssort(list)
        self.assertEqual([1], list)

    def test_ssort_doubleton(self):
        list = [10, 2]
        selection_sort.ssort(list)
        self.assertEqual([2, 10], list)
    
    def test_ssort_multiple(self):
        list = [10, -2, 40, 12, 43, 19]
        selection_sort.ssort(list)
        self.assertEqual([-2, 10, 12, 19, 40, 43], list)

if __name__ == "__main__":
    unittest.main()