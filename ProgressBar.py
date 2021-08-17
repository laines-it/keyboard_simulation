import pygame


class ProgressBar:
    def __init__(self,x,y,size,words):
        self.x = x
        self.y = y
        self.one_part = size / words
        self.parts = 0
        self.sizey = 50
        self.words = words

    def show(self,surface):
        r = pygame.Rect(self.x, self.y, self.one_part * self.parts, self.sizey)
        color = (255-(255/self.words)*self.parts,255,0)
        pygame.draw.rect(surface,color, r, border_radius=5)

    def add(self):
        self.parts += 1

    def get_parts(self):
        return self.parts

