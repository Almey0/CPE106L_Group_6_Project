# supplier.py
from tkinter import *
from tkinter.ttk import *
from database import *

def supplier_window():
    def populate_tree():
        data = db_get_supplier()
        for index in data:
            tree.insert('', 'end', 
                        values=(index[0], index[1], index[2], index[3], index[4]))
    
    #def add_supplier():
    
    #def update_supplier():
    
    #def add_supplier():
    
    
    supplier = Toplevel()
    supplier.title('Supplier')
    supplier.config(width=800, height=500)
    supplier.geometry('800x500')
    supplier.resizable(False, False)
    
    title_bar = Frame(supplier)
    search_bar = Frame(supplier)
    supplier_bar = Frame(supplier)
    function_bar = Frame(supplier)
    
    label_title = Label(title_bar, text='Supplier', font=('', 40))
    label_title.grid(row=0, column=0, pady=10)
    
    textbox_search = Text(search_bar, height=1, width=50)
    textbox_search.grid(row=0, column=0, padx=10, pady=10)
    
    button_search = Button(search_bar, text='Search')
    button_search.grid(row=0, column=1, padx=10)
    
    button_back = Button(search_bar, text='Back', command=supplier.destroy)
    button_back.grid(row=0, column=2, padx=10)

    tree = Treeview(supplier_bar, columns=('supplier_id', 'supplier_name', 'contact_person', 'contact_number', 'email'), show='headings', selectmode='browse')
    tree.heading('supplier_id', text="ID")
    tree.heading('supplier_name', text='Supplier Name')
    tree.heading('contact_person', text='Contact Person')
    tree.heading('contact_number', text='Contact Number')
    tree.heading('email', text='Email')
    tree.column('supplier_id', width=30)
    tree.column('supplier_name', width=100)
    tree.column('contact_person', width=100)
    tree.column('contact_number', width=100)
    tree.column('email', width=150)
    tree.grid(row=0, column=0, pady=20)
    
    populate_tree()
    
    button_update = Button(function_bar, text='Update Supplier')
    button_update.grid(row=0, column=0, padx=10)
    button_add = Button(function_bar, text='Add Supplier')
    button_add.grid(row=0, column=1,padx=10)
    button_delete = Button(function_bar, text='Delete Supplier')
    button_delete.grid(row=0, column=2, padx=10)
    
    title_bar.pack()
    search_bar.pack()
    supplier_bar.pack()
    function_bar.pack()
    
    supplier.mainloop()
    
supplier_window()
