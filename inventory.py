from tkinter import *

def inventory_window():
    inventory = Toplevel()
    inventory.title('Inventory')
    inventory.config(height=500, width=500)
    inventory.geometry('500x500')
    inventory.resizable(False, False)
    
    frame = Frame(inventory)
    
    label_title = Label(frame, 
                        text='Inventory', 
                        font=('Tahoma', 40))
    
    frame.pack()
    
    frame.mainloop()