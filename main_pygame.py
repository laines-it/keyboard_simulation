from math import floor
from time import time
from datetime import datetime
import pygame

from Baton import Button
from Keyboard import Keyboard
from ProgressBar import ProgressBar
from TaskText import TaskText
from TextObject import TextObject


class Main:
    def __init__(self):
        pygame.init()
        bg_path = 'resources/bg1.png'
        self.bgr = pygame.image.load(bg_path)
        wnf = open('resources/options.txt', 'r')
        wnl = wnf.readlines()
        self.words_need = int(wnl[2].rstrip())
        wnf.close()
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
        self.mytasktext = TaskText(words_file, self.words_need)
        self.textonscreen = TextObject(text_x, text_y, text_text_func, text_color, text_font, text_font_size)
        self.err_box_coords = (0, self.textonscreen.get_pos()[1] + 100)
        self.wrong2.blit(self.bgr, (0, -280))
        self.screen.blit(self.wrong2, self.err_box_coords)
        # self.testing = TextObject(text_x+text_font_size, text_y, lambda: 'g', 'red',text_font,text_font_size)

    def start(self):
        key_now = 0
        self.errors_total = 0
        words_completed = 0
        self.finished = False
        ready = False
        word_ready = False
        err_ongoing = False
        self.end = False
        text = self.mytasktext.create_text_list()
        self.textonscreen.set_text_func(text[words_completed])
        self.textonscreen.show(self.screen)
        self.bar = ProgressBar(self.mykeyboard.keyboard_x,0,self.mykeyboard.get_size(),self.words_need)
        print(type(self.bar))
        time_start = floor(time())
        while not self.finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finished = True
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
                                                self.errors_total += 1
                                                self.wrong2.blit(self.bgr, (0, -280))
                                                self.mytasktext.on_key_wrong(self.textonscreen, my_key, key_now) \
                                                    .show(self.wrong2, True)
                                                err_ongoing = True
                                                any_key.set_color('red')
                                                any_key.show(self.screen)

                    if event.key == pygame.K_ESCAPE:
                        self.finished = True
                    if event.key == pygame.K_SPACE:
                        if word_ready or words_completed == 0:
                            if words_completed != 0:
                                self.bar.add()
                                print(self.bar.get_parts())
                                self.bar.show(self.screen)
                            words_completed += 1
                            key_now = 0
                            word_ready = False
                            self.textonscreen.delete()

                            try:
                                self.textonscreen.set_text_func(text[words_completed])
                                self.textonscreen.delete(False)

                            except:
                                self.textonscreen.delete()
                                self.mykeyboard.delete()
                                self.end = True

                            self.time_end = floor(time()) - time_start
                            self.update(self.screen)
                        if not ready:
                            self.textonscreen.delete()
                            self.textonscreen.set_text_func(text[words_completed])
                            self.textonscreen.delete(False)
                            self.update(self.screen)
                            ready = True
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

    def show_stat(self,surface):
        color = 'black'
        font = 'Times'
        fontsize = 60
        accurate = TextObject(surface.get_width()/2,surface.get_height()/8,'Accuracy: '+str(100 - floor((self.errors_total / self.mytasktext.get_alllen())*100))+'%',color,font,fontsize)
        accurate.show(surface)
        wpm = TextObject(surface.get_width()/2,surface.get_height()/4,'Words per Minute: '+str(floor(self.words_need // (self.time_end / 60))),color,font,fontsize)
        wpm.show(surface)
        all_time = TextObject(surface.get_width()/2,surface.get_height()/2,'Overall Time: '+str(floor(self.time_end))+'s',color,font,fontsize)
        all_time.show(surface)
        exit = TextObject(surface.get_width()/2,surface.get_height()/1.5,'Press ESCAPE',color,'arialblack',fontsize)
        exit.show(surface)
        dt_now = datetime.now()
        tmn = str(dt_now.time())
        tmn = tmn.split(':')
        tmn[2] = str(floor(float(tmn[2])))
        tmn = ':'.join(tmn)
        stat_list = [str(dt_now.date()), tmn, str(self.words_need), str(self.mytasktext.awcs), accurate.get_text(), wpm.get_text(), all_time.get_text(), '-end_stat-']
        statf = open('resources/stats.txt', 'a')
        statf.write('\n' + '\n'.join(stat_list))
        statf.close()

    def update(self, surface):
        surface.blit(self.bgr, [0, 0])
        self.screen.blit(self.wrong2, self.err_box_coords)
        if not self.mykeyboard.is_deleted():
            self.mykeyboard.show(surface)
        if not self.textonscreen.is_deleted():
            self.textonscreen.show(surface)
        if self.end:
            self.show_stat(surface)
        self.bar.show(surface)
