import unittest
import bfs
from ds.graph import Graph



class breadth_first_test(unittest.TestCase):
    def test_bfs_single_hop(self):
        g1 = Graph("""
            a -> b
            b -> c
            a -> d
            e -> d
            """)

        result = bfs.breadth_first_search(g1, "b", "c")
        self.assertEqual(result, True)

        result = bfs.breadth_first_search(g1, "a", "e")
        self.assertEqual(result, False)


    def test_bfs_multiple_hop(self):
        g1 = Graph("""
            a -> b
            b -> c
            a -> e
            e -> f
            g -> h
            b -> g
            c -> h
            i -> h
            """)

        result = bfs.breadth_first_search(g1, "a", "h")
        self.assertEqual(result, True)

        result = bfs.breadth_first_search(g1, "a", "f")
        self.assertEqual(result, True)

        result = bfs.breadth_first_search(g1, "a", "f")
        self.assertEqual(result, True)

        result = bfs.breadth_first_search(g1, "a", "i")
        self.assertEqual(result, False)

if __name__ == "__main__":
    unittest.main()
