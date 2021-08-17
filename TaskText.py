from random import random, choice
from TextObject import TextObject


class TaskText:
    def __init__(self, file_path, words_need):
        self.file_path = file_path
        self.words_need = words_need
        self.errortext = ''

    def extract_words(self, file_text_path):
        words = []
        ws = open(file_text_path, "r")
        while True:
            w = ws.readline()
            if not w:
                break
            else:
                words.append(w.strip())
        ws.close()
        return words

    def create_text_list(self):
        words = self.extract_words(self.file_path)
        word_list = []
        word_list.append("Press SPACE if you're ready")

        all_words = 0
        all_len = 0
        Ns = 0
        while all_words < self.words_need:
            all_words += 1
            one_word = choice(words)
            print(one_word)
            all_len += len(one_word)
            if random() > 0:
                one_word.upper()
            word_list.append(one_word)
            Ns += 1
        self.average_word_len = round((all_len / all_words), 1)
        return word_list

        # Если нажатая клавиша была правильной
    def on_key_right(self, textobj, pressed, key):
        new_txt = (len(textobj.get_text()[:key]) + 1) * ' ' + pressed + ' ' * (len(textobj.get_text()) - key)
        new_text = TextObject(textobj.get_pos()[0], textobj.get_pos()[1],
                              new_txt, 'green', 'Courier', 70)
        return new_text

        # Если нажатая клавиша была неправильной
    def on_key_wrong(self, textobj, pressed, key):
        self.errortext += pressed
        new_txt = len(textobj.get_text()[:key]) * ' ' + len(self.errortext) * ' ' + self.errortext + \
                  len(textobj.get_text()[key:]) * ' '
        new_text = TextObject(textobj.get_pos()[0], -15,
                              new_txt, 'red', 'Courier', 70)
        return new_text

        # Удаление текста ошибки
    def delete_error_message(self, textobj, key):
        self.errortext = self.errortext[:-1]
        new_txt = len(textobj.get_text()[:key]) * ' ' + len(self.errortext) * ' ' + self.errortext + \
                  len(textobj.get_text()[key:]) * ' '
        new_text = TextObject(textobj.get_pos()[0], -15,
                              new_txt, 'red', 'Courier', 70)
        return new_text, self.errortext

    def get_average_word_length(self):
        return self.average_word_len
