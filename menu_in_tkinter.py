from tkinter import Tk, Canvas, NW, BOTH
from PIL import Image, ImageTk
from modules.simulation1 import Sim


class Menu:
    def __init__(self):
        self.root = Tk()
        self.root.resizable(False, False)
        bgpath = "D:/bg1.png"
        self.bg = ImageTk.PhotoImage(Image.open(bgpath))
        self.img = Image.open("D:/cry.png")
        self.cry = ImageTk.PhotoImage(self.img)
        self.img = Image.open("D:/cry_white.png")
        self.cry_white = ImageTk.PhotoImage(self.img)
        self.c = Canvas(self.root, width=self.bg.width(), height=self.bg.height())
        self.c.pack(expand=True, fill=BOTH)
        self.c.create_image(0, 0, image=self.bg, anchor=NW)
        title_text = 'Keyboard Simulator'
        title_text_h = self.bg.height() / 6
        title_text_w = self.bg.width() / 3
        button_h = self.bg.height() / 3
        button_w = self.bg.width() / 8
        self.button_space = self.bg.height() / 6
        self.c.create_text(title_text_w, title_text_h, text=title_text, font='Cambria 60')
        self.selected_butt = 0
        self.select_frame = self.c.create_rectangle(0,
                                                    (button_h + title_text_h) / 2,
                                                    self.bg.width() / 2,
                                                    button_h + self.cry.height(),
                                                    fill='black')
        self.butts = [(self.c.create_image(button_w, button_h + i * self.button_space, image=self.cry)) for i in
                      range(4)]
        self.texts = []
        text_for_butt = ["START", "RESULTS", "OPTIONS", "QUIT"]
        for t in text_for_butt:
            self.texts.append(self.c.create_text((button_w + self.bg.width() / 2) / 2,
                                                 button_h + text_for_butt.index(t) * self.button_space, text=t,
                                                 font='Courier 40'))
        self.c.itemconfigure(self.butts[0], image=self.cry_white)
        self.c.itemconfigure(self.texts[0], fill='white')
        self.root.bind('<KeyPress>', self.on_key_press)
        print('binded')
        self.root.bind('<KeyRelease>', self.on_key_release)

    def on_key_press(self, event):
        pressed_key = event.keysym
        print(pressed_key)
        move = 0
        if pressed_key == 'Down' and self.selected_butt < 3:
            move = 1
        if pressed_key == 'Up' and self.selected_butt > 0:
            move = -1
        self.selected_butt += move
        for i in self.butts:
            if self.selected_butt == self.butts.index(i):
                self.c.itemconfigure(i, image=self.cry_white)
                self.c.itemconfigure(self.texts[self.selected_butt], fill='white')
                self.c.move(self.select_frame, 0, move * self.button_space)
            else:
                self.c.itemconfigure(i, image=self.cry)
                for other_t in self.texts:
                    if self.texts.index(other_t) != self.selected_butt:
                        self.c.itemconfigure(other_t, fill='black')
        if (pressed_key == 'Return' or pressed_key == 'space') and (self.selected_butt == 0):
            print('DESTROYED')
            self.root.destroy()
            mysim = Sim()
            mysim.start()
            self.start()
        elif (pressed_key == 'Return' or pressed_key == 'space') and (self.selected_butt == 3):
            print('QUITED')
            self.root.destroy()

    def on_key_release(self, event):
        pass

    def get_resource(self, res):
        if res == 'bg':
            return self.bg
        elif res == 'cry':
            return self.cry
        elif res == 'cry_white':
            return self.cry_white

    def start(self):
        mymenu = Menu()
        mymenu.root.mainloop()


if __name__ == '__main__':
    mymenu = Menu()
    mymenu.root.mainloop()
