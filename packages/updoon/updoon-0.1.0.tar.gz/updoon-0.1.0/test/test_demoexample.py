import unittest
import numpy.testing as npt
import numpy as np
#import updoon as ud 

# test cases
class Test_Demo_Example(unittest.TestCase):
    def test1(self):
        self.assertEqual(123, 123)

    def test2(self):
        self.assertEqual(456, 456)

# run
if __name__ == '__main__':
    unittest.main()



