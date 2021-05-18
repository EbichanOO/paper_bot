import unittest
import test
class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(11, test.calc(6, 4))