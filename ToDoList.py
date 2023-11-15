import tkinter as tk
from tkinter import *

def add_task():
    task_text = task.get()
    if task_text:
        task_list.append(task_text)
        task_entry.delete(0, END)
        update_task_list()

def delete_task():
    selected_task = listbox.curselection()
    if selected_task:
        index = int(selected_task[0])
        del task_list[index]
        update_task_list()

def update_task_list():
    listbox.delete(0, END)
    for task in task_list:
        listbox.insert(END, task)

root = Tk()
root.title("To-Do-List")
root.geometry("400x450+400+100")
root.resizable(False, False)

task_list = []

frame = Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=0)

task = StringVar()
task_entry = Entry(frame, textvariable=task, width=18, font="arial 20", bd=0)
task_entry.place(x=10, y=5)

add_button = Button(root, text="ADD TASK", font="arial 10 bold", width=20, bg="Cornflower Blue", fg="white", bd=0, command=add_task)
add_button.place(x=115, y=100)

frame1 = Frame(root, width=450, height=200, bg="Light Green")
frame1.place(x=60, y=150)

listbox = Listbox(frame1, selectbackground="yellow", selectmode=SINGLE, height=8, width=45, bg="Light Green")
listbox.pack(side=LEFT)

delete_button = Button(root, text="DELETE TASK", font="arial 10 bold", width=20, bg="Cornflower Blue", fg="white", bd=0, command=delete_task)
delete_button.place(x=115, y=375)

root.mainloop()
