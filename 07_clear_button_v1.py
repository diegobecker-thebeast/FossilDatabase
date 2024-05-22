from tkinter import *

background = "#06283D"
framebg = "#EDEDED"
framefg = "#06283D"

root = Tk()
root.title("Fossil Registration System")
root.geometry("1250x740+210+100")
root.config(bg=background)

# Initialize variables
CatNum = "1"
DDate = "2"
Species = "3"
Nickname = "4"
EstimatedP = "5"
Taxonomy = "6"
Details = "7"
Traits = "8"
Condition = "9"

# Clear function
def Clear():
    global CatNum, DDate, Species, Nickname, EstimatedP, Taxonomy, Details, Traits, Condition
    CatNum = "2"
    DDate = "2"
    Species = "2"
    Nickname = "2"
    EstimatedP = "2"
    Taxonomy = "2"
    Details = "2"
    Traits = "2"
    Condition = "2"

# Print function
def Print():
    print(CatNum)
    print(DDate)
    print(Species)
    print(Nickname)
    print(EstimatedP)
    print(Taxonomy)
    print(Details)
    print(Traits)
    print(Condition)

# Button to print values
saveButton = Button(root, text="Print", width=19, height=2,
                    font="arial 12 bold", bg="lightgreen", command=Print)
saveButton.place(x=1000, y=450)

# Button to reset values
Button(root, text="Reset", width=19, height=2, font="arial 12 bold",
       bg="lightpink", command=Clear).place(x=1000, y=530)

root.mainloop()