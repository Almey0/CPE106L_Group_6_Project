# transaction.py
from tkinter import *
from tkinter.ttk import *
from database import *

def transaction_window():
    def populate_tree():
        data = db_get_transaction()
        for index in data:
            tree.insert('', 'end', values=(index[0], index[1], index[2], index[3], index[4], index[5], index[6]))
    
    #def add_transaction():
    
    #def update_transaction():
    
    #def add_transaction():
    
    transaction = Toplevel()
    transaction.title('transaction')
    transaction.config(width=800, height=530)
    transaction.geometry('800x530')
    transaction.resizable(False, False)
    
    title_bar = Frame(transaction)
    search_bar = Frame(transaction)
    transaction_bar = Frame(transaction)
    function_bar = Frame(transaction)
    option_bar = Frame(transaction)
    
    
    label_title = Label(title_bar, text='Transaction', font=('', 40))
    label_title.grid(row=0, column=0, pady=10)
    
    textbox_search = Text(search_bar, height=1, width=50)
    textbox_search.grid(row=0, column=0, padx=10, pady=10)
    
    button_search = Button(search_bar, text='Search')
    button_search.grid(row=0, column=1, padx=10)
    
    button_back = Button(search_bar, text='Back', command=transaction.destroy)
    button_back.grid(row=0, column=2, padx=10)

    tree = Treeview(transaction_bar, columns=('transaction_id', 'item_name', 'supplier_name', 'transaction_type', 'quantity', 'transaction_date', 'total_cost'), show='headings', selectmode='browse')
    tree.heading('transaction_id', text="ID")
    tree.heading('item_name', text='Item')
    tree.heading('supplier_name', text='Supplier')
    tree.heading('transaction_type', text='Type')
    tree.heading('quantity', text='Quantity')
    tree.heading('transaction_date', text='Date')
    tree.heading('total_cost', text='Total Cost')
    tree.column('transaction_id', width=30)
    tree.column('item_name', width=150)
    tree.column('supplier_name', width=100)
    tree.column('transaction_type', width=70)
    tree.column('quantity', width=70)
    tree.column('transaction_date', width=80, anchor='c')
    tree.column('total_cost', width=80)
    tree.grid(row=0, column=0, pady=20)
    
    populate_tree()
    
    button_update = Button(function_bar, text='Update Transaction')
    button_update.grid(row=0, column=0, padx=10)
    button_add = Button(function_bar, text='Add Transaction')
    button_add.grid(row=0, column=1,padx=10)
    button_delete = Button(function_bar, text='Delete Transaction')
    button_delete.grid(row=0, column=2, padx=10)
    
    option_bar1 = Frame(option_bar)
    label_item_name = Label(option_bar1, text='Item Name: ', anchor='e')
    label_item_name.grid(row=0, column=0, pady=5, sticky='e')
    textbox_item_name = Text(option_bar1, height=1, width=20)
    textbox_item_name.grid(row=0, column=1)
    label_supplier_name = Label(option_bar1, text='Supplier Name: ', anchor='e')
    label_supplier_name.grid(row=0, column=2, padx=(20, 0), pady=10, sticky='e')
    textbox_supplier_name = Text(option_bar1, height=1, width=20)
    
    option_bar2 = Frame(option_bar)
    textbox_supplier_name.grid(row=0, column=3)
    label_transaction_type = Label(option_bar2, text='Type: ', anchor='e')
    label_transaction_type.grid(row=0, column=0, sticky='e')
    textbox_transaction_type = Combobox(option_bar2, height=1, width=10)
    textbox_transaction_type.grid(row=0, column=1)
    label_quantity = Label(option_bar2, text='Quantity: ', anchor='e')
    label_quantity.grid(row=0, column=2, pady=10, padx=(20,0), sticky='e')
    textbox_quantity = Text(option_bar2, height=1, width=10)
    textbox_quantity.grid(row=0, column=3)
    
    
    
    title_bar.pack()
    search_bar.pack()
    transaction_bar.pack()
    function_bar.pack()
    option_bar.pack()
    option_bar1.pack()
    option_bar2.pack()
    
    transaction.mainloop()
    
#transaction_window() # comment this out
