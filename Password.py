from tkinter import *
import customtkinter as ctk
import random

def password():
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!@#$%^&*()-_=+[]{}|;:,.<>?/'

    all_chars = lower + upper + numbers + symbols

    length = int(t1.get())
    generated_password = "".join(random.sample(all_chars, length))
    t2.delete(0, END)
    t2.insert(0, generated_password)

# Create main window
win = ctk.CTk()
win.title("Password Generator")
win.geometry("600x300")

# Create and pack widgets
l1 = ctk.CTkLabel(win, text="Enter Password Length :")
l2 = ctk.CTkLabel(win, text="Generated Password : ")

t1 = ctk.CTkEntry(win, placeholder_text="Enter Pass Length")
t2 = ctk.CTkEntry(win)

b1 = ctk.CTkButton(win, text="Generate Password", command=password)

l1.place(x=100, y=50)
l2.place(x=100, y=100)

t1.place(x=250, y=50)
t2.place(x=250, y=100)

b1.place(x=100, y=150)

# Start the main loop
win.mainloop()
