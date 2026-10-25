import tkinter as tk
from todo import toDoList, saver
window = tk.Tk()
window.title("To-do app")

todo = toDoList()
saved = saver()

def refresh():
    taskBox.delete(0,tk.END)
    for task in todo.tasks:
        if task["done"]:
            taskBox.insert(tk.END, f"[x] {task['name']}")
        else:
            taskBox.insert(tk.END, f"[] {task['name']}")

def addClicked():
    taskName = box.get()
    if taskName.strip() == "": return
    todo.addTask(taskName)
    saved.save(todo.tasks)
    box.delete(0,tk.END)
    refresh()

def markDone():
    task = taskBox.curselection()
    if not task: return
    index = task[0]
    name = todo.tasks[index]["name"]
    todo.markTaskDone(name)
    saved.save(todo.tasks)
    refresh()

def deleteBox():
    task = taskBox.curselection()
    if not task: return
    index = task[0]
    name = todo.tasks[index]["name"]
    todo.removeTask(name)
    saved.save(todo.tasks)
    refresh()

row = tk.Frame(window)
row.pack(padx=10, pady=10)

box = tk.Entry(row)
box.pack(side="left")

add = tk.Button(row, text="Add Task")
add.pack(side="left")
add.config(command=addClicked)

taskBox = tk.Listbox(window, width=40, height=8)
taskBox.pack(fill="x", padx=10)


bottomRow = tk.Frame(window)
bottomRow.pack(padx=10, pady=10)

doneButton = tk.Button(bottomRow, text="Mark done")
doneButton.pack(side="left")
doneButton.config(command=markDone)

deleteButton = tk.Button(bottomRow, text="Delete")
deleteButton.pack(side="left")
deleteButton.config(command=deleteBox)

refresh()
window.mainloop()