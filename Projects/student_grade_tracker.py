import tkinter as tk
from tkinter import simpledialog, messagebox
import json
import os

# File to store date

DATA_FILE = "students_data.json"

# Load data from file if exists

if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        students = json.load(f)

else:
    students = {} # Format: {"Alice": {"Math": 90, "English": 85}}

# Convert grades back to float (JSON saves as strings sometimes)

for student in students:
    for subj in students[student]:
        student[student][subj] = float(students[student][subj])


# Letter grade function

def get_letter_grade(score):
    if score >= 90: return "A"
    elif score >= 80: return "B"
    elif score >= 70: return "C"
    elif score >= 60: return "D"
    else: return "F"


# Update listbox

def update_listbox(filtered=None):
    listbox.delete(0, tk.END)
    data = filtered if filtered else students
    for students, grades in data.items():
        subjects_str = ", ".join([f"{sub}: {grade} ({get_letter_grade(grade)})" for sub, grade in grades.items()])
        avg = sum(grades.values()) / len(grades)
        listbox.insert(tk.END, f"{student}: {subjects_str} | Avg: {avg:.2f} ({get_letter_grade(avg)})")


# Add student

def add_student():
    name = simpledialog.askstring("Add Student", "Enter student's name:")
    if not name:
        return
    
    subjects = {}
    while True:
        subject = simpledialog.askstring("Add Subject", "Enter subject name(or leave blank to finish):")
        if not subject:
            break
        try:
            grade = float(simpledialog.askstring("Add Grade", f"Enter grade for {subject}:"))
            subjects[subject] = grade
        except (ValueError, TypeError):
            messagebox.showerror("Error", "Invalid grade! Try again.")
            continue

    if subjects:
        students[name] = subjects
        save_data()
        messagebox.showinfo("Success", f"Added {name} with subjects: {', '.join(subjects.keys())}")
        update_listbox()

# Remove student

def remove_student():
    selected = listbox.curselection()
    if selected:
        student_name = listbox.get(selected).split(":")[0]
        del students[student_name]
        save_data()
        messagebox.showinfor("Removed", f"Removed {student_name}")
        update_listbox()
    else:
        messagebox.showwarning("Warning", "No student selected!")

# Edit student grades

def edit_student():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "No student selected!")
        return
    student_name = listbox.get(selected).split(":")[0]
    student_grades = students[student_name]

    while True:
        subject = simpledialog.askstring("Edit Subject", "Enter subject to edit (or leave blank to finish):")
        if not subject:
            break
        if subject not in student_grades:
            messagebox.showwarning("Warning", f"{subject} not found")
            continue
        try:
            grade = float(simpledialog.askstring("Edit Grade", f"Enter new grade  for {subject}:"))
            student_grades[subject] = grade
        except (ValueError, TypeError):
            messagebox.showerror("Error", "Invalid grade! Try again.")
            continue

    save_data()
    update_listbox()

# Show average

def average_grade():
    selected = listbox.curselection()
    if selected:
        student_name = listbox.get(selected).split(":")[0]
        grades = students[student_name].value()
        avg = sum(grades) / len(grades)
        messagebox.showinfo("Average Grade", f"{student_name}'s average: {avg:.2f} ({get_letter_grade(avg)})")
    else:
        messagebox.showwarning("Warning", "NO student selected!")

# Sort studetns by average

def sort_by_average():
    sorted_students = dict(sorted(students.items(), key=lambda x: sum(x[1].values())/len(x[1]), reverse=True))
    update_listbox(sorted_students)


# Filter by subject

def filter_by_subject():
    subject = simpledialog.askstring("Filter by Subject", "Enter subject name:")
    if not subject:
        return
    filtered = {}
    for student, grades in students.items():
        if subject in grades:
            filtered[student] = {subject: grades[subject]}
    update_listbox(filtered)


# GUI  Setup

root = tk.Tk()
root.title("Student Grade Tracker Pro")

listbox = tk.Listbox(root, width=100)
listbox.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="Add Student", command=add_student, width=15).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Remove Student", command=remove_student, width=15).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Edit Grades", command=edit_student, width=15).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Average Grade", command=average_grade, width=15).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Sort by Average", command=sort_by_average, width=15).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Filter by Subject", command=filter_by_subject, width=15).pack(side=tk.LEFT, padx=5)

update_listbox()
root.mainloop()



        


     