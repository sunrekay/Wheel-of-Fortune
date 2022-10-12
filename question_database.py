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
