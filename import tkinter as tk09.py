import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry('450x800')
        self.root.title("PE'X")
        self.root.configure(bg='#101720')

        # Expense tracking variables
        self.total_expenses = 0
        self.expenses = []
        self.salary = 0
        self.expense_limit = 0
        self.income_sources = []
        self.budget = {}
        self.recurring_expenses = []

        self.create_login_widgets()

    def create_login_widgets(self):
        self.label_title = tk.Label(self.root, text="PEX TRACK", font=("Arial Black", 17), bg='#101720', fg='#CEE9B6')
        self.label_title.pack(pady=5)

        self.label_username = tk.Label(self.root, text="Username:", font=("Arial", 10), bg='#101720', fg='#8FC79A')
        self.label_username.pack(pady=5)
        self.entry_username = tk.Entry(self.root)
        self.entry_username.pack(pady=5)

        self.label_password = tk.Label(self.root, text="Password:", font=("Arial", 10), bg='#101720', fg='#8FC79A')
        self.label_password.pack(pady=5)
        self.entry_password = tk.Entry(self.root, show="*")
        self.entry_password.pack(pady=5)

        self.button_login = tk.Button(self.root, text="Login", command=self.login)
        self.button_login.pack(pady=5)

        self.button_register = tk.Button(self.root, text="Register", command=self.open_register_window)
        self.button_register.pack(pady=5)

    def exit(self):
        self.root.geometry("450x800")
        self.root.deiconify()

    def login(self):
        username = self.entry_username.get()
        messagebox.showinfo("Login", f"Welcome, {username}!")
        self.root.withdraw()
        self.open_salary_window()

    def open_register_window(self):
        self.root.withdraw()
        self.register_window = tk.Toplevel(self.root)
        self.register_window.geometry('450x800')
        self.register_window.title("Register")
        self.register_window.configure(bg='#5E9387')

        self.label_new_username = tk.Label(self.register_window, text="New Username:", bg='#5E9387', fg='#CEE9B6')
        self.label_new_username.pack(pady=(10, 0))
        self.entry_new_username = tk.Entry(self.register_window)
        self.entry_new_username.pack(pady=5)

        self.label_new_password = tk.Label(self.register_window, text="New Password:", bg='#5E9387', fg='#CEE9B6')
        self.label_new_password.pack(pady=(10, 0))
        self.entry_new_password = tk.Entry(self.register_window, show="*")
        self.entry_new_password.pack(pady=5)

        self.button_register_user = tk.Button(self.register_window, text="Register", command=self.register_user)
        self.button_register_user.pack(pady=5)

        self.button_exit_register = tk.Button(self.register_window, text="Exit", command=self.exit_register)
        self.button_exit_register.pack(pady=5)

    def exit_register(self):
        self.register_window.destroy()
        self.root.deiconify()

    def register_user(self):
        new_username = self.entry_new_username.get()
        new_password = self.entry_new_password.get()
        messagebox.showinfo("Registration", f"User {new_username} registered successfully!")
        self.register_window.destroy()
        self.root.deiconify()
        self.entry_username.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)

    def open_salary_window(self):
        self.salary_window = tk.Toplevel(self.root)
        self.salary_window.geometry('450x800')
        self.salary_window.title("Enter Salary")
        self.salary_window.configure(bg='#5E9387')

        self.label_salary = tk.Label(self.salary_window, text="Enter Your Salary:", bg='#5E9387', fg='#CEE9B6')
        self.label_salary.pack(pady=5)
        self.entry_salary = tk.Entry(self.salary_window)
        self.entry_salary.pack(pady=5)

        self.button_save_salary = tk.Button(self.salary_window, text="Save Salary", command=self.save_salary)
        self.button_save_salary.pack(pady=5)

        self.button_exit_salary = tk.Button(self.salary_window, text="Exit", command=self.exit_salary)
        self.button_exit_salary.pack(pady=5)

    def exit_salary(self):
        self.salary_window.destroy()
        self.root.deiconify()

    def save_salary(self):
        try:
            self.salary = float(self.entry_salary.get())
            self.entry_salary.delete(0, tk.END)
            self.salary_window.destroy()
            self.open_income_window()
        except ValueError:
            messagebox.showerror("Error", "Invalid salary input.")

    def open_income_window(self):
        self.income_window = tk.Toplevel(self.root)
        self.income_window.geometry("450x800")
        self.income_window.title("Enter Income Sources")
        self.income_window.configure(bg='#5E9387')

        self.label_income = tk.Label(self.income_window, text="Enter Income Source:", bg='#5E9387', fg='#CEE9B6')
        self.label_income.pack(pady=5)
        self.entry_income = tk.Entry(self.income_window)
        self.entry_income.pack(pady=5)

        self.label_income_amount = tk.Label(self.income_window, text="Enter Amount:", bg='#5E9387', fg='#CEE9B6')
        self.label_income_amount.pack(pady=5)
        self.entry_income_amount = tk.Entry(self.income_window)
        self.entry_income_amount.pack(pady=5)

        self.button_add_income = tk.Button(self.income_window, text="Add Income", command=self.add_income)
        self.button_add_income.pack(pady=5)

        self.button_done = tk.Button(self.income_window, text="Done", command=self.open_expenses_window)
        self.button_done.pack(pady=5)

        self.button_exit_income = tk.Button(self.income_window, text="Exit", command=self.exit_income)
        self.button_exit_income.pack(pady=5)

    def exit_income(self):
        self.income_window.destroy()
        self.root.deiconify()

    def add_income(self):
        try:
            income_source = self.entry_income.get()
            income_amount = float(self.entry_income_amount.get())
            self.income_window.destroy()
            self.open_expenses_window()
            self.income_sources.append((income_source, income_amount))
            self.entry_income.delete(0, tk.END)
            self.entry_income_amount.delete(0, tk.END)
            messagebox.showinfo("Income Added", f"Added income source: {income_source} - Amount: ${income_amount:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Invalid income input.")

    def open_expenses_window(self):
        self.expenses_window = tk.Toplevel(self.root)
        self.expenses_window.geometry("450x800")
        self.expenses_window.title("Enter Expenses")
        self.expenses_window.configure(bg='#5E9387')

        self.label_display_salary = tk.Label(self.expenses_window, text=f"Your Salary: ${self.salary:.2f}", bg='#5E9387', fg='#CEE9B6')
        self.label_display_salary.pack(pady=5)

        self.create_budget_inputs()

        self.label_category = tk.Label(self.expenses_window, text="Expense Category:", bg='#5E9387', fg='#CEE9B6')
        self.label_category.pack(pady=5)
        self.category_var = tk.StringVar(value="Food")
        self.category_menu = tk.OptionMenu(self.expenses_window, self.category_var, "Food", "Transportation", "Entertainment", "Other")
        self.category_menu.pack(pady=5)

        self.label_expense = tk.Label(self.expenses_window, text="Enter Expense Amount:", bg='#5E9387', fg='#CEE9B6')
        self.label_expense.pack(pady=5)
        self.entry_expense = tk.Entry(self.expenses_window)
        self.entry_expense.pack(pady=5)

        self.button_add_expense = tk.Button(self.expenses_window, text="Add Expense", command=self.add_expense)
        self.button_add_expense.pack(pady=5)

        self.listbox = tk.Listbox(self.expenses_window, width=50, height=10)
        self.listbox.pack(pady=5)

        self.total_label = tk.Label(self.expenses_window, text=f"Total Expenses: $0.00", bg='#5E9387', fg='#CEE9B6')
        self.total_label.pack(pady=5)

        self.remaining_label = tk.Label(self.expenses_window, text=f"Remaining Salary: ${self.salary:.2f}", bg='#5E9387', fg='#CEE9B6')
        self.remaining_label.pack(pady=5)

        self.button_analyze = tk.Button(self.expenses_window, text="Analyze Expenses", command=self.analyze_expenses)
        self.button_analyze.pack(pady=5)

        self.button_exit_expenses = tk.Button(self.expenses_window, text="Exit", command=self.exit_expenses)
        self.button_exit_expenses.pack(pady=5)

        # Button to manage recurring expenses
        self.button_recurring_expenses = tk.Button(self.expenses_window, text="Manage Recurring Expenses", command=self.open_recurring_expenses_window)
        self.button_recurring_expenses.pack(pady=5)

    def create_budget_inputs(self):
        self.budget_entries = {}
        for category in ["Food", "Transportation", "Entertainment", "Other"]:
            label = tk.Label(self.expenses_window, text=f"Set Budget for {category}:", bg='#5E9387', fg='#CEE9B6')
            label.pack(pady=5)
            entry = tk.Entry(self.expenses_window)
            entry.pack(pady=5)
            self.budget_entries[category] = entry

    def exit_expenses(self):
        self.expenses_window.destroy()
        self.root.deiconify()

    def add_expense(self):
        try:
            expense = float(self.entry_expense.get())
            if expense <= 0:
                raise ValueError("Expense must be positive.")

            category = self.category_var.get()
            self.expenses.append((category, expense))

            category_budget = self.budget.get(category, 0)
            total_category_expenses = sum(amount for cat, amount in self.expenses if cat == category)

            if total_category_expenses + expense > category_budget:
                messagebox.showwarning("Warning", f"You are exceeding your budget for {category}!")

            self.listbox.insert(tk.END, f"{category}: ${expense:.2f}")
            self.total_expenses += expense
            self.entry_expense.delete(0, tk.END)
            self.update_totals()

        except ValueError:
            messagebox.showerror("Error", "Invalid expense input.")

    def update_totals(self):
        remaining_salary = self.salary - self.total_expenses
        self.total_label.config(text=f"Total Expenses: ${self.total_expenses:.2f}")
        self.remaining_label.config(text=f"Remaining Salary: ${remaining_salary:.2f}")

        # Update budgets
        for category, entry in self.budget_entries.items():
            try:
                self.budget[category] = float(entry.get())
            except ValueError:
                self.budget[category] = 0

        # Calculate total of recurring expenses and check limits
        total_recurring = 0
        for name, amount, limit in self.recurring_expenses:
            total_recurring += amount
            if total_recurring > limit:
                messagebox.showwarning("Warning", f"You are exceeding the limit for {name}!")

        self.total_expenses += total_recurring  # Include recurring in total expenses

    def analyze_expenses(self):
        if not self.expenses:
            messagebox.showinfo("Analysis", "No expenses recorded yet.")
            return

        categories = {}
        for category, amount in self.expenses:
            if category in categories:
                categories[category] += amount
            else:
                categories[category] = amount

        labels = list(categories.keys())
        sizes = list(categories.values())

        plt.figure(figsize=(8, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title('Expense Distribution')
        plt.axis('equal')
        plt.show()

    def open_recurring_expenses_window(self):
        self.recurring_window = tk.Toplevel(self.root)
        self.recurring_window.geometry("450x800")
        self.recurring_window.title("Recurring Expenses")
        self.recurring_window.configure(bg='#5E9387')

        self.label_recurring = tk.Label(self.recurring_window, text="Recurring Expense:", bg='#5E9387', fg='#CEE9B6')
        self.label_recurring.pack(pady=5)
        self.entry_recurring_expense = tk.Entry(self.recurring_window)
        self.entry_recurring_expense.pack(pady=5)

        self.label_recurring_amount = tk.Label(self.recurring_window, text="Amount:", bg='#5E9387', fg='#CEE9B6')
        self.label_recurring_amount.pack(pady=5)
        self.entry_recurring_amount = tk.Entry(self.recurring_window)
        self.entry_recurring_amount.pack(pady=5)

        self.label_limit = tk.Label(self.recurring_window, text="Set Limit:", bg='#5E9387', fg='#CEE9B6')
        self.label_limit.pack(pady=5)
        self.entry_limit = tk.Entry(self.recurring_window)
        self.entry_limit.pack(pady=5)

        self.button_add_recurring = tk.Button(self.recurring_window, text="Add Recurring Expense", command=self.add_recurring_expense)
        self.button_add_recurring.pack(pady=5)

        self.button_done_recurring = tk.Button(self.recurring_window, text="Done", command=self.exit_recurring_expenses)
        self.button_done_recurring.pack(pady=5)

    def exit_recurring_expenses(self):
        self.recurring_window.destroy()
        self.root.deiconify()

    def add_recurring_expense(self):
        try:
            expense_name = self.entry_recurring_expense.get()
            expense_amount = float(self.entry_recurring_amount.get())
            limit = float(self.entry_limit.get())
            self.recurring_expenses.append((expense_name, expense_amount, limit))
            messagebox.showinfo("Recurring Expense Added", f"Added recurring expense: {expense_name} - Amount: ${expense_amount:.2f}, Limit: ${limit:.2f}")
            self.entry_recurring_expense.delete(0, tk.END)
            self.entry_recurring_amount.delete(0, tk.END)
            self.entry_limit.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Invalid input for recurring expense.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()