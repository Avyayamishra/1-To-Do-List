import sqlite3
from tabulate import tabulate
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db = os.path.join(BASE_DIR, "data.db")

cnxn = sqlite3.connect(db)
gamo = cnxn.cursor()

gamo.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL UNIQUE,
    description TEXT,
    is_completed TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")
cnxn.commit()
def createTask():
    try:
        a = input("Enter title: ")
        b = input("Enter description: ")
        c = input("If completed (Y/N): ")
        if c == "Y":
            gamo.execute("insert into tasks(title, description, is_completed) values (?,?,?)",(a, b, "Completed"))
            cnxn.commit()
            print("Task created successfuly.")
            mainMenu()
        elif c == "N":
            gamo.execute("insert into tasks(title, description, is_completed) values (?,?,?)", (a,b,"Incomplete"))
            cnxn.commit()
            print("Task created successfuly.")
            mainMenu()
        else:
            print("Error: Invalid choice selected.")
            (mainMenu)
    except Exception as e:
        print("Error occured: ", e)
def viewTask():
    try:
        gamo.execute("select * from tasks")
        u = gamo.fetchall()
        headers = ["Task ID", "Title", "Description", "Status", "Time"]
        print(tabulate(u, headers=headers, tablefmt = "fancy_grid"))
        mainMenu()
    except Exception as e:
        print("Error occured: ", e)
        mainMenu()
def deleteTask():
    try:
        x = int(input("Enter Task ID to delete: "))
        gamo.execute("DELETE FROM tasks WHERE id = ?", (x,))
        cnxn.commit()
        print("Task deleted successfuly.")
        mainMenu()
    except Exception as e:
        print("Error occured: ", e)
        mainMenu()
def mainMenu():
    print("""Available options:
    1) Create task
    2) View task
    3) Delete task
    """)
    d = int(input("Enter your choice: "))
    if d == 1:
        createTask()
    elif d == 2:
        viewTask()
    elif d == 3:
        deleteTask()
mainMenu()