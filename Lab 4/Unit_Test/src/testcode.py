import unittest
from mycode import double

class TestDouble(unittest.TestCase):
    def testdouble(self):
        self.assertEqual(double(2), 4)  
        self.assertEqual(double(4), 8)    
        self.assertEqual(double(0), 0)     
        self.assertEqual(double(-2), -4)    

if __name__ == "__main__":
    unittest.main()