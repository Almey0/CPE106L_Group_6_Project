from tkinter import *

def transaction_window():
    transaction = Toplevel()
    transaction.title('Transaction')
    transaction.config(neight=500, width=500)
    transaction.geometry('500x500')
    transaction.resizable(False, False)