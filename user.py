import sqlite3

class UserInterface:
    def __init__(self, master):
        self.master = master
        self.db = self.master.db  # Assuming the master has a db attribute

    def login_user(self, username, password):
        # Login verification logic
        query = "SELECT * FROM users WHERE username=? AND password=?"
        try:
            user = self.db.fetch_data(query, (username, password))
            if user:
                print("Login successful.")
                return True
            else:
                print("Invalid username or password.")
                return False
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return False

    def register_user(self, username, password):
        # Registration logic
        try:
            query = "INSERT INTO users (username, password) VALUES (?, ?)"
            self.db.execute_query(query, (username, password))
            print("User registered successfully.")
            return True
        except sqlite3.IntegrityError:
            print("Username already exists.")
            return False
        except Exception as e:
            print(f"Error registering user: {e}")
            return False

    def change_password(self, username, old_password, new_password):
        # Change password logic
        if self.login_user(username, old_password):  # First verify the old password
            try:
                query = "UPDATE users SET password=? WHERE username=?"
                self.db.execute_query(query, (new_password, username))
                print("Password changed successfully.")
                return True
            except Exception as e:
                print(f"Error changing password: {e}")
                return False
        else:
            print("Old password does not match.")
            return False
