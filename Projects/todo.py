import tkinter as tk
from tkinter import simpledialog, messagebox


tasks = []

def add_task():
    task = simpledialog.askstring("Add Task", "Enter a new task: ")
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)

def remove_task():
    selected = listbox.curselection()
    if selected:
        task = listbox.get(selected)
        tasks.remove(task)
        listbox.delete(selected)
    else:
        messagebox.showwarning("Warning", "No task selected!")

root = tk.Tk()
root.title("To_Do List")

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack()

add_btn = tk.Button(btn_frame, text="Add Task", command=add_task)
add_btn.pack(side=tk.LEFT, padx=5)


remove_btn = tk.Button(btn_frame, text="Remove Task", command=remove_task)
remove_btn.pack(side=tk.LEFT, padx=5)

root.mainloop()










tasks = []

def show_tasks():
    if not tasks:
        print("Your to-do list is empty. ")
    else:
        print("\nYour To-Do List: ")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}.{task}")
    print()


def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added!\n")


def remove_task():
    show_tasks()
    if tasks:
        try:
            num = int(input("Enter the number of the task to remove: "))
            removed = tasks.pop(num - 1)
            print(f"Task '{removed}' removed!\n")
        except (ValueError, IndexError):
            print("Invalid number!\n")


def main():
    while True:
        print("To-Do List Menu: ")
        print("1. Show tasks ")
        print("2. Add task ")
        print("3. Remove task ")
        print("4. Exit ")
        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            add_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.\n")

if __name__ == "__main__":
    main()