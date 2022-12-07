from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import mysql.connector

win = Tk()
win.state('zoomed')
win.config(bg = 'light green')

# HEADING
Label(win, text="Login Page", font="impack 31 bold", bg="blue", fg="white").pack(fill=X)
mainloop