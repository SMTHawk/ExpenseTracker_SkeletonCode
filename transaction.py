from popups import AddTransactionWindow
import tkinter as tk

class TransactionInterface:
    def __init__(self, master, db, categories):
        self.master = master
        self.db = db
        self.categories = categories

    def add_transaction(self, user_id, amount, category, date):
        """Add a new transaction to the database."""
        query = "INSERT INTO transactions (user_id, amount, category, date) VALUES (?, ?, ?, ?)"
        try:
            self.db.execute_query(query, (user_id, amount, category, date))
            return "Transaction added successfully"
        except Exception as e:
            return f"Error: {str(e)}"
        
    def add_transaction_window(self):
        add_transaction_window = AddTransactionWindow(self.master, self.db)
        add_transaction_window.grab_set()

    def delete_transaction(self, transaction_id):
        """Delete a transaction from the database."""
        query = "DELETE FROM transactions WHERE id = ?"
        try:
            self.db.execute_query(query, (transaction_id,))
            return "Transaction deleted successfully"
        except Exception as e:
            return f"Error: {str(e)}"

    def update_transaction(self, transaction_id, new_amount=None, new_category=None, new_date=None):
        """Update a transaction in the database."""
        updates = []
        params = []

        if new_amount is not None:
            updates.append("amount = ?")
            params.append(new_amount)
        if new_category is not None:
            updates.append("category = ?")
            params.append(new_category)
        if new_date is not None:
            updates.append("date = ?")
            params.append(new_date)

        params.append(transaction_id)
        query = f"UPDATE transactions SET {', '.join(updates)} WHERE id = ?"

        try:
            self.db.execute_query(query, tuple(params))
            return "Transaction updated successfully"
        except Exception as e:
            return f"Error: {str(e)}"

    def list_transactions(self, user_id=None):
        """List all transactions from the database, filtered by user ID."""
        query = "SELECT * FROM transactions"
        params = ()

        if user_id is not None:
            query += " WHERE user_id = ?"
            params = (user_id,)

        try:
            return self.db.fetch_data(query, params)
        except Exception as e:
            return f"Error: {str(e)}"

    def view_transactions(self):
        transactions_window = tk.Toplevel(self.master)
        transactions_window.title("View Transactions")
        
        #fetch and display transactions
        transactions = self.list_transactions()
        if transactions:
            #display transactions
            text_widget = tk.Text(transactions_window, height=10, width=50)
            text_widget.pack(expand=True, fill="both")

            for transaction in transactions:
                text_widget.insert(tk.END, f"ID: {transaction[0]}, Amount: {transaction[2]}, Category: {transaction[3]}, Date: {transaction[4]}\n")
        else:
            tk.Label(transactions_window, text="No transactions found").pack(padx=10, pady=10)
