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

B.title("Today's Image")
B.config(bg= 'white')
B.geometry('390x670')

current_day = datetime.now().strftime("%A")

images = {
    'Monday': 'mb.gif',
    'Tuesday': 'tb.gif',
    'Wednesday': 'wb.gif',
    'Thursday': 'thb.gif',
    'Friday': 'fb.gif',
    'Saturday': 'sb.gif', 
    "Sunday": 'sub.gif'
}

lbl = ImageLabel(B)
lbl.pack()
lbl.load(images[current_day])

def Back():
 B.destroy()
 import main


b4=tk.Button(width=20, height = 2,text='Back',border=2,bg='#DB4D30',fg='white',command= Back )
b4.place(x=20,y=600)

def Next():
 B.destroy()
 import nextB

b=tk.Button(width=20, height = 2,text='Next',border=2,bg='#DB4D30',fg='white',command= Next )
b.place(x=210,y=600)



B.mainloop()