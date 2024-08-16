#Required Library
import sqlite3
from datetime import datetime
#Creating the Database
def initialize_db():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task TEXT NOT NULL,
                    priority TEXT CHECK(priority IN ('low', 'medium', 'high')),
                    due_date TEXT,
                    completed INTEGER CHECK(completed IN (0, 1))
                )''')
    conn.commit()
    conn.close()
#Adding a Task
def add_task(task, priority='medium', due_date=None):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("INSERT INTO tasks (task, priority, due_date, completed) VALUES (?, ?, ?, 0)", 
              (task, priority, due_date))
    conn.commit()
    conn.close()
    print(f"Task '{task}' added.")
#Removing a Task
def remove_task(task_id):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()
    print(f"Task ID {task_id} removed.")
#Marking a Task as Completed
def complete_task(task_id):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("UPDATE tasks SET completed=1 WHERE id=?", (task_id,))
    conn.commit()
    conn.close()
    print(f"Task ID {task_id} marked as completed.")
#List all Task
def list_tasks():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tasks ORDER BY priority, due_date")
    tasks = c.fetchall()
    conn.close()
    
    print("\nTask List:")
    for task in tasks:
        status = "✓" if task[4] == 1 else "✗"
        print(f"ID: {task[0]} | Task: {task[1]} | Priority: {task[2]} | Due: {task[3]} | Completed: {status}")
#Main Program loop
def main():
    initialize_db()
    
    while True:
        print("\nCommands: add, remove, complete, list, quit")
        cmd = input("Enter command: ").strip().lower()
        
        if cmd == "add":
            task = input("Enter task: ")
            priority = input("Enter priority (low, medium, high): ").strip().lower()
            due_date = input("Enter due date (YYYY-MM-DD) [optional]: ")
            add_task(task, priority, due_date)
        
        elif cmd == "remove":
            task_id = int(input("Enter task ID to remove: "))
            remove_task(task_id)
        
        elif cmd == "complete":
            task_id = int(input("Enter task ID to mark as completed: "))
            complete_task(task_id)
        
        elif cmd == "list":
            list_tasks()
        
        elif cmd == "quit":
            break
        
        else:
            print("Unknown command.")
#Run the Application
if __name__ == "__main__":
    main()


