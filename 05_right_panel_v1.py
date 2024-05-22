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

# image
f = Frame(root, bd=3, bg="black", width=200, height=200, relief=GROOVE)
f.place(x=1000, y=150)

# buttons for image
Button(root, text="Upload", width=19, height=2, font="arial 12 bold",
       bg="lightblue").place(x=1000, y=370)

saveButton = Button(root, text="Save", width=19, height=2,
                    font="arial 12 bold", bg="lightgreen")
saveButton.place(x=1000, y=450)

Button(root, text="Reset", width=19, height=2, font="arial 12 bold",
       bg="lightpink").place(x=1000, y=530)

Button(root, text="Exit", width=19, height=2, font="arial 12 bold",
       bg="grey").place(x=1000, y=610)

root.mainloop()
