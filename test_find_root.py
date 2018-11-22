import unittest
from find_root import bisect

def f(x):
    return x ** 2 - 4


class TestFindRoot(unittest.TestCase):
    
    def test_simple(self):
        root1 = bisect(f, -1.1, 23.5)
        print(root1)
        self.assertAlmostEqual(root1, 2)
        
    
    
if __name__ == '__main__':
    unittest.main()