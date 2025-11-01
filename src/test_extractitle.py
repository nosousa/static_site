import unittest
from extracttitle import extract_title

class TestExtract(unittest.TestCase):
    def test_extracttitle(self):
        s = "# Hello"
        self.assertEqual(extract_title(s), "Hello")

        s = "# \n\n paragraph intro\n\n# Title Here\n\n titlenot here"
        self.assertEqual(extract_title(s), "Title Here")


if __name__ == "__main__":
    unittest.main()