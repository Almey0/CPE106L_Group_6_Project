# supplier.py
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from database import *

def supplier_window():
   
    def populate_tree():
        # Delete all items in the treeview
        tree.delete(*tree.get_children())

        # Populate the treeview with new data
        data = db_get_supplier()
        for index in data:
            tree.insert('', 'end', 
                        values=(index[0], index[1], index[2], index[3], index[4]))

    def add_supplier():
        supplier_name = textbox_supplier_name.get("1.0", "end-1c").strip()
        contact_person = textbox_contact_person.get("1.0", "end-1c").strip()
        contact_number = textbox_contact_number.get("1.0", "end-1c").strip()
        email = textbox_email.get("1.0", "end-1c").strip()

        # Validate if all fields are filled
        if not all([supplier_name, contact_person, contact_number, email]):
            showerror('Add Error', 'Please fill in all fields.')
            return

        # Add supplier to the database
        db_add_supplier(supplier_name, contact_person, contact_number, email)

        # Clear entry fields
        textbox_supplier_name.delete("1.0", "end")
        textbox_contact_person.delete("1.0", "end")
        textbox_contact_number.delete("1.0", "end")
        textbox_email.delete("1.0", "end")

        # Refresh treeview
        populate_tree()
        showinfo('Add Success', 'Supplier added successfully.')

    def update_supplier():
        # Get selected supplier
        selected_supplier = tree.focus()
        if not selected_supplier:
            showerror('Update Error', 'Please select a supplier to update.')
            return

        # Get supplier ID
        supplier_id = tree.item(selected_supplier, 'values')[0]

        supplier_name = textbox_supplier_name.get("1.0", "end-1c").strip()
        contact_person = textbox_contact_person.get("1.0", "end-1c").strip()
        contact_number = textbox_contact_number.get("1.0", "end-1c").strip()
        email = textbox_email.get("1.0", "end-1c").strip()

        # Update supplier in the database
        db_update_supplier(supplier_id, supplier_name, contact_person, contact_number, email)

        # Clear entry fields
        textbox_supplier_name.delete("1.0", "end")
        textbox_contact_person.delete("1.0", "end")
        textbox_contact_number.delete("1.0", "end")
        textbox_email.delete("1.0", "end")

        # Refresh treeview
        populate_tree()
        showinfo('Update Success', 'Supplier updated successfully.')

    def delete_supplier():
        # Get selected supplier
        selected_supplier = tree.focus()
        if not selected_supplier:
            showerror('Delete Error', 'Please select a supplier to delete.')
            return

        # Get supplier ID
        supplier_id = tree.item(selected_supplier, 'values')[0]

        # Delete supplier from the database
        db_delete_supplier(supplier_id)

        # Refresh treeview
        populate_tree()
        showinfo('Delete Success', 'Supplier deleted successfully.')

    def show_selected_supplier(event):
        selected_supplier = tree.focus()
        if selected_supplier:
            supplier_values = tree.item(selected_supplier, 'values')
            textbox_supplier_name.delete('1.0', 'end')
            textbox_supplier_name.insert('1.0', supplier_values[1])
            textbox_contact_person.delete('1.0', 'end')
            textbox_contact_person.insert('1.0', supplier_values[2])
            textbox_contact_number.delete('1.0', 'end')
            textbox_contact_number.insert('1.0', supplier_values[3])
            textbox_email.delete('1.0', 'end')
            textbox_email.insert('1.0', supplier_values[4])

    # Window
    supplier = Toplevel()
    supplier.title('Supplier')
    supplier.config(width=800, height=530)
    supplier.geometry('800x530')
    supplier.resizable(False, False)

    # Group
    title_bar = Frame(supplier)
    search_bar = Frame(supplier)
    supplier_bar = Frame(supplier)
    function_bar = Frame(supplier)
    option_bar = Frame(supplier)

    # Title
    label_title = Label(title_bar, text='Supplier', font=('', 40))
    label_title.grid(row=0, column=0, pady=10)

    # Search
    textbox_search = Text(search_bar, height=1, width=50)
    textbox_search.grid(row=0, column=0, padx=10, pady=10)
    button_search = Button(search_bar, text='Search')
    button_search.grid(row=0, column=1, padx=10)
    button_back = Button(search_bar, text='Back', command=supplier.destroy)
    button_back.grid(row=0, column=2, padx=10)

    # Table
    tree = Treeview(supplier_bar, columns=('supplier_id', 'supplier_name', 'contact_person', 'contact_number', 'email'), show='headings')
    tree.heading('supplier_id', text="ID")
    tree.heading('supplier_name', text='Supplier Name')
    tree.heading('contact_person', text='Contact Person')
    tree.heading('contact_number', text='Contact Number')
    tree.heading('email', text='Email')
    tree.column('supplier_id', width=30)
    tree.column('supplier_name', width=150)
    tree.column('contact_person', width=150)
    tree.column('contact_number', width=120)
    tree.column('email', width=200)
    tree.grid(row=0, column=0, pady=20)
    tree.bind('<<TreeviewSelect>>', show_selected_supplier)

    populate_tree()

    # Option
    option_bar1 = Frame(option_bar)
    label_supplier_name = Label(option_bar1, text='Supplier Name: ', anchor='e')
    label_supplier_name.grid(row=0, column=0, pady=5, sticky='e')
    textbox_supplier_name = Text(option_bar1, height=1, width=20)
    textbox_supplier_name.grid(row=0, column=1)
    label_contact_person = Label(option_bar1, text='Contact Person: ', anchor='e')
    label_contact_person.grid(row=0, column=2, padx=(20, 0), pady=10, sticky='e')
    textbox_contact_person = Text(option_bar1, height=1, width=20)
    textbox_contact_person.grid(row=0, column=3)

    option_bar2 = Frame(option_bar)
    label_contact_number = Label(option_bar2, text='Contact Number: ', anchor='e')
    label_contact_number.grid(row=0, column=0, sticky='e')
    textbox_contact_number = Text(option_bar2, height=1, width=20)
    textbox_contact_number.grid(row=0, column=1)
    label_email = Label(option_bar2, text='Email: ', anchor='e')
    label_email.grid(row=0, column=2, pady=10, padx=(20, 0), sticky='e')
    textbox_email = Text(option_bar2, height=1, width=35)
    textbox_email.grid(row=0, column=3)

# Add the show_selected_supplier function here
    def show_selected_supplier(event):
        selected_supplier = tree.focus()
        if selected_supplier:
            supplier_values = tree.item(selected_supplier, 'values')
            textbox_supplier_name.delete('1.0', 'end')
            textbox_supplier_name.insert('1.0', supplier_values[1])
            textbox_contact_person.delete('1.0', 'end')
            textbox_contact_person.insert('1.0', supplier_values[2])
            textbox_contact_number.delete('1.0', 'end')
            textbox_contact_number.insert('1.0', supplier_values[3])
            textbox_email.delete('1.0', 'end')
            textbox_email.insert('1.0', supplier_values[4])

    # Action
    button_update = Button(function_bar, text='Update Supplier', command=update_supplier)
    button_update.grid(row=0, column=0, padx=10, pady=10)
    button_add = Button(function_bar, text='Add Supplier', command=add_supplier)
    button_add.grid(row=0, column=1, padx=10)
    button_delete = Button(function_bar, text='Delete Supplier', command=delete_supplier)
    button_delete.grid(row=0, column=2, padx=10)

    # Display
    title_bar.pack()
    search_bar.pack()
    supplier_bar.pack()
    option_bar.pack()
    option_bar1.pack()
    option_bar2.pack()
    function_bar.pack()

    supplier.mainloop()
    
