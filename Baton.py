import pygame

from TextObject import TextObject


# I just copied class "Key" because why not?
class Button:
    def __init__(self, button_text, keysizex, keysizey, surface, radiuss=0, action='-no_action-'):
        self.keysizex = keysizex
        self.keysizey = keysizey
        self.color = 'white'
        self.set_color('white')
        self.radius = radiuss
        self.button_text = button_text
        self.surface = surface
        self.action = action
        self.is_active = True

    def set_color(self, color):
        # This func changes color according to the "rgb" argument
        self.color = color

    def get_color(self):
        return self.color

    def create_text(self):
        textx = self.keysizex / 2
        texty = self.keysizey / 4
        font = 'Times'
        font_size = 30
        color_text = 'black'
        self.keytext = TextObject(textx, texty, self.button_text, color_text, font, font_size)

    def show(self):
        self.create_text()
        r = pygame.Rect(0, 0, self.keysizex, self.keysizey)
        pygame.draw.rect(self.surface, self.color, r, border_radius=self.radius)
        self.keytext.show(self.surface)

    def on_mouse_hover(self):
        # This function will trigger when mouse hovers over the button
        if self.is_active:
            self.set_color((100, 100, 100))
            self.show()

    def on_mouse_unhover(self):
        # This function will trigger when mouse stops hovering over the button
        if self.is_active:
            self.set_color('white')
            self.show()

    def on_mouse_click(self):
        if self.is_active:
            if self.action == '-no_action-':
                return self.button_text
            else:
                return self.action
        else:
            return '-is_inactive-'

    def make_inactive(self):
        self.is_active = False
        self.set_color((50, 50, 50))
        self.show()

    def make_active(self):
        self.is_active = True
        self.set_color('white')
        self.show()
