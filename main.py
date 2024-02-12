from tkinter import *
from PIL import ImageTk,Image
import tkinter as tk
import datetime


root = tk.Tk()

root.title('food')
root.config(bg= 'white')
root.geometry('390x670')


# def update_time():
#     current_time = datetime.datetime.now().strftime("%H:%M:%S")
#     current_day = datetime.datetime.now().strftime("%A")
#     current_date = datetime.datetime.now().strftime("%B %d, %Y")
#     time_label.config(text=current_time)
#     day_label.config(text=current_day)
#     date_label.config(text=current_date)
#     time_label.after(1000, update_time)

root.geometry('390x605')


bgm = "bgimg.png"
bg = ImageTk.PhotoImage(Image.open(bgm))
label1 = Label( root, image = bg , anchor='center')
label1.place(x = 0, y = 0, relheight=1 , relwidth=1 )


# time_label = tk.Label(root, font=("calibri", 30, "bold") , background="white" , bg="#fff4bf" )
# time_label.grid(row=0, column=0, padx=100, pady=2 )

# day_label = tk.Label(root, font=("calibri", 20, "bold") , background="white" , bg="#fff4bf")
# day_label.grid(row=1, column=0, padx=100, pady=0.4)

# date_label = tk.Label(root, font=("calibri", 20, "bold"), background="white" , bg="#fff4bf")
# date_label.grid(row=2, column=0, padx=100, pady=1)

# update_time()



def Breakfast():
 root.destroy()
 import Breakfast

def Lunch():
 root.destroy()
 import Lunch

def Dinner():
 root.destroy()
 import Dinner



b2=tk.Button(width=30, height = 2,text='Breakfast',border=2,bg='#DB4D30',fg='white',command= Breakfast )
b2.place(x=100,y=320)

b3=tk.Button(width=30,height = 2,text='Lunch',border=1,bg='#DB4D30',fg='white',command= Lunch)
b3.place(x=100,y=385)

b4=tk.Button(width=30,height = 2,text='Dinner',border=1,bg='#DB4D30',fg='white',command= Dinner)
b4.place(x=100,y=445)


root.mainloop()
