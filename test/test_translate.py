import unittest
from unittest.mock import patch

from ovos_google_translate_plugin import GoogleTranslatePlugin


class TestGoogleTranslatePlugin(unittest.TestCase):

    @patch("ovos_google_translate_plugin.google_tx")
    def test_translate_auto_source(self, mock_tx):
        # shape returned by the endpoint when source is "auto"/omitted
        mock_tx.return_value = [["meu nome e Casimiro", "en"]]
        plugin = GoogleTranslatePlugin()
        result = plugin.translate("my name is Casimiro", target="pt", source="auto")
        self.assertEqual(result, "meu nome e Casimiro")

    @patch("ovos_google_translate_plugin.google_tx")
    def test_translate_explicit_source(self, mock_tx):
        # shape returned by the endpoint when an explicit source is passed
        mock_tx.return_value = ["meu nome e Casimiro"]
        plugin = GoogleTranslatePlugin()
        result = plugin.translate("my name is Casimiro", target="pt", source="en")
        self.assertEqual(result, "meu nome e Casimiro")
        # regression guard: must not be just the first character
        self.assertNotEqual(result, "m")


if __name__ == "__main__":
    unittest.main()
