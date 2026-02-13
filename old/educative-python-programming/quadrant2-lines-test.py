import quadrant2_lines
import unittest

class q2_line_test(unittest.TestCase):
    def test_empty_q2_line_set(self):
        lines = [(1, (2, 3), (3, 4)), (2, (0, -1), (-3, 4)), (3, (-3, 4), (4, -4))]
        result = quadrant2_lines.filter_line_segments(lines)
        self.assertEqual(result, None)

    def test_q2_line_on_axis(self):
        # Case where a point of the line segment is on the y-axis (i.e x is zero)
        lines = [(1, (2, 3), (3, 4)), (2, (0, 1), (-3, 4)), (3, (-3, 4), (-4, 4))]
        result = quadrant2_lines.filter_line_segments(lines)
        self.assertEqual(result, [2, 3])

    def test_singleton_q2_line_set(self):
        lines = [(1, (2, 3), (3, 4)), (2, (0, -1), (-3, 4)), (3, (-3, 4), (-4, 4))]
        result = quadrant2_lines.filter_line_segments(lines)
        self.assertEqual(result, [3])

    def test_multiple_q1_line_set(self):
        lines = [(1, (-2, 3), (-3, 4)), (2, (-2, 0), (-3, 6)), (3, (-3, 4), (-4, 4))]
        result = quadrant2_lines.filter_line_segments(lines)
        self.assertEqual(result, [1,2,3])

    def test_multiple_q1_line_set2(self):
        lines = [(1, (0, 3), (0, 4)), (2, (-2, 0), (-3, 0)), (3, (0, 0), (-4, 4))]
        result = quadrant2_lines.filter_line_segments(lines)
        self.assertEqual(result, [3])

if __name__ == "__main__":
    unittest.main()
