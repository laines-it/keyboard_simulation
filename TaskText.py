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

    # def change_color_letter(self, text, key_now):
    #     text =
    def change_color_letter(self, textobj, right, pressed, key, deleting=False):
        if deleting:
            self.errortext = self.errortext[:-1]
            new_txt = (len(textobj.get_text()[:key + 1])) * '  ' + self.errortext
            return new_txt, self.errortext
        else:
            if right:
                new_txt = (len(textobj.get_text()[:key])+1) * ' ' + pressed + ' ' * (len(textobj.get_text()) - key)
                new_text = TextObject(textobj.get_pos()[0], textobj.get_pos()[1],
                                      new_txt, 'green', 'Courier', 70)
                print(new_txt)
                print('s' * (len(textobj.get_text()) - key - 1))
                return new_text

            else:
                self.errortext += pressed
                new_txt = (len(textobj.get_text()[:key + 1])) * '  ' + self.errortext
                return new_txt

    def get_average_word_length(self):
        return self.average_word_len


