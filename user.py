import sqlite3
from database import Database
from popups import RegisterPopup, LoginPopup, ChangePasswordPopup

# Define schema
create_users_table = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
"""

def create_database(db_name):
    try:
        # Create file
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        # Execute SQL
        cursor.execute(create_users_table)
        
        # Commit changes and close
        conn.commit()
        conn.close()
        print(f"Database '{db_name}' created successfully with users table.")
    except sqlite3.Error as e:
        print(f"Error creating database: {e}")

if __name__ == "__main__":
    # Name of database
    db_name = "users.db"
    
    # Create the SQL database
    create_database(db_name)

class Database:
    def __init__(self, db_name):
        # Initialize database connection
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        print("Database connection established.")

    def execute_query(self, query):
        # Execute SQL query
        try:
            self.cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully.")
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")

    def fetch_data(self, query):
        # Fetch data from the database
        try:
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            print("Data fetched successfully.")
            return data
        except sqlite3.Error as e:
            print(f"Error fetching data: {e}")
            return None

    def close_connection(self):
        # Close database connection
        self.cursor.close()
        self.connection.close()
        print("Database connection closed.")

class UserInterface:
    def __init__(self, master):
        self.master = master
        self.db = Database("users.db")
        
    def register_user(self):
        register_popup = RegisterPopup(self.master)

    def login_user(self, username, password):
        # Check credentials against the database
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        print("Executing query:", query)  
        data = self.db.fetch_data(query)
        if data:
            print("Login successful.")
        else:
            print("Invalid username or password.")

    def update_profile(self):
        pass

    def change_password(self):
        change_pass_popup = ChangePasswordPopup(self.master)
