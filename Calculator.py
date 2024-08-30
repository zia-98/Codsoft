import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x350")

        # Create input field
        self.display = tk.Entry(root, font=("Arial", 16), justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Create buttons
        self.buttons = {
            "MC": lambda: self.memory_clear(),
            "MR": lambda: self.memory_recall(),
            "M+": lambda: self.memory_add(),
            "M-": lambda: self.memory_subtract(),
            "MS": lambda: self.memory_store(),
            "%": lambda: self.percentage(),
            "CE": lambda: self.clear_entry(),
            "C": lambda: self.clear(),
            "←": lambda: self.backspace(),
            "+": lambda: self.append_operator("+"),
            "-": lambda: self.append_operator("-"),
            "*": lambda: self.append_operator("*"),
            "/": lambda: self.append_operator("/"),
            "7": lambda: self.append_digit(7),
            "8": lambda: self.append_digit(8),
            "9": lambda: self.append_digit(9),
            "4": lambda: self.append_digit(4),
            "5": lambda: self.append_digit(5),
            "6": lambda: self.append_digit(6),
            "1": lambda: self.append_digit(1),
            "2": lambda: self.append_digit(2),
            "3": lambda: self.append_digit(3),
            ".": lambda: self.append_decimal(),
            "0": lambda: self.append_digit(0),
            "=": lambda: self.calculate()
        }

        # Place buttons on the grid
        row = 1
        col = 0
        for key, command in self.buttons.items():
            button = tk.Button(root, text=key, command=command, width=5, height=2)
            button.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col == 4:
                row += 1
                col = 0

    # Memory operations
    def memory_clear(self):
        pass  # Implement memory clear logic here

    def memory_recall(self):
        pass  # Implement memory recall logic here

    def memory_add(self):
        pass  # Implement memory add logic here

    def memory_subtract(self):
        pass  # Implement memory subtract logic here

    def memory_store(self):
        pass  # Implement memory store logic here

    # Calculator functions
    def percentage(self):
        try:
            value = float(self.display.get())
            result = value / 100
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
        except ValueError:
            pass

    def clear_entry(self):
        self.display.delete(0, tk.END)

    def clear(self):
        self.display.delete(0, tk.END)
        self.expression = ""

    def backspace(self):
        self.display.delete(len(self.display.get()) - 1, tk.END)

    def append_operator(self, operator):
        self.display.insert(tk.END, operator)

    def append_digit(self, digit):
        self.display.insert(tk.END, digit)

    def append_decimal(self):
        if "." not in self.display.get():
            self.display.insert(tk.END, ".")

    def calculate(self):
        try:
            result = eval(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
        except Exception:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()