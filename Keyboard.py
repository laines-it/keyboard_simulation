from Key import Key


class Keyboard:
    def __init__(self, surface):
        self.deleted = False
        indent = 3
        size_backspace = 3
        self.lang = [["`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "BackSpace"],
                     ["Tab", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "[", "]", "Return"],
                     ["Caps", "a", "s", "d", "f", "g", "h", "j", "k", "l", ";", "'"],
                     ["Shift_L", "z", "x", "c", "v", "b", "n", "m", ",", ".", "/", "Shift_R"],
                     ["Ctrl", "Win", "Alt", "space", "Alt", "Fn", "List", "Ctrl"]]
        self.lang_shift = [["~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "BackSpace"],
                           ["Tab", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "{", "}", "Return"],
                           ["Caps", "A", "S", "D", "F", "G", "H", "J", "K", "L", ":", '""'],
                           ["Shift_L", "Z", "X", "C", "V", "B", "N", "M", "<", ">", "?", "Shift_R"],
                           ["Ctrl", "Win", "Alt", "space", "Alt", "Fn", "List", "Ctrl"]]
        keys_total = (len(self.lang[0]) + size_backspace) + 2 * indent
        self.shifted = False
        self.keysize = surface.get_width() / keys_total
        self.keyspace = self.keysize / 10
        self.keys_created = []
        self.keyboard_x = indent * self.keysize
        self.keyboard_y = surface.get_height() / 2
        self.create_keyboard()

    def create_keyboard(self):
        for hor in range(5):
            k = 0
            dopkeysizex = 0
            if self.shifted:
                my_language = self.lang_shift
            else:
                my_language = self.lang
            for vert in my_language[hor]:
                new_key = Key(self.keyboard_x + (self.keysize + self.keyspace) * k + dopkeysizex,
                              self.keyboard_y + (self.keysize + self.keyspace) * hor,
                              vert,
                              self.keysize,
                              self.keysize)

                if vert == "BackSpace":
                    new_key.add_keysizex(self.keysize * 2)
                elif vert == "Tab":
                    dopkeysizex = self.keysize * 0.5
                    new_key.add_keysizex(dopkeysizex)
                elif vert == "Return":
                    dopkeysizex = self.keysize * 0.5
                    dopkeysizey = self.keysize * 1 + self.keyspace
                    new_key.add_keysizex(dopkeysizex)
                    new_key.add_keysizey(dopkeysizey)
                elif vert == "Caps":
                    dopkeysizex = self.keysize * 1
                    new_key.add_keysizex(dopkeysizex)
                elif vert == "Shift_L":
                    dopkeysizex = self.keysize * 1.5
                    new_key.add_keysizex(dopkeysizex)
                elif vert == "Shift_R":
                    dopkeysizex = self.keysize * 1.5
                    new_key.add_keysizex(dopkeysizex)
                elif vert == "space":
                    dopkeysizex = self.keysize * 7.5
                    new_key.add_keysizex(dopkeysizex)

                self.keys_created.append(new_key)
                k += 1

    def set_shift(self, shift):
        self.shifted = shift

    def get_keys(self):
        return self.keys_created

    def get_lang(self):
        if self.shifted:
            return self.lang_shift
        else:
            return self.lang

    def delete(self,deletet = True):
        self.deleted = deletet

    def is_deleted(self):
        return self.deleted

    def show(self, surface):
        # ITS ONLY FOR VISUALISATION
        for let in self.keys_created:
            let.show(surface)
