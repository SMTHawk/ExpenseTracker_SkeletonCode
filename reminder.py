import tkinter as tk
from threading import Thread
import time
from datetime import datetime

class ReminderInterface:
    def __init__(self, db):
        self.db = db
        self.reminders = []

    def add_reminder(self, message, remind_time, remind_date):
        """Add a new reminder with a specific message, date, and time."""
        self.add_reminder_to_db(message, remind_time, remind_date)
        return "Reminder added successfully"

    def add_reminder_to_db(self, message, remind_time, remind_date):
        """Add a new reminder to the database."""
        query = "INSERT INTO reminders (note, time, date) VALUES (?, ?, ?)"
        self.db.execute_query(query, (message, remind_time, remind_date))

    def delete_reminder(self, reminder_id):
        """Delete a reminder by its index."""
        try:
            del self.reminders[reminder_id]
            return "Reminder deleted successfully"
        except IndexError:
            return "Invalid reminder ID"

    def update_reminder(self, reminder_id, new_message=None, new_time=None):
        """Update an existing reminder."""
        try:
            if new_message:
                self.reminders[reminder_id]['message'] = new_message
            if new_time:
                self.reminders[reminder_id]['time'] = new_time
            return "Reminder updated successfully"
        except IndexError:
            return "Invalid reminder ID"

    def list_reminders(self):
        """Return a list of all reminders from the database."""
        query = "SELECT note, time, date FROM reminders"
        reminders_from_db = self.db.fetch_data(query)
        reminders_formatted = []
        if reminders_from_db:
            for reminder in reminders_from_db:
                formatted_reminder = {
                    'note': reminder[0],
                    'time': reminder[1],
                    'date': reminder[2]
                }
                reminders_formatted.append(formatted_reminder)
        return reminders_formatted

    def notify_user(self):
        """Check reminders continuously and notify the user if it's time."""
        def check_reminders():
            while True:
                current_time = time.strftime('%H:%M')
                for reminder in self.reminders:
                    if reminder['time'] == current_time:
                        self.show_notification(reminder['message'])
                time.sleep(60)  # Check every minute to avoid excessive CPU usage

        thread = Thread(target=check_reminders)
        thread.daemon = True
        thread.start()

    def show_notification(self, message):
        """Show a notification window when a reminder time is reached."""
        notification = tk.Toplevel(self.master)
        notification.title("Reminder")
        notification.geometry("300x200")
        tk.Label(notification, text=message, font=('Helvetica', 18)).pack(expand=True)
        tk.Button(notification, text="Okay", command=notification.destroy).pack()
