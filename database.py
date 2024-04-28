import sqlite3

class Database:
    def __init__(self, db_name):
        #Initialize connection
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        print("Database connection established.")

    def execute_query(self, query):
        #Execute query
        try:
            self.cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully.")
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")

    def fetch_data(self, query):
        #Fetch data
        try:
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            print("Data fetched successfully.")
        except sqlite3.Error as e:
            print(f"Error fetcing data: {e}")
            return None

    def close_connection(self):
        #Close connection
        self.cursor.close()
        self.connection.close()
        print("Database connection closed.")