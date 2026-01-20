import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(entry.get())
        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4.")
            return
        
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        digits = string.digits
        symbols = string.punctuation


        password = [
            random.choice(lower),
            random.choice(upper),
            random.choice(digits),
            random.choice(symbols)
        ]

        all_chars = lower + upper + digits + symbols
        password += random.choices(all_chars, k=length-4)
        random.shuffle(password)

        result_label.config(text=''.join(password))
    except ValueError:
        messagebox.showerror("Error"< "Enter a valid number.")

root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Enter password length: ").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=5)
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()