import pygame
from TextObject import TextObject
from Baton import Button


class Stats:
    def __init__(self):
        pygame.init()
        screen_size = (1280, 720)
        bg_path = 'resources/bg1.png'
        self.bgr = pygame.image.load(bg_path)
        statf = open('resources/stats.txt')
        statl = statf.readlines()
        statf.close()
        self.statm = []
        statm1 = []
        for stat_line in statl:
            if stat_line.strip() == '-end_stat-':
                self.statm.append(statm1)
                statm1 = []
            else:
                statm1.append(stat_line.strip())
        print(self.statm)
        self.stat_pos = [(300, 100), (300, 150), (300, 200), (300, 250), (300, 300), (300, 350), (300, 400)]
        self.stat_text = ['Date: ', 'Time: ', 'Word number: ', 'Average word length: ', '', '', '']
        self.title_text = 'Keyboard simulator'
        self.current_stat_block = 0
        self.title = TextObject(625, 100, self.title_text, 'black', 'arialblack', 80)
        self.finished = False
        self.screen = pygame.display.set_mode(screen_size)
        self.mouse_controls = False
        self.selected_button = 0
        # Making the buttons
        self.button_dims = [(300, 600, 250, 75), (650, 600, 250, 75)]
        self.button_surfaces = [pygame.Surface(self.button_dims[0][2:]),
                                pygame.Surface(self.button_dims[1][2:])]
        self.button_list = [Button('Previous', self.button_dims[0][2], self.button_dims[0][3],
                                   self.button_surfaces[0]),
                            Button('Next', self.button_dims[1][2], self.button_dims[1][3],
                                   self.button_surfaces[1])]
        for one_button in range(len(self.button_list)):
            self.button_list[one_button].show()
            self.screen.blit(self.button_surfaces[one_button], self.button_dims[one_button][0:2])
        self.button_list[0].make_inactive()
        if len(self.statm) == 1:
            self.button_list[1].make_inactive()
        self.button_list[0].on_mouse_hover()

    def button_click(self, sel_button):
        if self.button_list[sel_button].on_mouse_click() == 'Previous':
            self.current_stat_block -= 1
            print(self.current_stat_block)
            if self.current_stat_block == 0:
                self.button_list[0].make_inactive()
                self.selected_button = 1
                self.button_list[1].make_active()
                self.button_list[1].on_mouse_hover()
            else:
                self.button_list[1].make_active()
        elif self.button_list[sel_button].on_mouse_click() == 'Next':
            self.current_stat_block += 1
            print(self.current_stat_block)
            if self.current_stat_block == len(self.statm) - 1:
                self.button_list[1].make_inactive()
                self.selected_button = 0
                self.button_list[0].make_active()
                self.button_list[0].on_mouse_hover()
            else:
                self.button_list[0].make_active()

    def start(self):
        self.current_stat_block = 0
        self.title.show(self.screen)
        self.finished = False
        self.selected_button = 0
        while not self.finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finished = True
                    self.closed = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.finished = True
                        self.closed = True
                    # Keyboard controls
                    elif event.key == pygame.K_w or event.key == pygame.K_UP:
                        # Selecting previous button
                        self.mouse_controls = False
                        self.button_list[self.selected_button].on_mouse_unhover()
                        if self.selected_button == 0:
                            self.selected_button = 1
                            self.button_list[self.selected_button].on_mouse_hover()
                        else:
                            self.selected_button = 0
                            self.button_list[self.selected_button].on_mouse_hover()
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        # Selecting next button
                        self.mouse_controls = False
                        self.button_list[self.selected_button].on_mouse_unhover()
                        if self.selected_button == 1:
                            self.selected_button = 0
                            self.button_list[self.selected_button].on_mouse_hover()
                        else:
                            self.selected_button = 1
                            self.button_list[self.selected_button].on_mouse_hover()
                    elif event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        # Activating the button
                        self.button_click(self.selected_button)
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
                            self.button_click(one_button)
                            break
            self.screen.blit(self.bgr, (0, 0))
            for stat_line in range(len(self.stat_pos)):
                stat_text1 = self.stat_text[stat_line] + self.statm[self.current_stat_block][stat_line]
                line_s = TextObject(self.stat_pos[stat_line][0], self.stat_pos[stat_line][1],
                                    stat_text1, 'black', 'calibri', 50)
                line_s.show(self.screen, False)
            for one_button in range(len(self.button_list)):
                self.screen.blit(self.button_surfaces[one_button], self.button_dims[one_button][0:2])
            pygame.display.flip()
