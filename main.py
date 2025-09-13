import sqlite3
import tabulate

cnxn = sqlite3.connect("data.db")
gamo = cnxn.cursor()

gamo.execute("create table if not exists")