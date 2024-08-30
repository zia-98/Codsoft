import tkinter as tk
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Password Generator")
        self.root.geometry("400x300")

        # Labels and Entry fields
        self.length_label = tk.Label(root, text="Password Length:")
        self.length_entry = tk.Entry(root, width=10)
        self.include_uppercase_label = tk.Label(root, text="Include Uppercase Letters:")
        self.include_uppercase_var = tk.IntVar(value=1)  # Default to True
        self.include_uppercase_checkbox = tk.Checkbutton(
            root, variable=self.include_uppercase_var
        )
        self.include_lowercase_label = tk.Label(root, text="Include Lowercase Letters:")
        self.include_lowercase_var = tk.IntVar(value=1)  # Default to True
        self.include_lowercase_checkbox = tk.Checkbutton(
            root, variable=self.include_lowercase_var
        )
        self.include_digits_label = tk.Label(root, text="Include Digits:")
        self.include_digits_var = tk.IntVar(value=1)  # Default to True
        self.include_digits_checkbox = tk.Checkbutton(root, variable=self.include_digits_var)
        self.include_symbols_label = tk.Label(root, text="Include Symbols:")
        self.include_symbols_var = tk.IntVar(value=1)  # Default to True
        self.include_symbols_checkbox = tk.Checkbutton(root, variable=self.include_symbols_var)
        self.password_label = tk.Label(root, text="Generated Password:")
        self.password_display = tk.Label(root, text="", font=("Arial", 12))

        # Button
        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.copy_button = tk.Button(root, text="Copy Password", command=self.copy_password, state="disabled")  # Initially disabled

        # Place widgets on the grid
        self.length_label.grid(row=0, column=0, padx=5, pady=5)
        self.length_entry.grid(row=0, column=1, padx=5, pady=5)
        self.include_uppercase_label.grid(row=1, column=0, padx=5, pady=5)
        self.include_uppercase_checkbox.grid(row=1, column=1, padx=5, pady=5)
        self.include_lowercase_label.grid(row=2, column=0, padx=5, pady=5)
        self.include_lowercase_checkbox.grid(row=2, column=1, padx=5, pady=5)
        self.include_digits_label.grid(row=3, column=0, padx=5, pady=5)
        self.include_digits_checkbox.grid(row=3, column=1, padx=5, pady=5)
        self.include_symbols_label.grid(row=4, column=0, padx=5, pady=5)
        self.include_symbols_checkbox.grid(row=4, column=1, padx=5, pady=5)
        self.password_label.grid(row=5, column=0, padx=5, pady=5)
        self.password_display.grid(row=5, column=1, padx=5, pady=5)
        self.generate_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)
        self.copy_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError

            # Build character set based on user selections
            character_set = ""
            if self.include_uppercase_var.get():
                character_set += string.ascii_uppercase
            if self.include_lowercase_var.get():
                character_set += string.ascii_lowercase
            if self.include_digits_var.get():
                character_set += string.digits
            if self.include_symbols_var.get():
                character_set += string.punctuation

            # Check if character set is empty
            if not character_set:
                raise ValueError("Please select at least one character type.")

            password = ''.join(random.choice(character_set) for _ in range(length))
            self.password_display.config(text=password)
            self.copy_button.config(state="normal")  # Enable the Copy button
        except ValueError as e:
            self.password_display.config(text=str(e))
            self.copy_button.config(state="disabled")  # Disable the Copy button

    def copy_password(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.password_display.cget("text"))

if __name__ == "__main__":
    root = tk.Tk()
    password_generator = PasswordGenerator(root)
    root.mainloop()