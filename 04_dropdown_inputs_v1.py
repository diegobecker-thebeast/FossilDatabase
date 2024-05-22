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

file = pathlib.Path('Fossil_Data.xlsx')
if file.exists():
    pass
else:
    file = Workbook()
    sheet = file.active
    sheet['A1'] = "Registration Number"
    sheet['B1'] = "Catalogue Number"
    sheet['C1'] = "Species"
    sheet['D1'] = "Date Discovered"
    sheet['E1'] = "Date Registered"
    sheet['F1'] = "Condition"
    sheet['G1'] = "Diet"
    sheet['H1'] = "Nickname"
    sheet['I1'] = "Estimated Period"
    sheet['J1'] = "Taxonomy"
    sheet['K1'] = "Additional Details"
    sheet['L1'] = "Traits"

    file.save('Fossil_Data.xlsx')


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

    # print(Diet)  # testing purposes


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

# Button for help
help_button = Button(root, text="Help", bg="#68ddfa", font="arial 13 bold", pady=6, width=10)
help_button.place(x=250, y=64)

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

today = date.today()
d1 = today.strftime("%d/%m/%Y")
date_entry = Entry(root, textvariable=Date, width=15, font="arial 10")
date_entry.place(x=550, y=150)
date_entry.config(state='readonly')

Date.set(d1)

# Fossil details
###########
obj = LabelFrame(root, text="Fossil Details", font=20, bd=2, width=900,
                 bg=framebg, fg=framefg, height=250, relief=GROOVE)
obj.place(x=30, y=200)

Label(obj, text="Catalogue Number:", font="arial 13", bg=framebg, fg=framefg).place(x=30, y=50)
Label(obj, text="Discovery Date:", font="arial 13", bg=framebg, fg=framefg).place(x=30, y=100)
Label(obj, text="Dietary Classification:", font="arial 13", bg=framebg, fg=framefg).place(x=30, y=150)

Label(obj, text="Species:", font="arial 13", bg=framebg, fg=framefg).place(x=500, y=50)
Label(obj, text="Condition:", font="arial 13", bg=framebg, fg=framefg).place(x=500, y=100)
Label(obj, text="Nickname", font="arial 13", bg=framebg, fg=framefg).place(x=500, y=150)

# input box for catalogue number
CatNum = StringVar()
cat_entry = Entry(obj, textvariable=CatNum, width=20, font="arial 10")
cat_entry.place(x=200, y=50)

# input box for date discovered -
DDate = StringVar()
ddate_entry = Entry(obj, textvariable=DDate, width=20, font="arial 10")
ddate_entry.place(x=200, y=100)

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

# dropdown for condition
Condition = Combobox(obj, values=['Excellent', 'Good', 'Fair', 'Poor', 'Bad', 'Ruined'],
                     font="Roboto", width=17, state="r")
Condition.place(x=630, y=100)
Condition.set("Select Condition")

# input box for species
Species = StringVar()
species_entry = Entry(obj, textvariable=Species, width=20, font="arial 10")
species_entry.place(x=630, y=50)

# input box for nickname
Nickname = StringVar()
nickname_entry = Entry(obj, textvariable=Nickname, width=20, font="arial 10")
nickname_entry.place(x=630, y=150)

#####

# additional details
#########
obj2 = LabelFrame(root, text="Additional Details", font=20, bd=2, width=900,
                  bg=framebg, fg=framefg, height=250, relief=GROOVE)
obj2.place(x=30, y=470)

Label(obj2, text="Estimated Period:", font="arial 13", bg=framebg, fg=framefg).place(x=30, y=50)
EstimatedP = StringVar()
ep_entry = Entry(obj2, textvariable=EstimatedP, width=20, font="arial 10")
ep_entry.place(x=200, y=50)

Label(obj2, text="Details of Fossil Condition:", font="arial 13", bg=framebg, fg=framefg).place(x=30, y=100)
Details = StringVar()
details_entry = Entry(obj2, textvariable=Details, width=50, font="arial 10")
details_entry.place(x=30, y=150)

Label(obj2, text="Genus:", font="arial 13", bg=framebg, fg=framefg).place(x=500, y=50)
Taxonomy = StringVar()
tax_entry = Entry(obj2, textvariable=Taxonomy, width=20, font="arial 10")
tax_entry.place(x=630, y=50)

Label(obj2, text="Distinguishable Phenotypes:", font="arial 13", bg=framebg, fg=framefg).place(x=500, y=100)
Traits = StringVar()
traits_entry = Entry(obj2, textvariable=Traits, width=50, font="arial 10")
traits_entry.place(x=500, y=150)
######


root.mainloop()
