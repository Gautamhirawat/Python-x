"""
Just random use of elements in the tkinter , to just learn the basic and use of each elements individually.
"""
import tkinter as tk
from tkinter import ttk, messagebox

def show_message():
    messagebox.showinfo("Message", "You clicked the button!")

def show_option():
    selected_option = var.get()
    messagebox.showinfo("Option", f"You selected: {selected_option}")

def show_options():
    options = [var1.get(), var2.get(), var3.get()]
    selected_options = [option for option, value in zip(["Option 1", "Option 2", "Option 3"], options) if value]
    messagebox.showinfo("Options", f"You selected: {', '.join(selected_options)}")

root = tk.Tk()
root.title("tkinter Demo")

# Label
label = tk.Label(root, text="Label")
label.pack()

# Button
button = tk.Button(root, text="Button", command=show_message)
button.pack()

# Entry
entry = tk.Entry(root)
entry.pack()

# Text
text = tk.Text(root)
text.pack()

# Checkboxes
var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()

checkbox1 = tk.Checkbutton(root, text="Checkbox 1", variable=var1)
checkbox2 = tk.Checkbutton(root, text="Checkbox 2", variable=var2)
checkbox3 = tk.Checkbutton(root, text="Checkbox 3", variable=var3)

checkbox1.pack()
checkbox2.pack()
checkbox3.pack()

# Radio buttons
var = tk.StringVar()

radio_button1 = tk.Radiobutton(root, text="Radio Button 1", variable=var, value="Option A", command=show_option)
radio_button2 = tk.Radiobutton(root, text="Radio Button 2", variable=var, value="Option B", command=show_option)
radio_button3 = tk.Radiobutton(root, text="Radio Button 3", variable=var, value="Option C", command=show_option)

radio_button1.pack()
radio_button2.pack()
radio_button3.pack()

# Listbox
listbox = tk.Listbox(root)
for item in ["Item 1", "Item 2", "Item 3"]:
    listbox.insert(tk.END, item)
listbox.pack()

# Scrollbar
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Canvas
canvas = tk.Canvas(root, width=200, height=100, bg="white")
canvas.pack()

# Frame
frame = tk.Frame(root, borderwidth=2, relief=tk.GROOVE)
frame.pack()

# Menu
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Scale
scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
scale.pack()

# Spinbox
spinbox = tk.Spinbox(root, from_=0, to=10)
spinbox.pack()

# PanedWindow
paned_window = tk.PanedWindow(root, orient=tk.HORIZONTAL)
paned_window.pack()

# Toplevel
top_level = tk.Toplevel(root)
top_level.title("Top Level Window")
top_label = tk.Label(top_level, text="Top Level Window")
top_label.pack()

# Message
message = tk.Message(root, text="This is a message widget")
message.pack()

# LabelFrame
label_frame = tk.LabelFrame(root, text="Label Frame")
label_frame.pack()

# Progressbar (using ttk module)
progressbar = ttk.Progressbar(root, orient=tk.HORIZONTAL, length=200, mode='indeterminate')
progressbar.pack()



# Treeview
tree = ttk.Treeview(root)
tree.insert("", tk.END, text="Item 1")
tree.insert("", tk.END, text="Item 2")
tree.pack()

# OptionMenu
option_menu_var = tk.StringVar()
option_menu_var.set("Option 1")
option_menu = tk.OptionMenu(root, option_menu_var, "Option 1", "Option 2", "Option 3")
option_menu.pack()

root.mainloop()
