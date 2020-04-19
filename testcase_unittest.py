import unittest
from celery_chain import add, mul

class Testdef(unittest.TestCase):
    # Setting up for the test
    def setUp(self):
        pass

    # Cleaning up after the test
    def tearDown(self):
        pass

    def test_def_add(self):
        self.assertEqual(add(3,4), 7)

    def test_def_mul(self):
        self.assertEqual(mul(4,5), 20)
    
if __name__ == '__main__':
    unittest.main()

