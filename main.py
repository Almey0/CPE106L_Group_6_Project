import tkinter as tk

root = tk.Tk()

root.geometry("1280x720")
root.title("Vita-Vault")

label =tk.Label(root, text='Hello World!', font=('Tahoma', 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3, font=('Tahoma', 16))
textbox.pack(padx=10)

button = tk.Button(root, text='Click Me!', font=('Tahoma', 18))
button.pack()

root.mainloop()
