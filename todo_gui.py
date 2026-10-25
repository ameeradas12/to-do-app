import tkinter as tk

window = tk.Tk()
window.title("To-do app")

# Row 1: text box + Add button, side by side
row = tk.Frame(window)
row.pack(padx=10, pady=10)

box = tk.Entry(row)
box.pack(side="left")

add = tk.Button(row, text="Add Task")
add.pack(side="left")

# The task list, directly in the window (stacks below row 1)
taskBox = tk.Listbox(window, width=40, height=8)
taskBox.pack(fill="x", padx=10)

taskBox.insert(tk.END, "First Line")
taskBox.insert(tk.END, "Second Line")

# Row 2: Mark done + Delete buttons, side by side
bottomRow = tk.Frame(window)
bottomRow.pack(padx=10, pady=10)

doneButton = tk.Button(bottomRow, text="Mark done")
doneButton.pack(side="left")

deleteButton = tk.Button(bottomRow, text="Delete")
deleteButton.pack(side="left")

window.mainloop()