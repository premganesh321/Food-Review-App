import tkinter as tk
from PIL import Image, ImageTk
from itertools import count, cycle
from datetime import datetime

class ImageLabel(tk.Label):
    """
    A Label that displays images, and plays them if they are gifs
    :im: A PIL Image instance or a string filename
    """
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []

        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)

        try:
            self.delay = im.info[1]
        except:
            self.delay = 40

        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)

#demo :
B = tk.Tk()

B.title("FOOD REVIEW")
B.config(bg= 'white')
B.geometry('925x500')

logo = "logofpro.gif"
lbl = ImageLabel(B)
lbl.pack()
lbl.load(logo)

def window_main():
    B.destroy()
    import minimal_login

B.after(2002 , window_main)


B.mainloop()