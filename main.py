import sqlite3
import tabulate

cnxn = sqlite3.connect("data.db")
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
gamo.commit()
def createTask():
    try:
        a = input("Enter title: ")
        b = input("Enter description: ")
        c = input("If completed (Y/N): ")
        if c == "Y":
            gamo.execute("insert into tasks(title, description, is_completed) values (?,?,?)",(a, b, "Completed"))
        elif c == "N":
            gamo.execute("insert into tasks(title, description, is_completed) values (?,?,?)", (a,b,"Incomplete"))
        else:
            print("Error: Invalid choice selected.")
    except Exception as e:
        print("Error occured: ", e)
def viewTask():
    try:
        gamo.execute("select * from tasks")
        u = gamo.fetchall()
        headers = ["Task ID", "Title", "Description", "Status", "Time"]
        print(tabulate(u, headers=headers, tablefmt = "github"))
    except Exception as e:
        print("Error occured: ", e)
def deleteTask():
    try:
        x = int(input("Enter Task ID to delete: "))
        gamo.execute("delete from tasks where id = (?)", (x))
    except Exception as e:
        print("Error occured: ", e)
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