import tkinter as tk


def convert_to_f():
    try:
        c = float(entry.get())
        result = (c * 9/5) + 32
        result_label.config(text=f"{result:.2f} °F")
    except ValueError:
        result_label.config(text="Invalid input")

def convert_to_c():
    try:
        f = float(entry.get())
        result = (f - 32) * 5/9
        result_label.config(text=f"{result:.2f} °C")
    except ValueError:
        result_label.config(text="Invalid input")


root = tk.Tk()
root.title("Temperature Converter")

tk.Label(root, text="Enter Temperature").grid(row=0, column=0, columnspan=2)

entry = tk.Entry(root)
entry.grid(row=1, column=0, columnspan=2)


tk.Button(root, text="C → F", command=convert_to_f ).grid(row=2, column=0)

tk.Button(root, text="F → C", command=convert_to_c ).grid(row=2, column=1)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2)

root.mainloop()

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def main():
    print("Temperature Converter ")
    print("1. Celsius to Fahrenhei ")
    print("2. Fahrenheit to Celsius ")

    choice = input("Choose (1 or 2): ")

    if choice == "1":
        c = float(input("Enter temperature in Celsius: "))
        print(f"{c}°C = {celsius_to_fahrenheit(c):.2f}°F")

    elif choice == "2":
        f = float(input("Enter temperature in Fahrenheit: "))
        print(f"{f}°F = {fahrenheit_to_celsius(f):.2f}°C")
    
    else:
        print("Invalied choice")


if __name__ == "__main___":
    main()

