from tkinter import *
from tkinter import Toplevel
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


# ############ dietary classification checkbox
def selection():
    global Diet
    Diet = "Unknown"
    value = radio.get()
    if value == 1:
        Diet = "Herbivore"
    elif value == 2:
        Diet = "Carnivore"
    elif value == 3:
        Diet = "Omnivore"
    else:
        Diet = "Unknown"

    print(Diet)  # testing purposes

# Fossil details
###########
obj = LabelFrame(root, text="Fossil Details", font=20, bd=2, width=900,
                 bg=framebg, fg=framefg, height=250, relief=GROOVE)
obj.place(x=30, y=200)

Label(obj, text="Dietary Classification:", font="arial 13", bg=framebg, fg=framefg).place(x=30, y=150)

# buttons for diet
radio = IntVar()
R1 = Radiobutton(obj, text="Herbivore", variable=radio, value=1, bg=framebg, fg=framefg, command=selection)
R1.place(x=20, y=180)

R2 = Radiobutton(obj, text="Carnivore", variable=radio, value=2, bg=framebg, fg=framefg, command=selection)
R2.place(x=120, y=180)

R3 = Radiobutton(obj, text="Omnivore", variable=radio, value=3, bg=framebg, fg=framefg, command=selection)
R3.place(x=220, y=180)

R4 = Radiobutton(obj, text="Unknown", variable=radio, value=4, bg=framebg, fg=framefg, command=selection)
R4.place(x=320, y=180)

root.mainloop()
