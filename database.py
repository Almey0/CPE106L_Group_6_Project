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
