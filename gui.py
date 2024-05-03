import tkinter as tk
from popups import RegisterPopup, LoginPopup, AddTransactionWindow, ChangePasswordPopup, AddReminderPopup
from transaction import TransactionInterface
from reminder import ReminderInterface
from database import Database
from user import UserInterface

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Expense Tracker")
        self.geometry("500x400")
        
        self.db = Database("users.db")
        self.user_interface = UserInterface(self)
        self.categories = []
        self.transaction_interface = TransactionInterface(self, self.db, self.categories)
        self.reminder_interface = ReminderInterface(self.db)
        
        self.initial_buttons = []
        self.create_initial_buttons()
        self.reminder_interface.notify_user()

    def create_initial_buttons(self):
        login_btn = tk.Button(self, text="User Login", command=self.open_login_popup)
        login_btn.pack(pady=20)
        self.initial_buttons.append(login_btn)
        
        register_btn = tk.Button(self, text="Register User", command=self.open_register_popup)
        register_btn.pack(pady=20)
        self.initial_buttons.append(register_btn)

    def create_widgets(self):
        for button in self.initial_buttons:
            button.pack_forget()  # Hide initial buttons
        # Add transaction management buttons, etc.
        self.add_trans_btn = tk.Button(self, text="Add Transaction", command=self.transaction_interface.add_transaction_window)
        self.add_trans_btn.pack(pady=5)

        view_transactions_btn = tk.Button(self, text="View Transactions", command=self.transaction_interface.view_transactions)
        view_transactions_btn.pack(pady=5)

        self.add_reminder_btn = tk.Button(self, text="Add Reminder", command=self.open_add_reminder_popup)
        self.add_reminder_btn.pack(pady=5)

        self.list_reminders_btn = tk.Button(self, text="List Reminders", command=self.show_reminders)
        self.list_reminders_btn.pack(pady=5)
        
    def open_register_popup(self):
        register_popup = RegisterPopup(self)
        register_popup.grab_set()

    def open_login_popup(self):
        login_popup = LoginPopup(self, self.login_user)  # Pass the login_user method
        login_popup.grab_set()
        
    def open_add_reminder_popup(self):
        add_reminder_popup = AddReminderPopup(self, self.reminder_interface)
        add_reminder_popup.grab_set()


    def login_user(self, username, password):
        if self.user_interface.login_user(username, password):
            print("Login successful, loading features...")
            self.create_widgets()  # Load other UI components
            return True
        else:
            print("Login failed. Please try again.")
            return False

    def show_reminders(self):
        reminders_window = tk.Toplevel(self)
        reminders_window.title("All Reminders")
        reminders_window.geometry("300x200")
        reminder_texts = "\n".join([f"{rem['note']} - {rem['date']} {rem['time']}" for rem in self.reminder_interface.list_reminders()])
        tk.Label(reminders_window, text=reminder_texts, justify=tk.LEFT, font=('Helvetica', 12)).pack(padx=10, pady=10)

if __name__ == "__main__":
    app = GUI()
    app.mainloop()
