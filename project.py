import tkinter as tk

def check_strength():
    password = password_entry.get()
    length = len(password)

    if length <= 5:
        strength_label.config(text="Weak", fg="red")
    elif 6 <= length <= 8:
        strength_label.config(text="Medium", fg="yellow")
    elif 9 <= length <= 12:
        strength_label.config(text="Strong", fg="lightgreen")
    else:
        strength_label.config(text="Very Strong", fg="darkgreen")

# Create the main window
root = tk.Tk()
root.geometry("400x400")
root.title("Length Converter App")

# Add a label for instructions
instruction_label = tk.Label(root, text="Enter Password:")
instruction_label.pack(pady=10)

# Add an entry box for the password
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=10)

# Add a button to check password strength
check_button = tk.Button(root, text="Check Strength", command=check_strength)
check_button.pack(pady=10)

# Add a label to display the password strength
strength_label = tk.Label(root, text="")
strength_label.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
