import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image
import mysql.connector
from tkinter import messagebox
import datetime

# connecting to the database
conn = mysql.connector.connect(
    host='localhost' , password = 'iiitkottayam@2021' , user = 'root' , database= 'python_database'
)

cursor = conn.cursor()

current_day = datetime.datetime.now().strftime("%A")

def submit_review():
    rating = rating_var.get()
    feedback = feedback_entry.get("1.0", "end")
    
    
    cursor.execute("INSERT INTO reviews ( menu_item, rating, feedback) VALUES ( %s, %s , %s)", (set_selected_item(), rating, feedback))
    conn.commit()
    messagebox.showinfo("thank you","      Review successfully submitted     ")
    root.destroy()
    import final

def show_menu():
    current_day = datetime.datetime.now().strftime("%A")
    if current_day=='Monday' :
     cursor.execute("SELECT Lunch FROM menu_monday")
     rows = cursor.fetchall()
     for row in rows:
         menu_list.insert("end", row[0])

    elif current_day=='Tuesday' :
     cursor.execute("SELECT Lunch FROM menu_tuesday")
     rows = cursor.fetchall()
     for row in rows:
         menu_list.insert("end", row[0])

    elif current_day=='Wednesday' :
     cursor.execute("SELECT Lunch FROM menu_wednesday")
     rows = cursor.fetchall()
     for row in rows:
         menu_list.insert("end", row[0])

    elif current_day=='Thursday' :
     cursor.execute("SELECT Lunch FROM menu_thursday")
     rows = cursor.fetchall()
     for row in rows:
         menu_list.insert("end", row[0])

    elif current_day=='Friday' :
     cursor.execute("SELECT Lunch FROM menu_friday")
     rows = cursor.fetchall()
     for row in rows:
         menu_list.insert("end", row[0])

    elif current_day=='Saturday' :
     cursor.execute("SELECT Lunch FROM menu_saturday")
     rows = cursor.fetchall()
     for row in rows:
         menu_list.insert("end", row[0])

    else :
     cursor.execute("SELECT Lunch FROM menu_sunday")
     rows = cursor.fetchall()
     for row in rows:
         menu_list.insert("end", row[0])

def update_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    current_day = datetime.datetime.now().strftime("%A")
    current_date = datetime.datetime.now().strftime("%B %d, %Y")
    time_label.config(text=current_time)
    day_label.config(text=current_day)
    date_label.config(text=current_date)
    time_label.after(1000, update_time)

root = tk.Tk()
root.geometry("390x690")
root.title("Food Review System")
root.configure(bg='#f5f5dc')

bgm = "bgim.png"
bg = ImageTk.PhotoImage(Image.open(bgm))
label1 = ttk.Label( root, image = bg , anchor='center')
label1.place(x = 0, y = 0, relheight=1 , relwidth=1 )



# Create a label for menu
menu_label = ttk.Label(root, text="Select a menu item:", font=("Helvetica", 12))
menu_label.place(x=120,y=145)
# menu_label.pack()

# Create a listbox for menu
menu_list = tk.Listbox(root, background='#f0f8ff')
menu_list.place(x=135, y=165)
# menu_list.pack()

# Populate menu list
show_menu()

# Create a label for rating
rating_label = ttk.Label(root, text="Please rate the food:", font=("Helvetica", 12))
rating_label.place(x=100 , y=335)
# rating_label.pack()

# Create a scale for rating
rating_var = tk.IntVar()
rating_scale = ttk.Scale(root, from_=1, to=5, variable=rating_var, orient='horizontal', length=250)
rating_scale.place(x=90 , y=385)
# rating_scale.pack()

# Create a label for feedback
feedback_label = ttk.Label(root, text="Please provide feedback:", font=("Helvetica", 12))
feedback_label.place(x=90 , y=435)
# feedback_label.pack()

# Create a textbox for feedback
feedback_entry = tk.Text(root, height=10, width=30)
feedback_entry.place(x=90 , y=465)
# feedback_entry.pack()

# Create a button for submitting the review
submit_button = ttk.Button(root, text="Submit", command=submit_review)
submit_button.place(x=150, y=645)
# submit_button.pack()

def set_selected_item():
    selected_item = menu_list.get(menu_list.curselection())
    return selected_item
    

menu_list.bind('&#8203;`oaicite:{"index":0,"invalid_reason":"Malformed citation ListboxSelect>>"}`&#8203;', lambda : set_selected_item(menu_list))
# menu_list.bind( '<<ListboxSelect>>', set_selected_item)



time_label = tk.Label(root, font=("calibri", 24, "bold") ,foreground="white" , bg="#37403f"  )
time_label.grid(row=0, column=0, padx=100)

day_label = tk.Label(root, font=("calibri", 20, "bold") , foreground="white" , bg="#37403f" )
day_label.grid(row=1, column=0, padx=100)

date_label = tk.Label(root, font=("calibri", 20, "bold"), foreground="white" , bg="#37403f" )
date_label.grid(row=2, column=0, padx=100)

update_time()


root.mainloop()
