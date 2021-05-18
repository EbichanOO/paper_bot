import unittest
from scripts.scraping import GoogleScholerScraping

class TestGoogleScholer(unittest.TestCase):
    def setUp(self) -> None:
        self.googleScholer = GoogleScholerScraping()

    def test_translate_one(self):
        self.assertEqual(self.googleScholer.translate("Hello"),'こんにちは')