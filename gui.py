import tkinter as tk
from user import UserInterface
from popups import RegisterPopup, LoginPopup, ChangePasswordPopup

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("User")
        self.geometry("300x200")
    
        self.create_widgets()
    
    def create_widgets(self):
        self.user_interface = UserInterface(self)
        
        #Register
        register_btn = tk.Button(self, text="Register User", command=self.open_register_popup)
        register_btn.pack(pady=10)
        
        #Login
        login_btn = tk.Button(self, text="User Login", command=self.open_login_popup)
        login_btn.pack(pady=10)
        
        #Change pass
        change_pass_btn = tk.Button(self, text="Change Password", command=self.open_change_password_popup)
        change_pass_btn.pack(pady=10)
        
    def open_register_popup(self):
        self.user_interface.register_user()

    def open_login_popup(self):
        login_popup = LoginPopup(self, self.user_interface.login_user)

    def open_change_password_popup(self):
        self.user_interface.change_password()

if __name__ == "__main__":
    app = GUI()
    app.mainloop()