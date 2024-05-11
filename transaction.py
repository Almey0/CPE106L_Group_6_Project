import datetime
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from database import *


def transaction_window():
    def populate_tree():
        # Clear existing items in the treeview
        for item in tree.get_children():
            tree.delete(item)
        # Fetch data from the database and populate the treeview
        data = db_get_transaction()
        for index in data:
            tree.insert('', 'end', values=(index[0], index[1], index[2], index[3], index[4], index[5]))

    def search_items():
    # Get the search text from the textbox_search
        search_text = textbox_search.get("1.0", "end-1c").strip().lower()

    # Clear existing items in the treeview
        for item in tree.get_children():
            tree.delete(item)

        # Fetch data from the database and filter based on search text
        data = db_get_transaction()
        for index in data:
            # Check if any column value contains the search text (case-insensitive)
            if any(search_text in str(value).lower() for value in index):
                tree.insert('', 'end', values=(index[0], index[1], index[2], index[3], index[4]))

    def update_transaction():
        selected_transaction = tree.focus()
        if not selected_transaction:
            showerror('Update Error', 'Please select a transaction to update.')
            return

        transaction_id = tree.item(selected_transaction, 'values')[0]

        item_name = combobox_item_name.get()
        supplier_name = combobox_supplier_name.get()
        quantity = int(textbox_quantity.get("1.0", "end-1c").strip())
        transaction_type = combobox_transaction_type.get()

        item_details = db_get_item_details(item_name, supplier_name)
        if item_details is None:
            showerror('Item Error', 'Item details not found.')
            return

        item_id, unit_price = item_details
        total_cost = quantity * unit_price

        db_update_transaction(transaction_id, item_id, transaction_type, quantity, total_cost)  # Corrected parameters

        populate_tree()
        showinfo('Update Success', 'Transaction updated successfully.')

    def add_transaction():
        item_name = combobox_item_name.get()
        supplier_name = combobox_supplier_name.get()
        quantity = int(textbox_quantity.get("1.0", "end-1c").strip())
        transaction_type = combobox_transaction_type.get()

        item_details = db_get_item_details(item_name, supplier_name)
        if item_details:
            item_id, unit_price = item_details
            total_cost = quantity * unit_price

            db_add_transaction(transaction_type, quantity, datetime.now(), total_cost, item_id, db_get_supplier_id(supplier_name))  # Corrected parameters

            populate_tree()
            showinfo('Add Success', 'Transaction added successfully.')
        else:
            showerror('Item Error', 'Item details not found.')

    def delete_transaction():
        selected_transaction = tree.focus()
        if not selected_transaction:
            showerror('Delete Error', 'Please select a transaction to delete.')
            return

        transaction_id = tree.item(selected_transaction, 'values')[0]

        db_delete_transaction(transaction_id)

        populate_tree()
        showinfo('Delete Success', 'Transaction deleted successfully.')

    def show_selected_transaction(event):
        selected_transaction = tree.focus()
        if selected_transaction:
            transaction_values = tree.item(selected_transaction, 'values')
            # Set the value of combobox_item_name to the selected item name
            combobox_item_name.set(transaction_values[1])
            # Set the value of combobox_supplier_name to the selected supplier name
            combobox_supplier_name.set(transaction_values[2])
            # Set the value of combobox_transaction_type to the selected transaction type
            combobox_transaction_type.set(transaction_values[3])
            # Delete the existing content in the quantity textbox and insert the selected quantity
            textbox_quantity.delete('1.0', 'end')
            textbox_quantity.insert('1.0', str(transaction_values[4]))

    # Window
    transaction = Toplevel()
    transaction.title('Transaction')
    transaction.config(width=800, height=530)
    transaction.geometry('800x530')
    transaction.resizable(False, False)

    # Group
    title_bar = Frame(transaction)
    search_bar = Frame(transaction)
    transaction_bar = Frame(transaction)
    function_bar = Frame(transaction)
    option_bar = Frame(transaction)

    # Title
    label_title = Label(title_bar, text='Transaction', font=('', 40))
    label_title.grid(row=0, column=0, pady=10)

    # Search
    textbox_search = Text(search_bar, height=1, width=50)
    textbox_search.grid(row=0, column=0, padx=10, pady=10)
    button_search = Button(search_bar, text='Search', command=search_items)
    button_search.grid(row=0, column=1, padx=10)
    button_back = Button(search_bar, text='Back', command=transaction.destroy)
    button_back.grid(row=0, column=2, padx=10)

    # Table
    tree = Treeview(transaction_bar, columns=('transaction_id', 'item_name', 'supplier_name', 'transaction_type', 'quantity', 'transaction_date', 'total_cost'), show='headings', selectmode='browse')
    tree.heading('item_name', text='Item Name')
    tree.heading('supplier_name', text='Supplier')
    tree.heading('transaction_type', text='Type')
    tree.heading('quantity', text='Quantity')
    tree.column('transaction_id', width=30)
    tree.column('item_name', width=150)
    tree.column('supplier_name', width=100)
    tree.column('transaction_type', width=70)
    tree.column('transaction_date', width=70)  # Corrected line
    tree.column('quantity', width=70)
    tree.column('total_cost', width=80, anchor='c')
    tree.heading('transaction_date', text='Date')  # Add heading for date column
    tree.heading('total_cost', text='Total Cost')
    tree.grid(row=0, column=0, pady=20)
    tree.bind('<<TreeviewSelect>>', show_selected_transaction)

    populate_tree()

    # Option
    option_bar1 = Frame(option_bar)
    label_item_name = Label(option_bar1, text='Item Name: ', anchor='e')
    label_item_name.grid(row=0, column=0, pady=5, sticky='e')
    combobox_item_name = Combobox(option_bar1, values=db_get_item_names(), height=1, width=20)
    combobox_item_name.grid(row=0, column=1)
    label_supplier_name = Label(option_bar1, text='Supplier Name: ', anchor='e')
    label_supplier_name.grid(row=0, column=2, padx=(20, 0), pady=10, sticky='e')
    combobox_supplier_name = Combobox(option_bar1, values=db_get_all_supplier_names(), height=1, width=20)
    combobox_supplier_name.grid(row=0, column=3)

    option_bar2 = Frame(option_bar)
    label_transaction_type = Label(option_bar2, text='Type: ', anchor='e')
    label_transaction_type.grid(row=0, column=0, sticky='e')
    combobox_transaction_type = Combobox(option_bar2, values=['Purchase', 'Sell'], height=1, width=10)
    combobox_transaction_type.grid(row=0, column=1)
    label_quantity = Label(option_bar2, text='Quantity: ', anchor='e')
    label_quantity.grid(row=0, column=2, pady=10, padx=(20, 0), sticky='e')
    textbox_quantity = Text(option_bar2, height=1, width=10)
    textbox_quantity.grid(row=0, column=3)

    # Action
    button_update = Button(function_bar, text='Update Transaction', command=update_transaction)
    button_update.grid(row=0, column=0, padx=10, pady=10)
    button_add = Button(function_bar, text='Add Transaction', command=add_transaction)
    button_add.grid(row=0, column=1, padx=10)
    button_delete = Button(function_bar, text='Delete Transaction', command=delete_transaction)
    button_delete.grid(row=0, column=2, padx=10)

    # Display
    title_bar.pack()
    search_bar.pack()
    transaction_bar.pack()
    option_bar1.pack()
    option_bar2.pack()
    option_bar.pack()
    function_bar.pack()

    transaction.mainloop()