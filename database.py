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

def db_get_item_details(item_name, supplier_name):
    cursor.execute('''
        SELECT item_id, unit_price
        FROM Item
        JOIN Supplier ON Item.supplier_id = Supplier.supplier_id
        WHERE item_name=? AND supplier_name=?
    ''', (item_name, supplier_name))
    result = cursor.fetchone()
    if result:
        return result[0], result[1]  # Return item_id and unit_price as a tuple
    else:
        return None  
    
def db_update_item(item_id, item_name, description, quantity_available, unit_price, supplier_name):
    cursor.execute('''
        SELECT supplier_id
        FROM Supplier
        WHERE supplier_name=?
    ''', (supplier_name,))
    result = cursor.fetchone()
    if result:
        supplier_id = result[0]
        # Update the item in the database with the fetched supplier_id
        cursor.execute('''
            UPDATE Item
            SET item_name=?, description=?, quantity_available=?, unit_price=?, supplier_id=?
            WHERE item_id=?
        ''', (item_name, description, quantity_available, unit_price, supplier_id, item_id))
        connection.commit()
    else:
        # Supplier not found, handle error or show message
        print('Supplier not found.')

def db_add_item(item_name, description, quantity_available, unit_price, supplier_id):
    cursor.execute('''
        INSERT INTO Item (item_name, description, quantity_available, unit_price, supplier_id)
        VALUES (?, ?, ?, ?, ?)
    ''', (item_name, description, quantity_available, unit_price, supplier_id))
    connection.commit()

def db_delete_item(item_id):
    cursor.execute('''
        DELETE FROM Item
        WHERE item_id=?
    ''', (item_id,))
    connection.commit()

def db_add_transaction(transaction_type, quantity, transaction_date, total_cost, item_id, supplier_id):
    cursor.execute('''
        INSERT INTO Transactions (transaction_type, quantity, transaction_date, total_cost, item_id, supplier_id)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (transaction_type, quantity, transaction_date, total_cost, item_id, supplier_id))
    connection.commit()

def db_update_transaction(transaction_id, item_name, supplier_name, transaction_type, quantity):
    # Get the item ID using the item_name and supplier_name parameters
    item_details = db_get_item_details(item_name, supplier_name)

    if item_details is None:
        # Handle error or show message
        print('Item not found.')
        return

    item_id, unit_price = item_details

    if transaction_type == 'Purchase':
        # Update the transaction in the database with the fetched item details and the calculated total cost
        cursor.execute('''
            UPDATE Transactions
          SET item_id=?, unit_price=?, quantity=?, total_cost=?, transaction_type=?
            WHERE transaction_id=?
        ''', (item_id, unit_price, quantity, quantity * unit_price, transaction_type, transaction_id))
        connection.commit()
    elif transaction_type == 'Sell':
        # Convert the quantity variable to an integer
        quantity = int(quantity)

        # Check if the quantity available is sufficient for the sell transaction
        cursor.execute('''
            SELECT quantity_available
            FROM Item
            WHERE item_id=?
        ''', (item_id,))
        result = cursor.fetchone()
        if result:
            quantity_available = result[0]
            if quantity_available >= quantity:
                # Update the item quantity available in the database
                cursor.execute('''
                    UPDATE Item
                    SET quantity_available=quantity_available-?
                    WHERE item_id=?
                ''', (quantity, item_id))
                connection.commit()

                # Update the transaction in the database with the fetched item details and the given total cost
                cursor.execute('''
                    UPDATE Transactions
                    SET item_id=?, quantity=?, total_cost=?, transaction_type=?
                    WHERE transaction_id=?
                ''', (item_id, quantity, quantity * unit_price, transaction_type, transaction_id))
                connection.commit()
            else:
                # Handle error or show message
                print('Insufficient quantity available.')
        else:
            # Handle error or show message
            print('Item not found.')
    else:
        # Handle error or show message
        print('Invalid transaction type.')

def db_delete_transaction(transaction_id):
    cursor.execute('''
        DELETE FROM Transactions
        WHERE transaction_id=?
    ''', (transaction_id,))
    connection.commit()

def db_get_supplier_names(item_name):
    cursor.execute('''
        SELECT DISTINCT Supplier.supplier_name
        FROM Item
        JOIN Supplier ON Item.supplier_id = Supplier.supplier_id
        WHERE Item.item_name=?
    ''', (item_name,))
    result = cursor.fetchall()
    if result:
        return [row[0] for row in result]
    else:
        return []
    
def db_get_item_names():
    cursor.execute('''
        SELECT item_name
        FROM Item
    ''')
    return [row[0] for row in cursor.fetchall()]

def db_get_all_supplier_names():
    cursor.execute('''
        SELECT supplier_name
        FROM Supplier
    ''')
    return [row[0] for row in cursor.fetchall()]

def db_get_supplier_id(supplier_name):
    cursor.execute('''
        SELECT supplier_id
        FROM Supplier
        WHERE supplier_name=?
    ''', (supplier_name,))
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return None
    
def db_add_supplier(supplier_name, contact_person, contact_number, email):
    cursor.execute('''
        INSERT INTO Supplier (supplier_name, contact_person, contact_number, email)
        VALUES (?, ?, ?, ?)
    ''', (supplier_name, contact_person, contact_number, email))
    connection.commit()

def db_update_supplier(supplier_id, supplier_name, contact_person, contact_number, email):
    cursor.execute('''
        UPDATE Supplier
        SET supplier_name=?, contact_person=?, contact_number=?, email=?
        WHERE supplier_id=?
    ''', (supplier_name, contact_person, contact_number, email, supplier_id))
    connection.commit()

def db_delete_supplier(supplier_id):
    cursor.execute('''
        DELETE FROM Supplier
        WHERE supplier_id=?
    ''', (supplier_id,))
    connection.commit()