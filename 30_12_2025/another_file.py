import unittest
from test_math import TestMath

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMath)
    unittest.TextTestRunner().run(suite)
    
