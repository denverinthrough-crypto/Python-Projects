"""
ADVANCED PYTHON CALCULATOR PROJECT (UPGRADED)
============================================
Features included:
1. GUI Calculator (Tkinter)
2. Scientific operations
3. Safe evaluation (no raw eval)
4. Calculation history + saved to file
5. Keyboard input support
6. Backspace & clear
7. Dark mode toggle
8. Graphing (simple function plot)
9. Packaged for learning and extension
"""


import tkinter as tk
from tkinter import messagebox, filedialog
import math
import matplotlib.pyplot as plt
import os


#-------------- SAFE EVALUATION ----------------

allowed_names = {
    'abs': abs, 'round': round, 'sqrt': math.sqrt, 'pow': pow,
    'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
    'pi': math.pi, 'e': math.e
}

HISTORY_FILE = 'calc_history.txt'

# ---------------- FUNCTIONS ----------------

def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def backspace():
    entry.delete(len(entry.get()) - 1)

def calculate():
       try:
              expression = entry.get()
              result = eval(expression, {"__builtins__": None}, allowed_names)
              entry.delete(0, tk.END)
              entry.insert(0, result)
              history.insert(tk.END, f"{expression} = {result}")
              save_history(f"{expression} = {result}")
       except:
              entry.delete(0, tk.END)
              entry.insert(0, "Error")
       
def save_history(text):
      with open(HISTORY_FILE, 'a') as f:
            f.write(text + '\n')

def load_history():
      if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE) as f:
                  for line in f:
                        history.insert(tk.END, line.strip())


def clear_history():
      history.delete(0, tk.END)
      with open(HISTORY_FILE, 'w') as f:
            f.write('')

def toggle_dark_mode():
       if root['bg'] == 'white':
            root.configure(bg='black')
            entry.configure(bg='gray20', fg='white')
            history.configure(bg='gray20', fg='white')
       else:
             root.configure(bg='white')
             entry.configure(bg='white', fg='black')
             history.configure(bg='white', fg='black')

def plot_function():
       try:
            expr = entry.get()
            x_values = [i/10 for i in range(-100, 101)]
            y_values = [eval(expr.replace('x', str(x)), {"__builtins__": None}, allowed_names) for x in x_values]
            plt.plot(x_values, y_values)
            plt.title(f"Plot of {expr}")
            plt.xlabel('x')
            plt.ylabel('y')
            plt.grid(True)
            plt.show()
       except Exception as e:
            messagebox.showerror("Error", f"Invalied expression for plotting: {e}")

# ---------------- GUI SETUP -----------------

root = tk.Tk()
root.title("Advance Calculator")
root.geometry("450x600")
root.configure(bg='white')

entry = tk.Entry(root, font=("Arial", 18), justify="right")
entry.pack(fill="x", padx=10, pady=10)

# ------------ BUTTON FRAME -----------

btn_frame = tk.Frame(root)
btn_frame.pack()

buttons = [
      '7', '8', '9', '/',
      '4', '5', '6', '*',
      '1', '2', '3', '-',
      '0', '.', '(',')',
      'sqrt', 'pow', 'sin', '+',
      'cos', 'tan', 'pi', '=', 'plot'
]

row = 0
col = 0

for btn in buttons:
       if btn == '=':
            action = calculate
       elif btn == 'plot':
             action = plot_function
       elif btn == 'sqrt':
             action = lambda: click('sqrt(')
       elif btn == 'pow':
             action = lambda: click('pow(')
       elif btn in ['sin', 'cos', 'tan']:
             action = lambda b=btn: click(b + '(')
       else:
             action = lambda b=btn: click(b)

       tk.Button(btn_frame, text=btn, width=6, height=2, command=action).grid(row=row, column=col, padx=3, pady=3)

       col += 1
       if col == 4:
             col = 0
             row += 1

# --------------- EXTRA CONTROLS ---------------


extra = tk.Frame(root)
extra.pack(pady=5)

tk.Button(extra, text="Clear", width=10, command=clear).pack(side="left", padx=5)
tk.Button(extra, text="Back", width=10, command=backspace).pack(side="left", padx=5)
tk.Button(extra, text="Dark Mode", width=10, command=toggle_dark_mode).pack(side="left", padx=5)
tk.Button(extra, text="Clear History", width=12, command=clear_history).pack(side="left", padx=5)


#----------------HISTORY ----------------

history_label = tk.Label(root, text="History", bg='white')
history_label.pack()

history = tk.Listbox(root, height=10)
history.pack(fill="both", padx=10, pady=5)

load_history()

# -------------- KEYBOARD SHORTCUT -------------


root.bind_all('<Return>', lambda e: calculate())
root.bind_all('<BackSpace>', lambda e: backspace())


root.mainloop()