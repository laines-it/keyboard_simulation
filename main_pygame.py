import pygame
from Keyboard import Keyboard
from TaskText import TaskText
from TextObject import TextObject


class Main:
    def __init__(self):
        pygame.init()
        bg_path = 'D:/bg1.png'
        bgr = pygame.image.load(bg_path)
        words_need = 10
        words_file = 'D:/words_en.txt'
        self.screen = pygame.display.set_mode((1280, 720))
        # text:
        text_x = self.screen.get_width() / 2
        text_y = self.screen.get_height() / 4
        text_text_func = 'rfed'
        text_color = 'black'
        text_font = 'Courier'
        text_font_size = 40
        pygame.Surface.blit(self.screen, bgr, (0, 0))
        self.mykeyboard = Keyboard(self.screen)
        self.mykeyboard.show(self.screen)
        self.mytasktext = TaskText(words_file, words_need)
        self.textonscreen = TextObject(text_x, text_y, lambda: text_text_func, text_color, text_font, text_font_size)

    def start(self):
        words_completed = 0
        finished = False
        text = self.mytasktext.create_text_list()
        while words_completed < len(text) and not finished:
            keys = pygame.key.get_pressed()
            self.textonscreen.set_text_func(lambda : text[words_completed])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                elif event.type == pygame.KEYDOWN:
                    mykey = event.unicode
                    for i in self.mykeyboard.get_lang():
                        if mykey in i:
                            for any_key in self.mykeyboard.get_keys():
                                if any_key.get_key() == mykey:
                                    any_key.set_color('green')
                                    any_key.show(self.screen)
                    if event.key == pygame.K_ESCAPE:
                        finished = True
                    if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        self.mykeyboard.set_shift(True)
                        self.mykeyboard.create_keyboard()
                        self.mykeyboard.show(self.screen)
                elif event.type == pygame.KEYUP:
                    mykey = event.unicode
                    for i in self.mykeyboard.get_lang():
                        if mykey in i:
                            for any_key in self.mykeyboard.get_keys():
                                if any_key.get_key() == mykey:
                                    any_key.set_color('white')
                                    any_key.show(self.screen)
                    if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        self.mykeyboard.set_shift(False)
                        self.mykeyboard.create_keyboard()
                        self.mykeyboard.show(self.screen)

            pygame.display.flip()


if __name__ == '__main__':
    main = Main()
    main.start()
