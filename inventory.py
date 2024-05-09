# inventory.py
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from database import *

def inventory_window():
    def populate_tree():
        # Clear existing items in the treeview
        for item in tree.get_children():
            tree.delete(item)
        # Fetch data from the database and populate the treeview
        data = db_get_item()
        for index in data:
            tree.insert('', 'end', values=(index[0], index[1], index[2], index[3], f"${index[4]:.2f}", index[5]))

    def search_items():
        # Get the search text from the textbox_search
        search_text = textbox_search.get("1.0", "end-1c").strip().lower()  # Convert to lowercase for case-insensitive search

        # Clear existing items in the treeview
        for item in tree.get_children():
            tree.delete(item)

        # Fetch data from the database and filter based on search text
        data = db_get_item()
        for index in data:
            # Check if any column value contains the search text (case-insensitive)
            if any(search_text in str(value).lower() for value in index):
                tree.insert('', 'end', values=(index[0], index[1], index[2], index[3], f"${index[4]:.2f}", index[5]))

    def update_item():
        # Check if an item is selected
        selected_item = tree.focus()
        if not selected_item:
            showerror('Update Error', 'Please select an item to update.')
            return

        # Get item_id from the selected item in the treeview
        item_id = tree.item(selected_item, 'values')[0]  # Assuming item_id is at index 0

        # Get values from the entry widgets
        item_name = textbox_item_name.get("1.0", "end-1c")
        description = textbox_description.get("1.0", "end-1c")
        quantity = textbox_quantity_available.get("1.0", "end-1c")
        unit_price = textbox_unit_price.get("1.0", "end-1c")
        supplier = supplier_name.get()

        # Update the item in the database
        db_update_item(item_id, item_name, description, quantity, unit_price, supplier)

        # Clear text in the entry widgets
        textbox_item_name.delete("1.0", "end")
        textbox_description.delete("1.0", "end")
        textbox_quantity_available.delete("1.0", "end")
        textbox_unit_price.delete("1.0", "end")

        # Refresh the treeview
        populate_tree()
        showinfo('Update Success', 'Item updated successfully.')

    def add_item():
        # Get values from the entry widgets
        item_name = textbox_item_name.get("1.0", "end-1c").strip()
        description = textbox_description.get("1.0", "end-1c").strip()
        quantity_available_str = textbox_quantity_available.get("1.0", "end-1c").strip()
        unit_price_str = textbox_unit_price.get("1.0", "end-1c").strip()
        selected_supplier = supplier_name.get()  # Renamed the variable

        # Check if any parameter is empty
        if not all([item_name, description, quantity_available_str, unit_price_str, selected_supplier]):
            showerror('Add Error', 'Please fill in all fields.')
            return

        # Validate data types
        try:
            quantity_available = int(quantity_available_str)
            unit_price = float(unit_price_str)
        except ValueError:
            showerror('Add Error', 'Quantity and Unit Price must be numeric.')
            return

        # Get the supplier_id corresponding to the selected supplier_name
        cursor.execute('''
            SELECT supplier_id
            FROM Supplier
            WHERE supplier_name=?
        ''', (selected_supplier,))
        result = cursor.fetchone()
        if result:
            supplier_id = result[0]
        else:
            showerror('Add Error', 'Supplier not found.')
            return

        # Add the item to the database with the correct supplier_id
        db_add_item(item_name, description, quantity_available, unit_price, supplier_id)
        
        # Clear text in the entry widgets
        textbox_item_name.delete("1.0", "end")
        textbox_description.delete("1.0", "end")
        textbox_quantity_available.delete("1.0", "end")
        textbox_unit_price.delete("1.0", "end")
        
        # Refresh the treeview
        populate_tree()

        showinfo('Add Success', 'Item added successfully.')

    def delete_item():
    # Check if an item is selected
        selected_item = tree.focus()
        if not selected_item:
            showerror('Delete Error', 'Please select an item to delete.')
            return
        # Get the item_id of the selected item
        item_id = tree.item(selected_item, 'values')[0]  # Assuming item_id is in the first column
        # Delete the item from the database
        db_delete_item(item_id)
        
        # Clear text in the entry widgets
        textbox_item_name.delete("1.0", "end")
        textbox_description.delete("1.0", "end")
        textbox_quantity_available.delete("1.0", "end")
        textbox_unit_price.delete("1.0", "end")
        
        # Refresh the treeview
        populate_tree()
        showinfo('Delete Success', 'Item deleted successfully.')
    
    def show_selected_item(event):
        # Get the selected item from the treeview
        selected_item = tree.focus()
        if selected_item:
            # Get the values of the selected item
            item_values = tree.item(selected_item, 'values')
            # Update the textbox with the values
            textbox_item_name.delete('1.0', 'end')
            textbox_item_name.insert('1.0', item_values[1])  # Assuming item_name is in the second column
            textbox_description.delete('1.0', 'end')
            textbox_description.insert('1.0', item_values[2])  # Assuming description is in the third column
            textbox_quantity_available.delete('1.0', 'end')
            textbox_quantity_available.insert('1.0', item_values[3])  # Assuming quantity_available is in the fourth column
            textbox_unit_price.delete('1.0', 'end')
            textbox_unit_price.insert('1.0', item_values[4][1:])  # Assuming unit_price is in the fifth column
            supplier_name.set(item_values[5])  # Assuming supplier_name is in the sixth column
    
    #window
    inventory = Toplevel()
    #inventory = Tk() # comment this out
    inventory.title('Inventory')
    inventory.config(width=800, height=530)
    inventory.geometry('800x530')
    inventory.resizable(False, False)
    
    #group
    title_bar = Frame(inventory)
    search_bar = Frame(inventory)
    inventory_bar = Frame(inventory)
    function_bar = Frame(inventory)
    option_bar = Frame(inventory)
    
    #title
    label_title = Label(title_bar, text='Inventory', font=('', 40))
    label_title.grid(row=0, column=0, pady=10)
    
    #search
    textbox_search = Text(search_bar, height=1, width=50)
    textbox_search.grid(row=0, column=0, padx=10, pady=10)
    button_search = Button(search_bar, text='Search', command=search_items)
    button_search.grid(row=0, column=1, padx=10)
    button_back = Button(search_bar, text='Back', command=inventory.destroy)
    button_back.grid(row=0, column=2, padx=10)

    #table
    tree = Treeview(inventory_bar, columns=('item_id', 'item_name', 'description', 'quantity_available', 'unit_price', 'supplier_id'), show='headings')
    tree.heading('item_id', text="ID")
    tree.heading('item_name', text='Item Name')
    tree.heading('description', text='Description')
    tree.heading('quantity_available', text='Available')
    tree.heading('unit_price', text='Price')
    tree.heading('supplier_id', text='Supplier')
    tree.column('item_id', width=30)
    tree.column('item_name', width=150)
    tree.column('description', width=300)
    tree.column('quantity_available', width=60)
    tree.column('unit_price', width=50)
    tree.column('supplier_id', width=100)
    tree.grid(row=0, column=0, pady=20)
    tree.bind('<<TreeviewSelect>>', show_selected_item)
    
    populate_tree()
    
    #option
    option_bar1 = Frame(option_bar)
    label_item_name = Label(option_bar1, text='Item: ', anchor='e')
    label_item_name.grid(row=0, column=0, pady=5, sticky='e')
    textbox_item_name = Text(option_bar1, height=1, width=20)
    textbox_item_name.grid(row=0, column=1)
    label_description = Label(option_bar1, text='Description: ', anchor='e')
    label_description.grid(row=0, column=2, padx=(20, 0), pady=10, sticky='e')
    textbox_description = Text(option_bar1, height=1, width=40)
    textbox_description.grid(row=0, column=3)
    
    option_bar2 = Frame(option_bar)
    label_quantity_available = Label(option_bar2, text='Quantity: ', anchor='e')
    label_quantity_available.grid(row=0, column=0, sticky='e')
    textbox_quantity_available = Text(option_bar2, height=1, width=10)
    textbox_quantity_available.grid(row=0, column=1)
    label_unit_price = Label(option_bar2, text='Unit Price: ', anchor='e')
    label_unit_price.grid(row=0, column=2, pady=10, padx=(20,0), sticky='e')
    textbox_unit_price = Text(option_bar2, height=1, width=10)
    textbox_unit_price.grid(row=0, column=3)
    label_supplier = Label(option_bar2, text='Supplier: ', anchor='e')
    label_supplier.grid(row=0, column=4, padx=(20,0), sticky='e')
    supplier_name = StringVar(inventory)
    data_supplier_name = db_get_supplier_name()
    supplier_names = [name[0] for name in data_supplier_name]
    supplier_name.set("")
    dropdown_supplier = OptionMenu(option_bar2, supplier_name, *supplier_names)
    dropdown_supplier.grid(row=0, column=5)
    
    #action
    button_update = Button(function_bar, text='Update Item', command=update_item)
    button_update.grid(row=0, column=0, padx=10, pady=10)
    button_add = Button(function_bar, text='Add Item', command=add_item)
    button_add.grid(row=0, column=1,padx=10)
    button_delete = Button(function_bar, text='Delete Item', command=delete_item)
    button_delete.grid(row=0, column=2, padx=10)
    
    #display
    title_bar.pack()
    search_bar.pack()
    inventory_bar.pack()
    option_bar.pack()
    option_bar1.pack()
    option_bar2.pack()
    function_bar.pack()
    
    inventory.mainloop()
   
#inventory_window() #comment this out