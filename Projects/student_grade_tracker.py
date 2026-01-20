import tkinter as tk
from tkinter import simpledialog, messagebox
import json
import os

# ---------------- FILE SETUP ----------------
DATA_FILE = "students_data.json"

if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        students = json.load(f)
else:
    students = {}

# Ensure grades are floats
for student in students:
    for subject in students[student]:
        students[student][subject] = float(students[student][subject])


# ---------------- HELPERS ----------------
def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(students, f, indent=4)


def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


# ---------------- UI FUNCTIONS ----------------
def update_listbox(filtered=None):
    global students
    listbox.delete(0, tk.END)
    data = filtered if filtered is not None else students

    for student, grades in data.items():
        subjects = ", ".join(
            f"{sub}: {grade} ({get_letter_grade(grade)})"
            for sub, grade in grades.items()
        )
        avg = sum(grades.values()) / len(grades)
        listbox.insert(
            tk.END,
            f"{student}: {subjects} | Avg: {avg:.2f} ({get_letter_grade(avg)})"
        )


def add_student():
    global students
    name = simpledialog.askstring("Add Student", "Enter student's name:")
    if not name:
        return

    subjects = {}
    while True:
        subject = simpledialog.askstring(
            "Add Subject", "Enter subject name (leave blank to finish):"
        )
        if not subject:
            break
        try:
            grade = float(
                simpledialog.askstring("Add Grade", f"Enter grade for {subject}:")
            )
            subjects[subject] = grade
        except (ValueError, TypeError):
            messagebox.showerror("Error", "Invalid grade!")

    if subjects:
        students[name] = subjects
        save_data()
        update_listbox()


def remove_student():
    global students
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "No student selected!")
        return

    name = listbox.get(selected).split(":")[0]
    del students[name]
    save_data()
    update_listbox()


def edit_student():
    global students
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "No student selected!")
        return

    name = listbox.get(selected).split(":")[0]
    grades = students[name]

    while True:
        subject = simpledialog.askstring(
            "Edit Subject", "Enter subject to edit (leave blank to finish):"
        )
        if not subject:
            break
        if subject not in grades:
            messagebox.showwarning("Warning", "Subject not found!")
            continue
        try:
            new_grade = float(
                simpledialog.askstring("Edit Grade", f"New grade for {subject}:")
            )
            grades[subject] = new_grade
        except (ValueError, TypeError):
            messagebox.showerror("Error", "Invalid grade!")

    save_data()
    update_listbox()


def average_grade():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "No student selected!")
        return

    name = listbox.get(selected).split(":")[0]
    grades = students[name].values()
    avg = sum(grades) / len(grades)
    messagebox.showinfo(
        "Average Grade",
        f"{name}'s Average: {avg:.2f} ({get_letter_grade(avg)})",
    )


def sort_by_average():
    global students
    sorted_students = dict(
        sorted(
            students.items(),
            key=lambda x: sum(x[1].values()) / len(x[1]),
            reverse=True,
        )
    )
    update_listbox(sorted_students)


def filter_by_subject():
    subject = simpledialog.askstring("Filter", "Enter subject name:")
    if not subject:
        return

    filtered = {
        student: {subject: grades[subject]}
        for student, grades in students.items()
        if subject in grades
    }

    update_listbox(filtered)


# ---------------- GUI SETUP ----------------
root = tk.Tk()
root.title("Student Grade Tracker Pro")

listbox = tk.Listbox(root, width=110)
listbox.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=5)

tk.Button(frame, text="Add Student", width=15, command=add_student).pack(side=tk.LEFT, padx=4)
tk.Button(frame, text="Remove Student", width=15, command=remove_student).pack(side=tk.LEFT, padx=4)
tk.Button(frame, text="Edit Grades", width=15, command=edit_student).pack(side=tk.LEFT, padx=4)
tk.Button(frame, text="Average Grade", width=15, command=average_grade).pack(side=tk.LEFT, padx=4)
tk.Button(frame, text="Sort by Average", width=15, command=sort_by_average).pack(side=tk.LEFT, padx=4)
tk.Button(frame, text="Filter by Subject", width=15, command=filter_by_subject).pack(side=tk.LEFT, padx=4)

update_listbox()
root.mainloop()
