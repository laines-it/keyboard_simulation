import pygame


class TextObject:
    def __init__(self, x, y, text, color, font_name, font_size):
        self.pos = (x, y)
        self.text = text
        self.text_func = lambda: text
        self.color = color
        self.font = pygame.font.SysFont(font_name, font_size)
        self.deleted = 0
        self.bounds = self.get_surface(text)

    def show(self, surface, centralized=True):
        text_surface, self.bounds = self.get_surface(self.text)
        if centralized:
            pos = (self.pos[0] - self.bounds.width // 2, self.pos[1])
        else:
            pos = self.pos
        surface.blit(text_surface, pos)

    def set_text_func(self, text):
        self.text = text
        self.text_func = lambda: text

    def get_pos(self):
        return self.pos

    def get_text(self):
        return self.text

    def get_surface(self, text):
        text_surface = self.font.render(text, False, self.color)
        return text_surface, text_surface.get_rect()

    def delete(self, deletet = True):
        self.deleted = deletet

    def is_deleted(self):
        return self.deleted
    
    def update(self):
        pass
