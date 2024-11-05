import tkinter as tk
from tkinter import messagebox

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def calculate():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive numbers.")

        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)

        result_label.config(text=f"Your BMI is: {bmi:.2f}\nCategory: {category}")
    
    except ValueError as e:
        messagebox.showerror("Input error", str(e))

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Create input fields and labels
tk.Label(root, text="Weight (kg):").grid(row=0, column=0)
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1)

tk.Label(root, text="Height (m):").grid(row=1, column=0)
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1)

# Create a button to calculate BMI
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate)
calculate_button.grid(row=2, column=0, columnspan=2)

# Label to display results
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2)

# Run the application
root.mainloop()
