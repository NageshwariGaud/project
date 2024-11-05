import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length, use_uppercase, use_numbers, use_symbols):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    numbers = string.digits if use_numbers else ''
    symbols = string.punctuation if use_symbols else ''
    
    all_characters = lowercase + uppercase + numbers + symbols
    
    if not all_characters:
        raise ValueError("At least one character type must be selected.")
    
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def create_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            raise ValueError("Password length should be at least 4.")
        
        use_uppercase = uppercase_var.get()
        use_numbers = numbers_var.get()
        use_symbols = symbols_var.get()

        password = generate_password(length, use_uppercase, use_numbers, use_symbols)
        password_entry.delete(0, tk.END)  # Clear the entry box
        password_entry.insert(0, password)  # Insert the generated password
        
    except ValueError as e:
        messagebox.showerror("Input error", str(e))

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())

# Create the main window
root = tk.Tk()
root.title("Random Password Generator")

# Input for password length
tk.Label(root, text="Password Length:").grid(row=0, column=0)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1)

# Checkboxes for character types
uppercase_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

# Ensure these lines are exactly as shown below
tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var).grid(row=1, columnspan=2)
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).grid(row=2, columnspan=2)
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).grid(row=3, columnspan=2)

# Button to generate password
generate_button = tk.Button(root, text="Generate Password", command=create_password)
generate_button.grid(row=4, columnspan=2)

# Entry to display generated password
tk.Label(root, text="Generated Password:").grid(row=5, column=0)
password_entry = tk.Entry(root)
password_entry.grid(row=5, column=1)

# Button to copy password to clipboard
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=6, columnspan=2)

# Run the application
root.mainloop()
