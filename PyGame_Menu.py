import pygame
from TextObject import TextObject
from Baton import Button
from main_pygame import Main


class Menu:
    def __init__(self):
        pygame.init()
        screen_size = (1280, 720)
        self.title_text = 'Keyboard simulator'
        self.title = TextObject(625, 100, lambda: self.title_text, 'black', 'arialblack', 80)
        self.start_main = False
        self.finished = False
        self.closed = False
        self.screen = pygame.display.set_mode(screen_size)
        self.mouse_controls = False
        self.selected_button = 0
        # Making the buttons
        self.button_dims = [(500, 300, 250, 75), (500, 425, 250, 75), (500, 550, 250, 75)]
        self.button_surfaces = [pygame.Surface(self.button_dims[0][2:]),
                                pygame.Surface(self.button_dims[1][2:]),
                                pygame.Surface(self.button_dims[2][2:])]
        self.button_list = [Button('Start', self.button_dims[0][2], self.button_dims[0][3],
                                   self.button_surfaces[0]),
                            Button('Options', self.button_dims[1][2], self.button_dims[1][3],
                                   self.button_surfaces[1]),
                            Button('Statistics', self.button_dims[2][2], self.button_dims[2][3],
                                   self.button_surfaces[2])]
        for one_button in range(len(self.button_list)):
            self.button_list[one_button].show()
            self.screen.blit(self.button_surfaces[one_button], self.button_dims[one_button][0:2])
        self.button_list[0].on_mouse_hover()

    def start(self):
        self.title.show(self.screen)
        self.finished = False
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
                        if self.button_list[self.selected_button].button_text == 'Start':
                            self.finished = True
                            self.start_main = True
                        else:
                            print('Not done yet')
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
                            if self.button_list[one_button].button_text == 'Start':
                                self.finished = True
                                self.start_main = True
                            else:
                                print('Not done yet')
                            break
            for one_button in range(len(self.button_list)):
                self.screen.blit(self.button_surfaces[one_button], self.button_dims[one_button][0:2])
            pygame.display.flip()


if __name__ == '__main__':
    # Program starts
    mymenu = Menu()
    bg_path = 'resources/bg1.png'
    bgr = pygame.image.load(bg_path)
    # This loop will return user to the menu after they close other windows
    # It will stop only if user closes the menu
    while not mymenu.closed:
        pygame.Surface.blit(mymenu.screen, bgr, (0, 0))
        mymenu.start_main = False
        mymenu.start()
        if mymenu.start_main:
            # Starting the keyboard simulator
            main = Main()
            main.start()
