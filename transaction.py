from tkinter import *

def transaction_window():
    transaction = Toplevel()
    transaction.title('Transaction')
    transaction.config(height=500, width=500)
    transaction.geometry('500x500')
    transaction.resizable(False, False)