import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password():
    length = int(length_entry.get())
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_password():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Empty", "No password to copy!")

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")
root.resizable(False, False)

# UI Elements
tk.Label(root, text="Password Length:").pack(pady=5)
length_entry = tk.Entry(root, width=10)
length_entry.insert(0, "12")
length_entry.pack()

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)
password_entry = tk.Entry(root, width=40)
password_entry.pack()

tk.Button(root, text="Copy to Clipboard", command=copy_password).pack(pady=10)

# Run the GUI
root.mainloop()
