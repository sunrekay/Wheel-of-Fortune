import unittest
import console_output


class MyTestCase(unittest.TestCase):
    def test_show_welcome(self):
        self.assertEqual(console_output.show_welcome(), True)

    def test_show_question(self):
        self.assertEqual(console_output.show_question("Ювелиры часто говорят, что бриллиантам необходимо это."), True)
        self.assertEqual(console_output.show_question("Где-то однажды Явился на свет С лаем и мяуканьем Зверь, каких нет. Назовите зверя."), True)

    def test_show_answer(self):
        self.assertEqual(console_output.show_answer("котопес"), True)
        self.assertEqual(console_output.show_answer("одиночество"), True)

    def test_show_word(self):
        self.assertEqual(console_output.show_answer("котопес"), True)


if __name__ == '__main__':
    unittest.main()
