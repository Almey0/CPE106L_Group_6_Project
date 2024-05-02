#database.py
from sqlite3 import *

connection = connect('Vita-Vault.db')
cursor = connection.cursor()

def db_get_item():
    cursor.execute('''
        SELECT Item.item_id, Item.item_name, Item.description, Item.quantity_available, Item.unit_price, Supplier.supplier_name
        FROM Item
        INNER JOIN Supplier ON Item.supplier_id = Supplier.supplier_id
    ''')
    return cursor.fetchall()

def db_get_supplier():
    cursor.execute('''
        SELECT * 
        FROM Supplier
    ''')
    return cursor.fetchall()

def db_get_supplier_name():
    cursor.execute('''
        SELECT supplier_name
        FROM Supplier
    ''')
    return cursor.fetchall()

def db_get_transaction():
    cursor.execute('''
        SELECT Transactions.transaction_id, Item.item_name, Supplier.supplier_name, Transactions.transaction_type, Transactions.quantity, Transactions.transaction_date, Transactions.total_cost
        FROM Transactions
        INNER JOIN Supplier ON Transactions.supplier_id = Supplier.supplier_id
        INNER JOIN Item ON Transactions.item_id = Item.item_id
    ''')
    return cursor.fetchall()