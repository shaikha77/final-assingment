import pickle
import tkinter as tk
from tkinter import messagebox

class EmployeeManagementFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.label = tk.Label(self, text="Employee Management")
        self.label.pack()

        # Dummy data for testing
        self.employees = [
            {"name": "John Doe", "employee_id": "001", "department": "HR", "job_title": "Manager", "basic_salary": 50000},
            {"name": "Jane Smith", "employee_id": "002", "department": "Finance", "job_title": "Accountant", "basic_salary": 45000}
        ]

        # Pickle the essential data needed to reconstruct the GUI
        data_to_pickle = {
            "employees": self.employees,
        }

        # Save the pickled data to a file
        with open("employee_data.pickle", "wb") as f:
            pickle.dump(data_to_pickle, f)

        # Display a message indicating successful pickling
        messagebox.showinfo("Success", "Employee data pickled successfully.")

class EventManagementFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.label = tk.Label(self, text="Event Management")
        self.label.pack()

        # Dummy data for testing
        self.events = [
            {"event_id": "E001", "type": "Conference", "theme": "Technology", "date": "2024-05-10", "venue_address": "123 Main St", "client_id": "C001"},
            {"event_id": "E002", "type": "Wedding", "theme": "Romantic", "date": "2024-06-15", "venue_address": "456 Park Ave", "client_id": "C002"}
        ]

        # Pickle the essential data needed to reconstruct the GUI
        data_to_pickle = {
            "events": self.events,
        }

        # Save the pickled data to a file
        with open("event_data.pickle", "wb") as f:
            pickle.dump(data_to_pickle, f)

        # Display a message indicating successful pickling
        messagebox.showinfo("Success", "Event data pickled successfully.")

# Create a root window for the GUI
root = tk.Tk()
root.withdraw()  # Hide the root window

# Create instances of each management frame
employee_frame = EmployeeManagementFrame(root)
event_frame = EventManagementFrame(root)

# Run the tkinter main loop
root.mainloop()
