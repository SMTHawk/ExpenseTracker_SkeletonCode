import tkinter as tk
from database import Database

class PopupWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry("300x200")

class RegisterPopup(PopupWindow):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Register User")
        self.db = Database("users.db")
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
        self.db.execute_query(f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')")
        print("User registered successfully.")
        self.destroy()

class LoginPopup(PopupWindow):
    def __init__(self, parent, callback):
        super().__init__(parent)
        self.title("Login User")
        self.db = Database("users.db")
        self.create_widgets(callback)

    def create_widgets(self, callback):
        self.username_label = tk.Label(self, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        self.password_label = tk.Label(self, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self, text="Login", command=lambda: callback(self.username_entry.get(), self.password_entry.get()))
        self.login_button.pack()

class ChangePasswordPopup(PopupWindow):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Change Password")
        self.db = Database("users.db")
        self.create_widgets()

    def create_widgets(self):
        self.username_label = tk.Label(self, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        self.current_password_label = tk.Label(self, text="Current Password:")
        self.current_password_label.pack()
        self.current_password_entry = tk.Entry(self, show="*")
        self.current_password_entry.pack()

        self.new_password_label = tk.Label(self, text="New Password:")
        self.new_password_label.pack()
        self.new_password_entry = tk.Entry(self, show="*")
        self.new_password_entry.pack()

        self.confirm_password_label = tk.Label(self, text="Confirm Password:")
        self.confirm_password_label.pack()
        self.confirm_password_entry = tk.Entry(self, show="*")
        self.confirm_password_entry.pack()

        self.change_password_button = tk.Button(self, text="Change Password", command=self.change_password)
        self.change_password_button.pack()

    def change_password(self):
        username = self.username_entry.get()
        current_password = self.current_password_entry.get()
        new_password = self.new_password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        
        data = self.db.fetch_data(f"SELECT * FROM users WHERE username='{username}' AND password='{current_password}'")
        if not data:
            print("Invalid username or password.")
            return

        if new_password != confirm_password:
            print("Passwords do not match.")
            return

        self.db.execute_query(f"UPDATE users SET password='{new_password}' WHERE username='{username}'")
        print("Password updated successfully.")
