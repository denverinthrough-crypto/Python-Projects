import tkinter as tk

def click(button_value):
       current = entry.get()
       entry.delete(0, tk.END)
       entry.insert(0, current + str(button_value))

def clear():
       entry.delete(0, tk.END)

def calculator():
       try:
              result = eval(entry.get())
              entry.delete(0, tk.END)
              entry.insert(0, result)
       except:
              entry.delete(0, tk.END)
              entry.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=20, font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
       "7", "8", "9", "/",
       "4", "5", "6", "*",
       "1", "2", "3", "-",
       "0", ".", "=", "+"
]

row = 1
col = 0

for button in buttons:
       if button == "=":
              tk.Button(root, text=button, width=5, command=calculator).grid(row=row, column=col)

       else:
              tk.Button(root, text=button, width=5,
                        command=lambda b=button: click(b)).grid(row=row, column=col)

       col += 1
       if col > 3:
              col = 0
              row += 1

tk.Button(root, text="C", width=5, command=clear).grid(row=row, column=0)

root.mainloop()
       


def add(a, b):
        return a + b

def subtract(a, b):
        return a - b

def multiply(a, b):
        return a * b

def divide(a, b):
        if b == 0:
            return "Error: Cannot divide by zero"
        return a / b

print("Simple Calculator ")
print("Choose an operation: ")
print("1. Add ")
print("2. Subtract ")
print("3. Multiply ")
print("4. Divide ")

choice = input("Enter choice (1/2/3/4) ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == "1":
       print("Result:", add(num1, num2))
elif choice == "2":
       print("Result:", subtract(num1, num2))
elif choice == "3":
       print("Result:", multiply(num1, num2))
elif choice == "4":
       print("Result:", divide(num1, num2))
else:
       print("Invalid choice")