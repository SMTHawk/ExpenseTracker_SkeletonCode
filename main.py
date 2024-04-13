import tkinter as tk
from expense_tracker.app import ExpenseTrackerApp
from expense_tracker.user import UserAuthentication

def main():
    root = tk.Tk()
    user_auth = UserAuthentication()
    app = ExpenseTrackerApp(root, user_auth)
    root.mainloop()

if __name__ == "__main__":
    main()
