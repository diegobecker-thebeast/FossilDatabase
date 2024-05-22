from tkinter import *
from datetime import date
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from tkinter.ttk import Combobox
import openpyxl, xlrd
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
root.geometry("1250x700+210+100")
root.config(bg=background)

file = pathlib.Path('Fossil_Data.xlsx')
if file.exists():
    pass
else:
    file = Workbook()
    sheet = file.active
    sheet['A1'] = "Registration No."
    sheet['B1'] = "Catalogue Number"
    sheet['C1'] = "Continent"
    sheet['D1'] = "Copy"
    sheet['E1'] = "Date Discovered"
    sheet['F1'] = "Date of Registration"
    sheet['G1'] = "Nickname"
    sheet['H1'] = "Species Type"

    file.save('Fossil_Data.xlsx')

root.mainloop()
