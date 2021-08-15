import pygame

from TextObject import TextObject


class Key:
    def __init__(self, x, y, key, keysizex, keysizey):
        self.x = x
        self.y = y
        self.keysizex = keysizex
        self.keysizey = keysizey
        self.set_color('white')
        self.radius = 10
        self.key = key

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_key(self):
        return self.key

    def get_keysizex(self):
        return self.keysizex

    def add_keysizex(self, keysizex):
        self.keysizex += keysizex

    def get_keysizey(self):
        return self.keysizey

    def add_keysizey(self, keysizey):
        self.keysizey += keysizey

    def set_color(self, color):
        # This func changes color according "rgb" argument
        self.color = color

    def get_color(self):
        return self.color

    def create_text(self):
        textx = self.x + self.keysizex / 2
        texty = self.y + self.keysizey / 4
        font = 'Times'
        font_size = 30
        color_text = 'black'
        self.keytext = TextObject(textx, texty, lambda: self.key, color_text, font, font_size)

    def show(self, surface):
        self.create_text()
        r = pygame.Rect(self.x, self.y, self.keysizex, self.keysizey)
        pygame.draw.rect(surface, self.color, r, border_radius=self.radius)
        self.keytext.show(surface)
