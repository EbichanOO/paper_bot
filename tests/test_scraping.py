import unittest
from scripts import scraping

class TestGoogleScholer(unittest.TestCase):
    def setUp(self) -> None:
        self.googleScholer = scraping.GoogleScholerScraping()

    def test_translate_one(self):
        self.assertEqual(self.googleScholer.translate('Hello'),'こんにちは')