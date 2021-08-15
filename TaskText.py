from math import floor
from random import random, randint, choice

from TextObject import TextObject


class TaskText:
    def __init__(self,file_path, words_need):
        self.file_path = file_path
        self.words_need = words_need

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
        word_list= []
        word_list.append("Press SPACE if you're ready")

        all_words = 0
        all_len = 0
        Ns = 0
        while all_words < self.words_need:
            text = ''
            for i in range(randint(1, 4)):
                if all_words >= self.words_need:
                    break
                all_words += 1
                one_word = choice(words)
                print(one_word)
                all_len += len(one_word)
                if random() > 0:
                    one_word.upper()
                text += one_word + ' '
            word_list.append(text)
            Ns += 1
        self.average_word_len = round((all_len / all_words),1)
        return word_list

    def get_average_word_length(self):
        return self.average_word_len


