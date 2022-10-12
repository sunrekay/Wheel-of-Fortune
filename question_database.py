import json


def add_question(id, word, question):
    with open("questions.json", "r", encoding='utf-8') as f:
        try:
            data = json.loads(f.read())
        except:
            data={}
    f.close()
    questions = {
        id: {
            "word": word,
            "question": question
        }
    }
    data.update(questions)
    questions_json = json.dumps(data, indent=4)

    with open("questions.json", "w", encoding='utf-8') as my_file:
        my_file.write(questions_json)
    my_file.close()
    return True


def get_question(number_of_question):
    with open("questions.json", "r") as f:
        try:
            data = json.loads(f.read())
            f.close()
            return data[str(number_of_question)]
        except:
            f.close()
            return None

add_question("1", "котопес", "Где-то однажды Явился на свет С лаем и мяуканьем Зверь, каких нет. Назовите зверя.")
add_question("2", "разочаровываться", "Герцогиня Англии XVIII века Сара Черчилль говорила: «Вы молоды, если вы еще способны…»")
add_question("3", "одиночество", "Ювелиры часто говорят, что бриллиантам необходимо это.")