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


# ################ image upload function, opens file window and replaces image
def showimage():
    global filename
    global img
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title="Select Image File", filetype=(("JPG File", "*.jpg"),("PNG File", "*.png"),("All files", "*.txt"))) # this code was origionally contained in the image file bit
    img = (Image.open(filename))
    resized_image = img.resize((190, 190))
    photo2 = ImageTk.PhotoImage(resized_image)
    lbl.config(image=photo2)
    lbl.image = photo2


# ################ Clear
# ################ Clear
def Clear():
    global img
    CatNum.set('')
    DDate.set('')
    Species.set('')
    Nickname.set('')
    EstimatedP.set('')
    Taxonomy.set('')
    Details.set('')
    Traits.set('')
    Condition.set("Select Condition")

    img1 = PhotoImage(file='Images/no_img.png')
    lbl.config(image=img1)
    lbl.image = img1

    img = ""

    # Clear radio selection
    radio.set(0)

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

# image
f = Frame(root, bd=3, bg="black", width=200, height=200, relief=GROOVE)
f.place(x=1000, y=150)

img = PhotoImage(file="Images/no_img.png")
lbl = Label(f, bg="black", image=img)
lbl.place(x=0, y=0)

# buttons for image
Button(root, text="Upload", width=19, height=2, font="arial 12 bold",
       bg="lightblue", command=showimage).place(x=1000, y=370)

Button(root, text="Reset", width=19, height=2, font="arial 12 bold",
       bg="lightpink", command=Clear).place(x=1000, y=530)

root.mainloop()
