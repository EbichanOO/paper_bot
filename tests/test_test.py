import unittest
from scripts import test
# all run tests  python -m unittest discover tests
class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(10, test.calc(6, 4))