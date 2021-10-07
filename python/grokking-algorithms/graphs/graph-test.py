import unittest
from graph import Graph

class graph_test(unittest.TestCase):
    def test_graph_random1(self):
        # To test if graph has been formed properly
        g1 = Graph("""
            a->b
            a -> c
            a ->d[5 ]
            b-> d[6]
            c->d[ 7]
            """)
        self.assertEqual(['b', 'c', 'd'], g1.graph['a'])
        self.assertEqual(['d'], g1.graph['b'])
        self.assertEqual(['d'], g1.graph['c'])
        self.assertEqual([0], g1.weights[('a', 'b')])
        self.assertEqual([0], g1.weights[('a', 'c')])
        self.assertEqual([5], g1.weights[('a', 'd')])
        self.assertEqual([6], g1.weights[('b', 'd')])
        self.assertEqual([7], g1.weights[('c', 'd')])

    def test_graph_multiedge(self):
        # two nodes with multiple edges
        g1 = Graph("""
            a->b
            a->b[10]
            a->b[11]
            a->b[12]
            """)
        self.assertEqual(['b'], g1.graph['a'])
        self.assertEqual([0, 10, 11, 12], g1.weights[('a', 'b')])

        # delete one edge
        g1.del_edge('a', 'b', 10)
        self.assertEqual(['b'], g1.graph['a'])
        self.assertEqual([0, 11, 12], g1.weights[('a', 'b')])

        # add one edge
        g1.add_edge('a', 'b', 19)
        self.assertEqual(['b'], g1.graph['a'])
        self.assertEqual([0, 11, 12, 19], g1.weights[('a', 'b')])

    def test_graph_multiedge_loop(self):
        # single node with multiple edges to itself
        g1 = Graph("""
            a->a
            a->a[10]
            a->a[11]
            a->a[12]
            """)
        self.assertEqual(['a'], g1.graph['a'])
        self.assertEqual([0, 10, 11, 12], g1.weights[('a', 'a')])

        # delete one edge
        g1.del_edge('a', 'a', 10)
        self.assertEqual(['a'], g1.graph['a'])
        self.assertEqual([0, 11, 12], g1.weights[('a', 'a')])

        # add one edge
        g1.add_edge('a', 'a', 19)
        self.assertEqual(['a'], g1.graph['a'])
        self.assertEqual([0, 11, 12, 19], g1.weights[('a', 'a')])

if __name__ == "__main__":
    unittest.main()