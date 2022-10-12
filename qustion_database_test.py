import unittest
import question_database


class MyTestCase(unittest.TestCase):
    def test_get_question(self):
        self.assertEqual(question_database.get_question(1), {"word": "котопес",
                                                             "question": "Где-то однажды Явился на свет С лаем и мяуканьем Зверь, каких нет. Назовите зверя."})

        self.assertEqual(question_database.get_question(2), {"word": "разочаровываться",
                                                             "question": "Герцогиня Англии XVIII века Сара Черчилль говорила: «Вы молоды, если вы еще способны…»"})

        self.assertEqual(question_database.get_question(3), {"word": "одиночество.",
                                                             "question": "Ювелиры часто говорят, что бриллиантам необходимо это."})


if __name__ == '__main__':
    unittest.main()
