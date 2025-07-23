import tkinter as tk
from tkinter import messagebox

# In-memory data store
users = {}

# Task statuses
statuses = ["New", "In Progress", "Hold", "In Testing", "Completed"]

# Function: Add User
def add_user():
    username = user_entry.get().strip()
    if not username:
        messagebox.showerror("Error", "Username cannot be empty!")
        return
    if username in users:
        messagebox.showerror("Error", "User already exists!")
    else:
        users[username] = []
        user_entry.delete(0, tk.END)
        messagebox.showinfo("Success", f"User '{username}' added successfully!")

# Function: Add Task
def add_task():
    username = user_entry.get().strip()
    task_name = task_entry.get().strip()
    if username not in users:
        messagebox.showerror("Error", "User does not exist!")
        return
    if not task_name:
        messagebox.showerror("Error", "Task name cannot be empty!")
        return
    task = {"task": task_name, "status": "New"}
    users[username].append(task)
    task_entry.delete(0, tk.END)
    messagebox.showinfo("Success", "Task added successfully!")

# Function: View All Tasks
def view_all_tasks():
    if not users:
        messagebox.showinfo("Info", "No users or tasks available.")
        return
    window = tk.Toplevel(app)
    window.title("All Tasks")
    task_list = tk.Text(window, width=80, height=20)
    task_list.pack(padx=10, pady=10)
    for user, tasks in users.items():
        task_list.insert(tk.END, f"User: {user}\n")
        for idx, task in enumerate(tasks, 1):
            task_list.insert(tk.END, f"  {idx}. Task: {task['task']} | Status: {task['status']}\n")
        task_list.insert(tk.END, "-" * 60 + "\n")

# Function: Update Task Status
def update_status():
    username = user_entry.get().strip()
    if username not in users:
        messagebox.showerror("Error", "User does not exist!")
        return
    try:
        index = int(task_index_entry.get().strip()) - 1
    except ValueError:
        messagebox.showerror("Error", "Invalid task number!")
        return
    if index < 0 or index >= len(users[username]):
        messagebox.showerror("Error", "Task number out of range!")
        return
    users[username][index]["status"] = status_var.get()
    messagebox.showinfo("Success", "Task status updated!")

# Function: Delete User and Their Tasks
def delete_user_tasks():
    username = user_entry.get().strip()
    if username not in users:
        messagebox.showerror("Error", "User does not exist!")
        return
    del users[username]
    messagebox.showinfo("Success", f"User '{username}' and all their tasks have been deleted!")

# Main App Window
app = tk.Tk()
app.title("Task Management System")
app.geometry("500x400")

# --- Widgets ---

# User input
tk.Label(app, text="User Name:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
user_entry = tk.Entry(app, width=30)
user_entry.grid(row=0, column=1, padx=10, pady=5)
tk.Button(app, text="Add User", command=add_user).grid(row=0, column=2, padx=10)

# Task input
tk.Label(app, text="Task Name:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
task_entry = tk.Entry(app, width=30)
task_entry.grid(row=1, column=1, padx=10, pady=5)
tk.Button(app, text="Add Task", command=add_task).grid(row=1, column=2, padx=10)

# View All
tk.Button(app, text="View All Tasks", command=view_all_tasks).grid(row=2, column=0, columnspan=3, pady=10)

# Update Task Status
tk.Label(app, text="Task Number:").grid(row=3, column=0, padx=10, pady=5, sticky='e')
task_index_entry = tk.Entry(app, width=10)
task_index_entry.grid(row=3, column=1, sticky='w')

status_var = tk.StringVar(app)
status_var.set(statuses[0])
tk.OptionMenu(app, status_var, *statuses).grid(row=3, column=2, padx=10)

tk.Button(app, text="Update Status", command=update_status).grid(row=4, column=0, columnspan=3, pady=10)

# Delete user & tasks
tk.Button(app, text="Delete User & Tasks", command=delete_user_tasks).grid(row=5, column=0, columnspan=3, pady=10)

# Run the App
app.mainloop()
