import unittest

def factorial(x):
    if x == 1:
        return 1
    return x * factorial(x - 1)


class FactorialTest(unittest.TestCase):
    
    def test_basic_input(self):
        x = 1
        y = 1
        y_hat = factorial(x)
        self.assertEqual(y, y_hat)
        
        
    def test_basic_input2(self):
        x = 2
        y = 2
        y_hat = factorial(x)
        self.assertEqual(y, y_hat)
    
    
    def test_basic_input3(self):
        x = 3
        y = 6
        y_hat = factorial(x)
        self.assertEqual(y, y_hat)
    
    
if __name__ == '__main__':
    unittest.main()





