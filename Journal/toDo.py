import tkinter
from tkinter import *

root = Tk()
root.title("To do List")
root.geometry("400x650+400+100")

task_list = []

def deleteTask():
    global task_list

    task = str(listbox.get(ANCHOR))  # ANCHOR is correct here
    if task in task_list:
        task_list.remove(task)
        with open("taskList.txt", 'w') as taskfile:
            for task in task_list:
                taskfile.write(task + "\n")  # Corrected 'taskfie' typo
        listbox.delete(ANCHOR)

def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)
    # I want to store this in
    if task:
        with open("taskList.txt", 'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END, task)

def openTaskFile():
    try:
        global task_list  # 'global' is necessary to modify task_list
        with open("taskList.txt", "r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task != '\n':
                task_list.append(task.strip())  # Remove unnecessary newlines
                listbox.insert(END, task.strip())
    except FileNotFoundError:
        file = open('taskList.txt', "w")  # Create file if not exists
        file.close()

# icon
Image_icon = PhotoImage(file="task.png")
root.iconphoto(False, Image_icon)

# top bar
TopImage = PhotoImage(file="topbar.png")
Label(root, image=TopImage).pack()

# Dock
dockImage = PhotoImage(file="dock.png")
Label(root, image=dockImage, bg="#32405b").place(x=30, y=25)

# label
noteImage = PhotoImage(file="task.png")
Label(root, image=noteImage, bg="#32405b").place(x=30, y=25)

# heading
heading = Label(root, text="ALL TASK", font="arial 20 bold", fg="white", bg="#32405b")
heading.place(x=130, y=20)

# main
frame = Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=180)

# text entry
task = StringVar()
task_entry = Entry(frame, width=18, font="arial 20", bd=0)
task_entry.place(x=10, y=200)
task_entry.focus()


# how can i store this entry to csv

# Button
button = Button(frame, text="ADD", font="arial 20 bold", width=6, bg="#5a95ff", fg="#fff", bd=0, command=addTask)
button.place(x=300, y=0)

# listbox
frame1 = Frame(root, bd=3, width=700, height=280, bg="#32405b")
frame1.pack(pady=(160, 0))

listbox = Listbox(frame1, font=('arial', 12), width=40, height=16, bg="#32405b", cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)

scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# open task file
openTaskFile()

# delete button
Delete_icon = PhotoImage(file="delete.png")
Button(root, image=Delete_icon, bd=0, command=deleteTask).pack(side=BOTTOM, pady=13)

root.mainloop()
