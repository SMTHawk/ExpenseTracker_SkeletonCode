import sqlite3

#Define schema
create_users_table = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
"""

def create_database(db_name):
    #Create file
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    #Execute SQL
    cursor.execute(create_users_table)
    
    #Commit changes and close
    conn.commit()
    conn.close()
    print(f"Database '{db_name}' created successfully with users table.")

if __name__ == "__main__":
    #Name of database
    db_name = "users.db"
    
    #Create the SQL database
    create_database(db_name)