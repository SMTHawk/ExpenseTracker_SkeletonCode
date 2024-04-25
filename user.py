from database import Database
from popups import RegisterPopup, LoginPopup, ChangePasswordPopup

class UserInterface:
    def __init__(self, master):
        self.master = master
        #Initialize user management GUI components

    def register_user(self):
        register_popup = RegisterPopup(self.master)

    def login_user(self):
        login_popup = LoginPopup(self.master)

    def update_profile(self):
        pass

    def change_password(self):
        change_pass_popup = ChangePasswordPopup(self.master)
