import tkinter as tk
from threading import Thread
import time

class ReminderInterface:
    def __init__(self, master):
        self.master = master
        self.reminders = []  # Store reminders as a list of dicts

    def add_reminder(self, message, remind_time):
        """Add a new reminder with a specific message and time."""
        self.reminders.append({'message': message, 'time': remind_time})
        return "Reminder added successfully"

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
        """Return a list of all reminders."""
        return self.reminders

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
