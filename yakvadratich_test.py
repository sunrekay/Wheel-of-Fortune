import unittest
import yakvadratich


class MyTestCase(unittest.TestCase):
    def add_word_test(self):
        self.assertEqual(yakvadratich.add_word('о', 'одиночество'),
                         ["О", "_", "_", "_", "О", "_", "_", "_", "_", "_", "О"])
        self.assertEqual(yakvadratich.add_word('д', 'одиночество'),
                         ["_", "Д", "_", "_", "_", "_", "_", "_", "_", "_", "_"])

        self.assertEqual(yakvadratich.add_word('д', 'котопес'),
                         ["_", "_", "_", "_", "_", "_", "_"])
        self.assertEqual(yakvadratich.add_word('о', 'котопес'),
                         ["_", "О", "_", "О", "_", "_", "_"])
