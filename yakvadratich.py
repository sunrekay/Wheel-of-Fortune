import random

import question_database
import console_output
import os
import time

WORD_LIST = []


def add_word(symbol, word):
    global WORD_LIST
    for i in range(len(word)):
        if symbol.lower() == word[i].lower():
            WORD_LIST[i] = symbol.upper()
    return WORD_LIST


def show_info():
    os.system('cls')
    console_output.show_welcome()
    console_output.show_question(question)
    console_output.show_word("".join(WORD_LIST))


if __name__ == "__main__":
    console_output.show_welcome()
    start = console_output.start_menu()

    question_id = random.randint(1, 3)
    question_dict = question_database.get_question(question_id)

    question = question_dict['question']
    answer = question_dict['word']

    WORD_LIST = ["_"] * len(answer)

    while start == "1":

        if "_" not in WORD_LIST:
            console_output.end_menu()
            break

        show_info()
        choose = console_output.show_menu()
        show_info()

        if choose == "1":

            symbol = str(input("БУКВА: "))
            if symbol in answer:
                print("""
    ЕСТЬ ТАКАЯ БУКВА!
                """)
                add_word(symbol, answer)
            else:
                print("""
    ТАКОЙ БУКВЫ НЕТ!
                """)
            time.sleep(2)

        elif choose == "2":

            word = str(input("СЛОВО: "))
            if word.lower() == answer.lower():
                console_output.end_menu()
                start = console_output.start_menu()

            print("""
    УВЫ, ЭТО НЕ ТО СЛОВО.
            """)
            time.sleep(2)

        elif choose == "3":
            print("""
    НУ ПОКА!
            """)
            time.sleep(2)
            os.system('cls')
            break

        else:
            print("""
    Я НЕ ПОНИМАЮ!
            """)
            time.sleep(2)
            os.system('cls')

    if start == "2":
        print("НУ ПОКА!")
        time.sleep(2)
        os.system('cls')