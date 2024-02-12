from tkinter import *
from PIL import ImageTk,Image
import tkinter as tk
import datetime


root = tk.Tk()

root.title('thanks')
root.config(bg= 'white')
root.geometry('390x670')



root.geometry('925x500')


bgm = "lastimg.png"
bg = ImageTk.PhotoImage(Image.open(bgm))
label1 = Label( root, image = bg , anchor='center')
label1.place(x = 0, y = 0, relheight=1 , relwidth=1 )




root.mainloop()
