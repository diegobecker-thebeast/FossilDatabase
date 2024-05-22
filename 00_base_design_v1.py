from tkinter import *
from datetime import date
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from tkinter.ttk import Combobox
import openpyxl  # , xlrd
from openpyxl import Workbook
import pathlib

# modules required:
# pip install pathlib
# pip install openpyxl
# pip install xlrd
# pip install pillow

background = "#06283D"
framebg = "#EDEDED"
framefg = "#06283D"

root = Tk()
root.title("Fossil Registration System")
root.geometry("1250x740+210+100")
root.config(bg=background)

# top frames
Label(root, text="Diego Becker da Beast", width=10, height=3,
      bg="#f0687c", anchor='e').pack(side=TOP, fill=X)

Label(root, text="Fossil Registration", width=10, height=2,
      bg="#c36464", fg='#fff', font='arial 20 bold').pack(side=TOP, fill=X)

# search box to update
# not that Search and search are 2 different variables
Search = StringVar()
Entry(root, textvariable=Search, width=15, bd=2, font="arial 20").place(x=820, y=70)

# image_icon3 = PhotoImage(file="Images/ant.png")
Srch = Button(root, text="Search", compound=LEFT, width=12, pady=6,
              bg='#68ddfa', font="arial 13 bold")
Srch.place(x=1060, y=66)

# image_icon4 = PhotoImage(fiole="Images/Layer 4.png")
# update button for all details
update_button = Button(root, text="Update File", bg="#68ddfa",
                       font="arial 13 bold", pady=6, width=10)
update_button.place(x=110, y=64)
update_button = Button(root, text="Help", bg="#68ddfa",
                       font="arial 13 bold", pady=6, width=10)
update_button.place(x=250, y=64)

# Registration number and date - same row
Label(root, text="Registration Number:", font="arial 13", fg=framebg,
      bg=background).place(x=30, y=150)
Label(root, text="Date:", font="arial 13", fg=framebg,
      bg=background).place(x=500, y=150)

Registration = IntVar()
Date = StringVar()

reg_entry = Entry(root, textvariable=Registration, width=15, font="arial 10")
reg_entry.place(x=200, y=150)
reg_entry.config(state='readonly')


date_entry = Entry(root,  width=15, font="arial 10")
date_entry.place(x=550, y=150)

# Fossil details
###########
obj = LabelFrame(root, text="Fossil Details", font=20, bd=2, width=900,
                 bg=framebg, fg=framefg, height=250, relief=GROOVE)
obj.place(x=30, y=200)

# additional details
#########
obj2 = LabelFrame(root, text="Additional Details", font=20, bd=2, width=900,
                  bg=framebg, fg=framefg, height=250, relief=GROOVE)
obj2.place(x=30, y=470)

root.mainloop()
