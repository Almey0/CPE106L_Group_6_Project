import tkinter as tk
from tkinter import messagebox
import sqlite3

def login():
    username = entry_username.get()
    password = entry_password.get() 
    

    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = c.fetchone()
    
    if result:
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

    conn.close()

# register
def register():
    registration_window = tk.Toplevel(root)
    registration_window.title("Registration")
    
    tk.Label(registration_window, text="Username:").grid(row=0, column=0, pady=(10, 5))
    tk.Label(registration_window, text="Password:").grid(row=1, column=0, pady=5)
    tk.Label(registration_window, text="Confirm Password:").grid(row=2, column=0, pady=5)

    entry_username_reg = tk.Entry(registration_window)
    entry_username_reg.grid(row=0, column=1, pady=(10, 5))
    entry_password_reg = tk.Entry(registration_window, show="*")
    entry_password_reg.grid(row=1, column=1, pady=5)
    entry_confirm_password_reg = tk.Entry(registration_window, show="*")
    entry_confirm_password_reg.grid(row=2, column=1, pady=5)

    def register_new_user():
        new_username = entry_username_reg.get()
        new_password = entry_password_reg.get()
        confirm_password = entry_confirm_password_reg.get()

        conn = sqlite3.connect('users.db')
        c = conn.cursor()

        if new_password == confirm_password:
            c.execute("SELECT * FROM users WHERE username=?", (new_username,))
            existing_user = c.fetchone()

            if existing_user:
                messagebox.showerror("Registration Failed", "Username already exists.")
            else:
                c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (new_username, new_password))
                conn.commit()
                messagebox.showinfo("Registration Successful", "Welcome, " + new_username + "! You are now registered.")
                registration_window.destroy()
        else:
            messagebox.showerror("Registration Failed", "Passwords do not match.")

        conn.close()

    tk.Button(registration_window, text="Register", command=register_new_user).grid(row=3, columnspan=2, pady=(10, 0))

root = tk.Tk()
root.title("Login")
root.geometry("1280x720")

# login
tk.Label(root, text="Username:").grid(row=0, column=0, pady=(10, 5))
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, pady=(10, 5))
 
tk.Label(root, text="Password:").grid(row=1, column=0, pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1, pady=5)

tk.Button(root, text="Login", command=login, width=10).grid(row=2, column=0, columnspan=2, pady=(20, 10))
tk.Button(root, text="Register", command=register, width=10).grid(row=3, column=0, columnspan=2)

conn = sqlite3.connect('users.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
             )''')

conn.commit()
conn.close()

root.mainloop()
