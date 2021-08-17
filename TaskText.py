from random import random, choice
from TextObject import TextObject


class TaskText:
    def __init__(self, file_path, words_need):
        self.file_path = file_path
        self.words_need = words_need
        self.errortext = ''
        self.average_word_len = 0

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
        awcf = open('resources/options.txt', 'r')
        awc = awcf.readlines()
        awcs = int(awc[0].strip())
        awcf.close()
        words = self.extract_words(self.file_path)
        word_list = []
        word_list.append("Press SPACE if you're ready")

        all_words = 0
        self.all_len = 0
        while all_words < self.words_need:
            if self.average_word_len > awcs:
                one_word = choice(words)
                if len(one_word) < self.average_word_len:
                    all_words += 1
                    print(one_word)
                    self.all_len += len(one_word)
                    if random() > 0:
                        one_word.upper()
                    word_list.append(one_word)
            else:
                one_word = choice(words)
                if len(one_word) >= self.average_word_len:
                    all_words += 1
                    print(one_word)
                    self.all_len += len(one_word)
                    if random() > 0:
                        one_word.upper()
                    word_list.append(one_word)
            self.average_word_len = round((self.all_len / all_words), 1)
        return word_list

        # Если нажатая клавиша была правильной
    def on_key_right(self, textobj, pressed, key):
        new_txt = (len(textobj.get_text()[:key]) + 1) * ' ' + pressed + ' ' * (len(textobj.get_text()) - key)
        new_text = TextObject(textobj.get_pos()[0], textobj.get_pos()[1],
                              new_txt, 'green', 'Courier', 70)
        return new_text

    def get_alllen(self):
        return self.all_len

    def get_allwords(self):
        return self.all_len

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
