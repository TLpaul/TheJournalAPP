import tkinter
from tkinter import *



#root
root = Tk()
root.title("Journal")
root.geometry("450x600+400+100")

# Function
# Function to center the label
def center_label():
    # Update the label's x-coordinate based on the current width of the window
    window_width = root.winfo_width()
    label_width = heading.winfo_reqwidth()
    x_position = (window_width - label_width) // 2
    heading.place(x=x_position, y=15)



#Design

# icon
Image_icon = PhotoImage(file="Pencil.png")
root.iconphoto(False, Image_icon)

# top bar
Background = PhotoImage(file="background.png")
Label(root, image=Background).pack()

# heading
heading = Label(root, text="Welcome", font="arial 20 bold", fg="#4B4B4B", bg="#ADD8E6" )
heading.place(x=0, y=15)
root.after(100,center_label)


# root
root.mainloop()
#