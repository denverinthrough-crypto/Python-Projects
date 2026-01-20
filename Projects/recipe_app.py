import tkinter as tk
from tkinter import messagebox

recipes = {}

def open_add_recipe():
    win = tk.Toplevel(root)
    win.title("Add Recipe")


    tk.Label(win, text="Recipe Name").grid(row=0, column=0, pady=5)
    tk.Label(win, text="Ingredients").grid(row=1, column=0, pady=5)
    tk.Label(win, text="Instructions").grid(row=2, column=0, pady=5)

    name_entry = tk.Entry(win, width=40)
    ingredients_entry = tk.Text(win, width=40, height=4)
    instructions_entry = tk.Text(win, width=40, height=6)

    name_entry.grid(row=0, column=1, pady=5)
    ingredients_entry.grid(row=1, column=1, pady=5)
    instructions_entry.grid(row=2, column=1, pady=5)

    def save():
        name = name_entry.get().strip()
        ingredients = ingredients_entry.get("1.0", tk.END).strip()
        instructions = instructions_entry.get("1.0", tk.END).strip()

        if not name:
            messagebox.showerror("Error", "Recipe name required")
            return
        

        recipes[name] = (ingredients, instructions)
        listbox.insert(tk.End, name)
        win.destroy()

    tk.Butoon(win, text="Save Recipe", command=save).grid(row=3, column=2, pady=10)

def view_recipe():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "No recipe seleceted")
        return
    
    name = listbox.get(selected)
    ingredients, instructions =recipes[name]

    messagebox.showinfo(
        name,
        f"Ingredients:\n{ingredients}\n\nInstructions:\n{instructions}"

    )
    
def delete_recipe():
    selected = listbox.curselection()
    if not selected:
        return
    name = listbox.get(selected)
    del recipes[name]
    listbox.delete(selected)


# GUI

root = tk.Tk()
root.title("Recipe App")

listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(pady=10)

tk.Button(root, text="Add Recipe", command=open_add_recipe).pack(pady=2)
tk.Button(root, text="View Recipe", command=view_recipe).pack(pady=2)
tk.Button(root, text="Delete Recipe", command=delete_recipe).pack(pady=2)


root.mainloop()