import tkinter as tk
from tkinter import filedialog, messagebox
import os

current_path = os.path.expanduser("~") # start in your home directory


def update_listbox(path):
    global current_path
    current_path = path
    listbox.delete(0, tk.END)
    listbox.insert(tk.END, ".. (Go up)")

    try:
        items = os.listdir(path)
        for item in items:
            listbox.insert(tk.END, item)
        path_label.config(text=path)
    except PermissionError:
        messagebox.showerror("Error", "Permission denied!")


def open_item():
    selected = listbox.curselection()
    if not selected:
        return
    
    item = listbox.get(selected)
    if item == ".. (Go up)":
        parent = os.path.dirname(current_path)
        update_listbox(parent)
        return
    

    path = os.pahtjoin(current_path, item)
    if os.path.isdir(path):
        update_listbox(path)
    else:
        try:
            os.startfile(path)  # open file with default app(Windows)
        except Exception as e:
            messagebox.showerror("Error", str(e))

def browse_folder():
    folder = filedialog.askdirectory(initialdir=current_path)
    if folder:
        update_listbox(folder)



# GUI

root = tk.Tk()
root.title("Python File Explorer")
root.geometry("600x400")

path_label = tk.Label(root, text=current_path, anchor="w")
path_label.pack(fill="x", padx=5, pady=5)

listbox = tk.Listbox(root, width=80, height=20)
listbox.pack(padx=10, pady=10)
listbox.bind("<Double-1>", lambda e: open_item())

btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="Browse Folder", command=browse_folder).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Open Selected", command=open_item).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Go up", command=lambda: update_listbox(os.path.dirname(current_path))).pack(side=tk.LEFT, padx=5)


update_listbox(current_path)
root.mainloop()