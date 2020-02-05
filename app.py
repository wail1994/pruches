from tkinter import ttk
import tkinter as tk
import sqlite3

import null as null


def connect():
    import sqlite3
    conn = sqlite3.connect('Purchases.db')


    c = conn.cursor()

# Create table
    c.execute('''CREATE TABLE IF NOT EXISTS Purchases
             (name text, number text, date text, time text)''')

# Insert a row of data
    c.execute("INSERT INTO Purchases VALUES ('2006-01-05','BUY','RHAT',100)")

# Save (commit) the changes
    conn.commit()

    conn.close()

def View():
          conn = sqlite3.connect("Purchases.db")
          cur = conn.cursor()
          cur.execute("SELECT * FROM Purchases")
          rows = cur.fetchall()
          for row in rows:
           print(row) # it print all records in the database
           tree.insert("", tk.END, values=row)
          conn.close()









connect()
root = tk.Tk()
root.geometry("400x400")

tree= ttk.Treeview(root, column=("column1", "column2", "column3", "column4"), show='headings')
tree.heading("#1", text="NUMBER")
tree.heading("#2", text="FIRST NAME")
tree.heading("#3", text="NUMBER")
tree.heading("#4", text="FIRST NAME")
tree.pack()
View()
b2 = tk.Button(text="view data", command=View)
b2.pack()

root.mainloop()