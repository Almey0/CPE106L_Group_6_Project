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
        # Populate the treeview with updated data
        data = db_get_item()
        #for index in data:
            #tree.insert('', 'end', values=(index[0], index[1], index[2], index[3], f"${index[4]:.2f}", index[5]))
    def displayAll():
        tree.delete(*tree.get_children())
        for row in db_get_item():
            tree.insert("", END, values=row)
        
            

    def update_textbox_values(event):
        # Get the selected item from the treeview
        selected_item = tree.focus()
        if not selected_item:
            return
        # Get the values of the selected item
        item_name = tree.item(selected_item, "values")[1]
        description = tree.item(selected_item, "values")[2]
        quantity_available = tree.item(selected_item, "values")[3]
        unit_price = tree.item(selected_item, "values")[4][1:]  # Remove "$" from the price
        supplier = tree.item(selected_item, "values")[5]
        # Update the textboxes with the selected item's values
        textbox_item_name.delete("1.0", "end")
        textbox_item_name.insert("1.0", item_name)
        textbox_description.delete("1.0", "end")
        textbox_description.insert("1.0", description)
        textbox_quantity_available.delete("1.0", "end")
        textbox_quantity_available.insert("1.0", quantity_available)
        textbox_unit_price.delete("1.0", "end")
        textbox_unit_price.insert("1.0", unit_price)
        supplier_name.set(supplier)
    
    def update_item():
        # Check if an item is selected
        selected_item = tree.focus()
        if not selected_item:
            showerror('Update Error', 'Please select an item to update.')
            return
        # Get values from the entry widgets
        item_name = textbox_item_name.get("1.0", "end-1c")
        description = textbox_description.get("1.0", "end-1c")
        quantity_available = textbox_quantity_available.get("1.0", "end-1c")
        unit_price = textbox_unit_price.get("1.0", "end-1c")
        supplier = supplier_name.get()
        # Update the item in the database
        db_update_item(selected_item, item_name, description, quantity_available, unit_price, supplier)
        # Refresh the treeview
        populate_tree()
        displayAll()
        showinfo('Update Success', 'Item updated successfully.')
    
        def populate_tree():
            tree.delete(*tree.get_children())
            updated_data = db_fetch_updated_data()
            for item in updated_data:
                tree.insert('', 'end', values=item)
                tree.update()  # or tree.update() if updating just the treeview



    def add_item():
        # Get values from the entry widgets
        item_name = textbox_item_name.get("1.0", "end-1c")
        description = textbox_description.get("1.0", "end-1c")
        quantity = textbox_quantity_available.get("1.0", "end-1c")
        unit_price = textbox_unit_price.get("1.0", "end-1c")
        supplier = supplier_name.get()
        # Add the item to the database
        db_add_item(item_name, description, quantity, unit_price, supplier)
        # Refresh the treeview
        populate_tree()
        displayAll()
        showinfo('Add Success', 'Item added successfully.')

    def delete_item():
        # Check if an item is selected
        selected_item = tree.focus()
        if not selected_item:
            showerror('Delete Error', 'Please select an item to delete.')
            return
        # Delete the item from the database
        db_delete_item(selected_item)
        # Refresh the treeview
        populate_tree()
        displayAll()
        showinfo('Delete Success', 'Item deleted successfully.')
    
    #window
    inventory = Toplevel()
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
    button_search = Button(search_bar, text='Search')
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
    tree.delete(*tree.get_children())  # Clear existing items
    populate_tree()
    tree.grid(row=0, column=0, pady=20)
    displayAll()
    
    populate_tree()
    
    tree.bind("<<TreeviewSelect>>", update_textbox_values)
    
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
   
inventory_window() #comment this out
