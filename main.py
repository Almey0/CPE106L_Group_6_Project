from tkinter import *
from inventory import *
from supplier import *
from transaction import *

root = Tk()
root.geometry('500x500')
root.config(height=500, width=500)
#root.resizable(False, False)
root.title("Login")

frame = Frame(root)
frame.pack(padx=50, pady=10)

label_title = Label(frame, 
                    text='Vita-Vault', 
                    font=('Arial', 40))
label_title.grid(row=0, column=0, 
                 pady=20, 
                 columnspan=2)

button_inventory = Button(frame, 
                          text='Inventory', 
                          font=('Tahoma', 15), 
                          height=2, width=10, 
                          command=inventory_window)
button_inventory.grid(row=1, column=0, 
                      padx=10, pady=10)
button_transaction = Button(frame, 
                            text='Transaction', 
                            font=('Tahoma', 15), 
                            height=2, width=10, 
                            command=transaction_window)
button_transaction.grid(row=1, column=1)
button_supplier = Button(frame, 
                         text='Supplier', 
                         font=('Tahoma', 15), 
                         height=2, width=10, 
                         command=supplier_window)
button_supplier.grid(row=2, column=0)
button_exit = Button(frame, 
                     text='Exit', 
                     font=('Tahoma', 15), 
                     height=2, width=10, 
                     command=root.destroy)
button_exit.grid(row=2, column=1)

root.mainloop()
