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

# Function to display help information
def display_help():
    # Create a new Toplevel window for help
    help_window = Toplevel(root)
    help_window.title("Help")
    help_window.config(bg=background)

    help_info = "The Fossil Registration System is a user-friendly application designed to " \
                "manage and track information about fossils. To begin, users can either search " \
                "for existing fossil records using the 'Search' button by entering the registration " \
                "number or start fresh by filling in the details of a new fossil. When entering " \
                "data for a new fossil, users need to provide information such as the catalogue number," \
                " species, discovery date, dietary classification, condition, nickname, estimated period," \
                " taxonomy, and additional details. Users can also upload an image of the fossil. " \
                "The 'Save' button stores the entered data in an Excel file, and the 'Update File' " \
                "button allows users to modify existing records. The 'Clear' button resets the input " \
                "fields for entering new data. For assistance, users can click the 'Help' button, " \
                "which opens a window with helpful information. " \
                "" \
                "Avoid using special characters for the catalogue number as this may cause errors with the images"

    # Add heading
    heading = Label(help_window, text="Help", font="arial 20 bold", bg=background, fg="white")
    heading.pack(pady=10)

    # Adjust font size and wrap length based on the width of the text
    wrap_length = 500  # Adjust this value as needed
    font_size = 12  # Adjust this value as needed

    # Add help text
    help_text = Label(help_window, text=help_info,
                      font=f"arial {font_size}", bg=background, fg="white", wraplength=wrap_length)
    help_text.pack(padx=20, pady=20)

    # Calculate the height needed for the window based on the text size
    text_height = help_text.winfo_reqheight() + heading.winfo_reqheight() + 40  # Additional padding

    # Adjust the window's height to fit the text
    help_window.geometry(f"{wrap_length+40}x{text_height+40}")

# Button for help
help_button = Button(root, text="Help", bg="#68ddfa", font="arial 13 bold", pady=6, width=10, command=display_help)
help_button.place(x=250, y=64)

root.mainloop()