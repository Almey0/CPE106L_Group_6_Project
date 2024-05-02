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
    supplier.config(width=800, height=530)
    supplier.geometry('800x530')
    supplier.resizable(False, False)
    
    title_bar = Frame(supplier)
    search_bar = Frame(supplier)
    supplier_bar = Frame(supplier)
    function_bar = Frame(supplier)
    option_bar = Frame(supplier)
    
    
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
    
    option_bar1 = Frame(option_bar)
    label_item_name = Label(option_bar1, text='Supplier Name: ', anchor='e')
    label_item_name.grid(row=0, column=0, pady=5, sticky='e')
    textbox_item_name = Text(option_bar1, height=1, width=20)
    textbox_item_name.grid(row=0, column=1)
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
    label_email.grid(row=0, column=2, pady=10, padx=(20,0), sticky='e')
    textbox_email = Text(option_bar2, height=1, width=35)
    textbox_email.grid(row=0, column=3)
    
    title_bar.pack()
    search_bar.pack()
    supplier_bar.pack()
    function_bar.pack()
    option_bar.pack()
    option_bar1.pack()
    option_bar2.pack()
    
    supplier.mainloop()
    
supplier_window() # comment this out
