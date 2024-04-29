class TransactionInterface:
    def __init__(self, master, db):
        self.master = master
        self.db = db

    def add_transaction(self, user_id, amount, category, date):
        """Add a new transaction to the database."""
        query = "INSERT INTO transactions (user_id, amount, category, date) VALUES (?, ?, ?, ?)"
        try:
            self.db.execute_query(query, (user_id, amount, category, date))
            return "Transaction added successfully"
        except Exception as e:
            return f"Error: {str(e)}"

    def delete_transaction(self):
        pass

    def update_transaction(self):
        pass

    def list_transactions(self):
        pass
