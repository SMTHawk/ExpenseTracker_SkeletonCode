import tkinter as tk

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
