## For running python with test cases
## $ python3 -m unittest linear-search.py


import unittest

def linear_search(l, target):
    for i in l:
        if i == target:
            return l.index(i)
    return "Not Found...!"


class TestClass(unittest.TestCase):
    def test_linear_search(self):
        l = [[2,3,1,4], [5,3,62,2,5,4], [2,63,3,6,2,4]]
        for i in l:
            target = 4
            self.assertEqual(linear_search(i, 4), i.index(target)) 

