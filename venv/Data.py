import sqlite3
from tkinter import ttk
import tkinter as tk
conn = sqlite3.connect('Purchases.db')

conn.execute('''CREATE TABLE IF NOT EXISTS Purchases
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            TEXT     NOT NULL,
         ADDRESS        TEXT,
         SALARY         TEXT);''')
conn.execute("INSERT INTO Purchases (NAME,AGE,ADDRESS,SALARY) \
      VALUES ( 'Paul', '32', 'California', '20000.00' )");
conn.commit()
conn.close()


def View():
    conn = sqlite3.connect("Purchases.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Purchases")
    rows = cur.fetchall()
    for row in rows:
        print(row)  # it print all records in the database
        tree.insert("", tk.END, values=row)
    conn.close()




root = tk.Tk()
root.geometry("400x400")

tree= ttk.Treeview(root, column=("column1", "column2", "column3", "column4"), show='headings')
tree.heading("#1", text="NUMBER")
tree.heading("#2", text="FIRST NAME")
tree.heading("#3", text="NUMBER")
tree.heading("#4", text="FIRST NAME")

tree.pack()
View()
#b2 = tk.Button(text="view data", command=Insert)
b2.pack()

root.mainloop()

