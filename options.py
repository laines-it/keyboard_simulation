import pygame
from TextObject import TextObject
from Baton import Button


class Options:
    def __init__(self):
        pygame.init()
        screen_size = (1280, 720)
        bg_path = 'resources/bg1.png'
        self.bgr = pygame.image.load(bg_path)
        self.option_cur = []
        self.opt = open('resources/options.txt', 'r')
        self.option_cur.append(self.opt.readline().strip())
        self.option_cur.append(self.opt.readline().strip())
        self.option_cur.append(self.opt.readline().strip())
        self.opt.close()
        self.modes = ['Words', 'Sentences']
        self.finished = False
        self.screen = pygame.display.set_mode(screen_size)
        self.option_text = ['Average word length: ', 'Current typing mode: ', 'Word count: ']
        self.option_text_pos = [(100, 100), (100, 250), (100, 400)]
        self.button_dims = [(100, 150, 100, 75), (250, 150, 100, 75),
                            (100, 300, 200, 75), (350, 300, 200, 75),
                            (100, 450, 100, 75), (250, 450, 100, 75),
                            (100, 600, 250, 75)]
        self.button_surfaces = [pygame.Surface(self.button_dims[0][2:]),
                                pygame.Surface(self.button_dims[1][2:]),
                                pygame.Surface(self.button_dims[2][2:]),
                                pygame.Surface(self.button_dims[3][2:]),
                                pygame.Surface(self.button_dims[4][2:]),
                                pygame.Surface(self.button_dims[5][2:]),
                                pygame.Surface(self.button_dims[6][2:])]
        self.button_list = [Button('+', self.button_dims[0][2], self.button_dims[0][3],
                                   self.button_surfaces[0], action='AWL+'),
                            Button('-', self.button_dims[1][2], self.button_dims[1][3],
                                   self.button_surfaces[1], action='AWL-'),
                            Button('Words', self.button_dims[2][2], self.button_dims[2][3],
                                   self.button_surfaces[2]),
                            Button('Sentences', self.button_dims[3][2], self.button_dims[3][3],
                                   self.button_surfaces[3]),
                            Button('+', self.button_dims[4][2], self.button_dims[4][3],
                                   self.button_surfaces[4], action='WC+'),
                            Button('-', self.button_dims[5][2], self.button_dims[5][3],
                                   self.button_surfaces[5], action='WC-'),
                            Button('Save changes', self.button_dims[6][2], self.button_dims[6][3],
                                   self.button_surfaces[6])]
        self.selected_button = 0
        self.mouse_controls = False
        pygame.Surface.blit(self.screen, self.bgr, (0, 0))
        for one_option in range(len(self.option_text)):
            opt = self.option_text[one_option] + self.option_cur[one_option]
            opt_t = TextObject(self.option_text_pos[one_option][0], self.option_text_pos[one_option][1],
                               opt, 'black', 'Times', 30)
            opt_t.show(self.screen, False)
        for one_button in range(len(self.button_list)):
            self.button_list[one_button].show()
            self.screen.blit(self.button_surfaces[one_button], self.button_dims[one_button][0:2])

    def start(self):
        self.finished = False
        self.mouse_controls = False
        self.selected_button = 0
        while not self.finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finished = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.finished = True
                    elif event.key == pygame.K_w or event.key == pygame.K_UP:
                        # Selecting previous button
                        self.mouse_controls = False
                        self.button_list[self.selected_button].on_mouse_unhover()
                        if self.selected_button == 0:
                            self.selected_button = 2
                            self.button_list[self.selected_button].on_mouse_hover()
                        else:
                            self.selected_button -= 1
                            self.button_list[self.selected_button].on_mouse_hover()
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        # Selecting next button
                        self.mouse_controls = False
                        self.button_list[self.selected_button].on_mouse_unhover()
                        if self.selected_button == 2:
                            self.selected_button = 0
                            self.button_list[self.selected_button].on_mouse_hover()
                        else:
                            self.selected_button += 1
                            self.button_list[self.selected_button].on_mouse_hover()
                    elif event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        # Activating the button
                        if self.button_list[self.selected_button].on_mouse_click() == 'AWL+':
                            self.option_cur[0] = str(int(self.option_cur[0]) + 1)
                        elif self.button_list[self.selected_button].on_mouse_click() == 'AWL-':
                            self.option_cur[0] = str(int(self.option_cur[0]) - 1)
                        elif self.button_list[self.selected_button].on_mouse_click() == 'Words':
                            self.option_cur[1] = 'Words'
                        elif self.button_list[self.selected_button].on_mouse_click() == 'Sentences':
                            self.option_cur[1] = 'Sentences'
                        elif self.button_list[self.selected_button].on_mouse_click() == 'WC+':
                            self.option_cur[2] = str(int(self.option_cur[2]) + 1)
                        elif self.button_list[self.selected_button].on_mouse_click() == 'WC-':
                            self.option_cur[2] = str(int(self.option_cur[2]) - 1)
                        elif self.button_list[self.selected_button].on_mouse_click() == 'Save changes':
                            opt_write = [self.option_cur[0], self.option_cur[1], self.option_cur[2]]
                            ow = open('resources/options.txt', 'w')
                            ow.write('\n'.join(opt_write))
                            ow.close()
                # Mouse controls
                elif event.type == pygame.MOUSEMOTION:
                    # Finding and selecting the button that mouse is hovering over
                    mouse_coords = pygame.mouse.get_pos()
                    for one_button in range(len(self.button_dims)):
                        if self.button_dims[one_button][0] <= mouse_coords[0] <= \
                                self.button_dims[one_button][0] + self.button_dims[one_button][2] \
                                and self.button_dims[one_button][1] <= mouse_coords[1] <= \
                                self.button_dims[one_button][1] + self.button_dims[one_button][3]:
                            self.button_list[self.selected_button].on_mouse_unhover()
                            self.button_list[one_button].on_mouse_hover()
                            self.mouse_controls = True
                        else:
                            if self.mouse_controls:
                                self.button_list[one_button].on_mouse_unhover()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Finding and activating the button that mouse clicked
                    mouse_coords = pygame.mouse.get_pos()
                    for one_button in range(len(self.button_dims)):
                        if self.button_dims[one_button][0] <= mouse_coords[0] <= \
                                self.button_dims[one_button][0] + self.button_dims[one_button][2] \
                                and self.button_dims[one_button][1] <= mouse_coords[1] <= \
                                self.button_dims[one_button][1] + self.button_dims[one_button][3]:
                            if self.button_list[one_button].on_mouse_click() == 'AWL+':
                                self.option_cur[0] = str(int(self.option_cur[0]) + 1)
                            elif self.button_list[one_button].on_mouse_click() == 'AWL-':
                                self.option_cur[0] = str(int(self.option_cur[0]) - 1)
                            elif self.button_list[one_button].on_mouse_click() == 'Words':
                                self.option_cur[1] = 'Words'
                            elif self.button_list[one_button].on_mouse_click() == 'Sentences':
                                self.option_cur[1] = 'Sentences'
                            elif self.button_list[one_button].on_mouse_click() == 'WC+':
                                self.option_cur[2] = str(int(self.option_cur[2]) + 1)
                            elif self.button_list[one_button].on_mouse_click() == 'WC-':
                                self.option_cur[2] = str(int(self.option_cur[2]) - 1)
                            elif self.button_list[one_button].on_mouse_click() == 'Save changes':
                                opt_write = [self.option_cur[0], self.option_cur[1], self.option_cur[2]]
                                ow = open('resources/options.txt', 'w')
                                ow.write('\n'.join(opt_write))
                                ow.close()
            pygame.Surface.blit(self.screen, self.bgr, (0, 0))
            for one_option in range(len(self.option_text)):
                opt = self.option_text[one_option] + self.option_cur[one_option]
                opt_t = TextObject(self.option_text_pos[one_option][0], self.option_text_pos[one_option][1],
                                   opt, 'black', 'Times', 30)
                opt_t.show(self.screen, False)
            for one_button in range(len(self.button_list)):
                self.screen.blit(self.button_surfaces[one_button], self.button_dims[one_button][0:2])
            pygame.display.flip()
