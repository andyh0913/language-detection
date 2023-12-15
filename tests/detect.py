#!/usr/bin/env python
import unittest
from langdetect import detect

class TestLanguageDetection(unittest.TestCase):
    def test_normal_detection(self):
        text = "Hello, world! 我喜歡 Coding。"
        result = detect(text)
        self.assertEqual(result, {'zh': 3, 'en': 3})  # Update expected result as needed

    def test_skip_special_word(self):
        text = "Hello, world! 我們的 DNA 是雙螺旋結構。" # DNA is an special word, that will passthought.
        result = detect(text)
        self.assertEqual(result, {'zh': 9, 'en': 2})  # Update expected result as needed

if __name__ == '__main__':
    unittest.main()