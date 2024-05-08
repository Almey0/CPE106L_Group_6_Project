import tkinter as tk
from tkinter import ttk

def update_textbox(event):
    # Get the selected item from the treeview
    item = tree.selection()[0]
    # Get the values from the selected item's columns
    name = tree.item(item, "values")[0]
    age = tree.item(item, "values")[1]
    birthday = tree.item(item, "values")[2]
    # Update the textbox with the selected item's values
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    birthday_entry.delete(0, tk.END)
    name_entry.insert(0, name)
    age_entry.insert(0, age)
    birthday_entry.insert(0, birthday)

def add_entry():
    # Get values from entry fields
    name = name_entry.get()
    age = age_entry.get()
    birthday = birthday_entry.get()
    # Insert new entry into Treeview
    tree.insert("", "end", values=(name, age, birthday))
    # Clear entry fields
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    birthday_entry.delete(0, tk.END)

def update_entry():
    # Get the selected item from the treeview
    item = tree.selection()[0]
    # Update values of the selected item
    tree.item(item, values=(name_entry.get(), age_entry.get(), birthday_entry.get()))

# Create the tkinter window
window = tk.Tk()
window.title("TreeView and TextBox Example")

# Create a Treeview widget with columns
tree = ttk.Treeview(window, columns=("Name", "Age", "Birthday"), show="headings")
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.heading("Birthday", text="Birthday")
tree.pack()

# Bind the update_textbox function to the treeview's selection event
tree.bind("<<TreeviewSelect>>", update_textbox)

# Create entry fields for adding or updating entries
name_entry = tk.Entry(window)
name_entry.pack()
age_entry = tk.Entry(window)
age_entry.pack()
birthday_entry = tk.Entry(window)
birthday_entry.pack()

# Create Add and Update buttons
add_button = tk.Button(window, text="Add", command=add_entry)
add_button.pack()
update_button = tk.Button(window, text="Update", command=update_entry)
update_button.pack()

# Run the tkinter event loop
window.mainloop()
