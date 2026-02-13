import unittest
from rlist import rIntList

class rIntListTest(unittest.TestCase):
    def test_empty_rlist(self):
        elist = rIntList(0)
        self.assertEqual(elist, [])

    def test_singleton_rlist(self):
        slist = rIntList(1)
        self.assertEqual(len(slist), 1)

    def test_doubleton_rlist(self):
        dlist = rIntList(2)
        self.assertEqual(len(dlist), 2)

    def test_no_negative_rlist(self):
        no_list = rIntList(10, 500)
        self.assertEqual(False, any([x for x in no_list if x < 0]))
    
    def test_negative_rlist(self):
        neg_list = rIntList(10, 500, negatives=True)
        self.assertEqual(True, any([x for x in neg_list if x < 0]))

    def test_bound_rlist(self):
        b_list = rIntList(20, 400)
        self.assertEqual(False, any([x for x in b_list if x > 400 or x < 0]))

if __name__ == "__main__":
    unittest.main()
