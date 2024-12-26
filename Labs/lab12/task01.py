import tkinter as tk

def calculate_cgpa():
    oop_marks = float(oop_entry.get())
    oop_lab_marks = float(oop_lab_entry.get())
    english_marks = float(english_entry.get())
    ist_marks = float(ist_entry.get())

    total_credit_hours = 8 

    oop_credit_hours = 3
    oop_lab_credit_hours = 1
    english_credit_hours = 2
    ist_credit_hours = 2

    total_marks = (oop_credit_hours * oop_marks +
                   oop_lab_credit_hours * oop_lab_marks +
                   english_credit_hours * english_marks +
                   ist_credit_hours * ist_marks)

    cgpa = total_marks / total_credit_hours

    cgpa_label.config(text=f"CGPA: {cgpa:.2f}")


window = tk.Tk()
window.title("CGPA Calculator")


oop_label = tk.Label(window, text="OOP Marks:")
oop_label.grid(row=0, column=0, padx=10, pady=5)
oop_entry = tk.Entry(window)
oop_entry.grid(row=0, column=1, padx=10, pady=5)

oop_lab_label = tk.Label(window, text="OOP Lab Marks:")
oop_lab_label.grid(row=1, column=0, padx=10, pady=5)
oop_lab_entry = tk.Entry(window)
oop_lab_entry.grid(row=1, column=1, padx=10, pady=5)

english_label = tk.Label(window, text="English Marks:")
english_label.grid(row=2, column=0, padx=10, pady=5)
english_entry = tk.Entry(window)
english_entry.grid(row=2, column=1, padx=10, pady=5)

ist_label = tk.Label(window, text="IST Marks:")
ist_label.grid(row=3, column=0, padx=10, pady=5)
ist_entry = tk.Entry(window)
ist_entry.grid(row=3, column=1, padx=10, pady=5)


calculate_button = tk.Button(window, text="Calculate CGPA", command=calculate_cgpa)
calculate_button.grid(row=4, column=0, columnspan=2, pady=10)


cgpa_label = tk.Label(window, text="CGPA: ")
cgpa_label.grid(row=5, column=0, columnspan=2, pady=5)


window.mainloop()