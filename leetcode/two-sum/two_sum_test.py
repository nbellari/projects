import unittest
import two_sum_simple
import two_sum

class TwoSumTest(unittest.TestCase):
    def test_two_sum_size_one(self):
        list = [1]
        target = 1
        result = testFunc(list, target)
        self.assertEqual([-1, 1], result)

    def test_two_sum_size_two_absent(self):
        list = [1,2]
        target = 43
        result = testFunc(list, target)
        self.assertEqual([-1, -1], result)

    def test_two_sum_size_two_present(self):
        list = [2, 4]
        target = 6
        result = testFunc(list, target)
        self.assertEqual([0, 1], result)

    def test_two_sum_many_present1(self):
        list = [3, 7, 10, 19, 11]
        target = 21
        result = testFunc(list, target)
        self.assertEqual([2, 4], result)

    def test_two_sum_many_present2(self):
        list = [10, 238, 12, 49, 12, 19]
        target = 250
        result = testFunc(list, target)
        self.assertEqual([1, 2], result)

    def test_two_sum_many_absent1(self):
        list = [10, 23, 18, 37, 29]
        target = 100
        result = testFunc(list, target)
        self.assertEqual([-1, -1], result)

if __name__ == "__main__":
    testFunc = two_sum_simple.twoSum
    unittest.main()
