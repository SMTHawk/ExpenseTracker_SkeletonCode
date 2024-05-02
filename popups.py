import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import datetime

class PopupWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry("300x200")

class RegisterPopup(PopupWindow):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Register User")
        self.create_widgets()

    def create_widgets(self):
        self.username_label = tk.Label(self, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        self.password_label = tk.Label(self, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        self.register_button = tk.Button(self, text="Register", command=self.register_user)
        self.register_button.pack()

    def register_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.parent.user_interface.register_user(username, password):
            print("User registered successfully.")
            self.destroy()
        else:
            print("Registration failed.")

import tkinter as tk

class LoginPopup(tk.Toplevel):
    def __init__(self, parent, login_callback):
        super().__init__(parent)
        self.login_callback = login_callback
        self.parent = parent  # Store the parent widget
        self.title("Login User")
        self.geometry("300x200")
        self.create_widgets()

    def create_widgets(self):
        self.username_label = tk.Label(self, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        self.password_label = tk.Label(self, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self, text="Login", command=self.attempt_login)
        self.login_button.pack()

    def attempt_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        login_success = self.login_callback(username, password)
        if login_success:
            print("Login successful.")
            self.destroy()  # This should close the login window
        else:
            print("Invalid username or password.")
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)

class ChangePasswordPopup(PopupWindow):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Change Password")
        self.create_widgets()

    def create_widgets(self):
        # Widgets for changing password
        pass  # Implement similar to other popups

class AddTransactionWindow(tk.Toplevel):
    def __init__(self, parent, db):
        super().__init__(parent)
        self.db = db
        self.parent = parent
        self.title("Add Transaction")
        self.geometry("400x500")
        self.create_widgets()

    def create_widgets(self):
        # Predefined categories
        categories = ["Income", "Savings", "Food", "Bills", "Transportation", "Entertainment", "Extra Expenses"]

        # Transaction type
        tk.Label(self, text="Transaction Type:").pack()
        self.transaction_type = ttk.Combobox(self, values=["Expense", "Income"])
        self.transaction_type.pack()

        # Amount Entry
        tk.Label(self, text="Amount:").pack()
        self.amount_entry = tk.Entry(self)
        self.amount_entry.pack()

        # Category Dropdown
        tk.Label(self, text="Category:").pack()
        self.category = ttk.Combobox(self, values=categories)
        self.category.pack()

        # Note Entry
        tk.Label(self, text="Note:").pack()
        self.note = tk.Entry(self)
        self.note.pack()

        # Date Picker
        tk.Label(self, text="Date:").pack()
        self.date_picker = Calendar(self)  # Calendar widget
        self.date_picker.pack()

        # Button Frame
        button_frame = tk.Frame(self)
        button_frame.pack()

        # Save button
        save_button = tk.Button(button_frame, text="Save", command=self.save_transaction)
        save_button.pack(side=tk.LEFT, padx=10)

        # Cancel button
        cancel_button = tk.Button(button_frame, text="Cancel", command=self.destroy)
        cancel_button.pack(side=tk.LEFT)

    def save_transaction(self):
        transaction_type = self.transaction_type.get()
        amount = self.amount_entry.get()
        category = self.category.get()
        note = self.note.get()
        selected_date_str = self.date_picker.get_date()
        print("Selected date string:", selected_date_str)

        try:
        # Attempting to parse the date using the suspected correct format
            selected_date = datetime.strptime(selected_date_str, '%m/%d/%y')
            date = selected_date.strftime('%Y-%m-%d')
            print("Parsed date:", date)  # To confirm the output

            if self.transaction_type.get() and self.amount_entry.get() and self.category.get() and date:
                query = "INSERT INTO transactions (type, amount, category, note, date) VALUES (?, ?, ?, ?, ?)"
                self.db.execute_query(query, (self.transaction_type.get(), self.amount_entry.get(), self.category.get(), self.note.get(), date))
                messagebox.showinfo("Success", "Transaction saved successfully.")
                self.destroy()
            else:
             messagebox.showwarning("Warning", "All fields are required.")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid date format. Expected 'MM/DD/YY', got '{selected_date_str}'. Error: {str(e)}")
            print("Date parsing error:", str(e))  # To log the specific error
