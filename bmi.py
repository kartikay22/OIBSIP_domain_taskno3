import tkinter as tk
from tkinter import messagebox

class BMICalculatorApp:
    def __init__(self, master):
        """
        Initializes the BMI Calculator application.

        Args:
            master (tk.Tk): The root Tkinter window.
        """
        self.master = master
        master.title("BMI Calculator")
        master.geometry("400x300")
        master.configure(bg='#f0f0f0')

        # Create main frame with padding and rounded corners
        self.main_frame = tk.Frame(master, padx=20, pady=20, bg='#ffffff', bd=2, relief="groove")
        self.main_frame.pack(expand=True, padx=20, pady=20)

        # Title Label
        self.title_label = tk.Label(self.main_frame, text="BMI Calculator", font=("Arial", 16, "bold"), bg='#ffffff', fg='#333333')
        self.title_label.pack(pady=10)

        # Weight Input
        self.weight_label = tk.Label(self.main_frame, text="Weight (kg):", font=("Arial", 12), bg='#ffffff', fg='#555555')
        self.weight_label.pack(pady=(10, 0))
        self.weight_entry = tk.Entry(self.main_frame, width=30, font=("Arial", 12), bd=1, relief="solid")
        self.weight_entry.pack()

        # Height Input
        self.height_label = tk.Label(self.main_frame, text="Height (m):", font=("Arial", 12), bg='#ffffff', fg='#555555')
        self.height_label.pack(pady=(10, 0))
        self.height_entry = tk.Entry(self.main_frame, width=30, font=("Arial", 12), bd=1, relief="solid")
        self.height_entry.pack()

        # Calculate Button
        self.calculate_button = tk.Button(self.main_frame, text="Calculate BMI", font=("Arial", 12, "bold"), bg='#007bff', fg='#ffffff', relief="raised", command=self.calculate_bmi)
        self.calculate_button.pack(pady=20)

        # Result Label
        self.result_label = tk.Label(self.main_frame, text="", font=("Arial", 12, "bold"), bg='#ffffff', fg='#000000')
        self.result_label.pack()

        # Category Label
        self.category_label = tk.Label(self.main_frame, text="", font=("Arial", 12), bg='#ffffff', fg='#000000')
        self.category_label.pack()

    def validate_input(self, value):
        """
        Validates if the input value is a positive number.

        Args:
            value (str): The input string to validate.

        Returns:
            float or None: The validated positive number as a float, or None if invalid.
        """
        try:
            val = float(value)
            if val <= 0:
                return None
            return val
        except ValueError:
            return None

    def get_bmi_category(self, bmi):
        """
        Determines the BMI category based on the calculated BMI value.

        Args:
            bmi (float): The BMI value.

        Returns:
            str: The classification category (e.g., 'Underweight').
        """
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obesity"

    def calculate_bmi(self):
        """
        Performs the BMI calculation and updates the GUI with the result and category.
        Handles user input validation and displays error messages if necessary.
        """
        weight_str = self.weight_entry.get()
        height_str = self.height_entry.get()

        weight = self.validate_input(weight_str)
        height = self.validate_input(height_str)

        if weight is None or height is None:
            messagebox.showerror("Invalid Input", "Please enter valid positive numbers for weight and height.")
            self.result_label.config(text="")
            self.category_label.config(text="")
            return

        if height == 0:
            messagebox.showerror("Invalid Input", "Height cannot be zero.")
            self.result_label.config(text="")
            self.category_label.config(text="")
            return

        # BMI formula: weight (kg) / height (m)^2
        bmi = weight / (height ** 2)
        category = self.get_bmi_category(bmi)

        self.result_label.config(text=f"Your BMI is: {bmi:.2f}")
        self.category_label.config(text=f"Category: {category}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculatorApp(root)
    root.mainloop()
