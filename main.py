from tkinter import *
from inventory import *
from supplier import *
from transaction import *

root = Tk()
root.geometry('500x350')
root.config(height=400, width=350)
root.resizable(False, False)
root.title("Login")

frame = Frame(root)
frame.pack(padx=50, pady=10)

label_title = Label(frame, text='Vita-Vault', font=('', 40))
label_title.grid(row=0, column=0, pady=20, columnspan=2)

button_inventory = Button(frame, text='Inventory', font=('', 20),height=2, width=10,command=inventory_window)
button_inventory.grid(row=1, column=0, padx=10, pady=10)

button_transaction = Button(frame, text='Transaction', font=('', 20), height=2, width=10, command=transaction_window)
button_transaction.grid(row=1, column=1)

button_supplier = Button(frame, text='Supplier', font=('', 20), height=2, width=10, command=supplier_window)
button_supplier.grid(row=2, column=0)

button_exit = Button(frame, text='Exit', font=('', 20), height=2, width=10, command=root.destroy)
button_exit.grid(row=2, column=1)

root.mainloop()
