import pygame
from Keyboard import Keyboard
from TaskText import TaskText
from TextObject import TextObject


class Main:
    def __init__(self):
        pygame.init()
        bg_path = 'resources/bg1.png'
        self.bgr = pygame.image.load(bg_path)
        words_need = 10
        words_file = 'resources/words_en.txt'
        self.screen = pygame.display.set_mode((1280, 720))
        self.wrong2 = pygame.Surface((1280, 60))
        self.err_font = pygame.font.SysFont('Courier', 70)
        # text:
        text_x = self.screen.get_width() / 2
        text_y = self.screen.get_height() / 4
        text_text_func = 'empty text'
        text_color = 'black'
        text_font = 'Courier'
        text_font_size = 70
        pygame.Surface.blit(self.screen, self.bgr, (0, 0))

        self.mykeyboard = Keyboard(self.screen)
        self.mykeyboard.show(self.screen)
        self.mytasktext = TaskText(words_file, words_need)
        self.textonscreen = TextObject(text_x, text_y, text_text_func, text_color, text_font, text_font_size)
        self.err_box_coords = (0, self.textonscreen.get_pos()[1] + 100)
        self.wrong2.blit(self.bgr, (0, -280))
        self.screen.blit(self.wrong2, self.err_box_coords)
        # self.testing = TextObject(text_x+text_font_size, text_y, lambda: 'g', 'red',text_font,text_font_size)

    def start(self):
        key_now = 0
        words_completed = 0
        finished = False
        ready = False
        word_ready = False
        err_ongoing = False
        text = self.mytasktext.create_text_list()
        self.textonscreen.set_text_func(text[words_completed])
        self.textonscreen.show(self.screen)
        while words_completed < len(text) and not finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                elif event.type == pygame.KEYDOWN:
                    my_key = event.unicode

                    if ready:
                        for i in self.mykeyboard.get_lang():  # for search in lang
                            if my_key in i:
                                for any_key in self.mykeyboard.get_keys():
                                    if any_key.get_key() == my_key:
                                        if key_now < len(text[words_completed]):
                                            if my_key == text[words_completed][key_now] and not err_ongoing:
                                                print('gotcha')
                                                self.mytasktext.on_key_right(self.textonscreen, my_key, key_now) \
                                                    .show(self.screen)
                                                key_now += 1
                                                if key_now == len(text[words_completed]):
                                                    word_ready = True
                                                    print('next please')
                                                any_key.set_color('green')
                                                any_key.show(self.screen)
                                            else:
                                                print('wrong')
                                                self.wrong2.blit(self.bgr, (0, -280))
                                                self.mytasktext.on_key_wrong(self.textonscreen, my_key, key_now) \
                                                    .show(self.wrong2, True)
                                                err_ongoing = True

                    if event.key == pygame.K_ESCAPE:
                        finished = True
                    # if event.key
                    if event.key == pygame.K_SPACE:
                        ready = True
                        if word_ready or words_completed == 0:
                            words_completed += 1
                            key_now = 0
                            word_ready = False
                        self.textonscreen.delete()
                        self.textonscreen.set_text_func(text[words_completed])
                        self.textonscreen.delete(False)
                        self.update(self.screen)
                        # self.textonscreen.set_text_func( text[words_completed])
                        # self.textonscreen.show(self.screen)
                    if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        self.mykeyboard.set_shift(True)
                        self.mykeyboard.keys_created = []
                        self.mykeyboard.create_keyboard()
                        self.mykeyboard.show(self.screen)
                    elif event.key == pygame.K_BACKSPACE and err_ongoing:
                        self.wrong2.blit(self.bgr, (0, -280))
                        cur_err, cur_err_t = self.mytasktext.delete_error_message(self.textonscreen, key_now)
                        cur_err.show(self.wrong2, True)
                        if cur_err_t == '':
                            err_ongoing = False
                elif event.type == pygame.KEYUP:
                    my_key = event.unicode
                    for i in self.mykeyboard.get_lang():
                        if my_key in i:
                            for any_key in self.mykeyboard.get_keys():
                                if any_key.get_key() == my_key:
                                    any_key.set_color('white')
                                    any_key.show(self.screen)
                    if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        self.mykeyboard.set_shift(False)
                        self.mykeyboard.keys_created = []
                        self.mykeyboard.create_keyboard()
                        self.mykeyboard.show(self.screen)
            self.screen.blit(self.wrong2, self.err_box_coords)
            pygame.display.flip()

    def update(self, surface):
        surface.blit(self.bgr, [0, 0])
        self.screen.blit(self.wrong2, self.err_box_coords)
        if not self.mykeyboard.is_deleted():
            self.mykeyboard.show(surface)
        if not self.textonscreen.is_deleted():
            self.textonscreen.show(surface)
