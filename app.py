from tkinter import ttk
import tkinter as tk
import sqlite3

import null as null
def show():


        conn = sqlite3.connect("Purchases.db")

        cur = conn.cursor()
        cur.execute("SELECT * FROM Purchases")
        rows = cur.fetchall()
        for i in tree.get_children():
            tree.delete(i)
        for row in rows:
            print(row)  # it print all records in the database

            tree.insert("", tk.END, values=row)

        conn.close()
        connect()




def Insert():
    conn1 = sqlite3.connect('Purchases.db')
    c = conn1.cursor()
    c.execute("INSERT INTO Purchases VALUES (NULL,'2020','wail')")

# Save (commit) the changes
    conn1.commit()
    conn1.close()



def connect():
    import sqlite3
    conn = sqlite3.connect('Purchases.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS Purchases(ID INTEGER PRIMARY KEY AUTOINCREMENT, First TEXT, Surname TEXT)")
    conn.commit()
    conn.close()


# Create table

# Insert a row of data
   # c.execute("INSERT INTO Purchases VALUES ('2006-01-05','BUY','RHAT',100)")

# Save (commit) the changes




def View():
          Insert()
          conn = sqlite3.connect("Purchases.db")

          cur = conn.cursor()
          cur.execute("SELECT * FROM Purchases")
          rows = cur.fetchall()
          for i in tree.get_children():
              tree.delete(i)
          for row in rows:

           print(row) # it print all records in the database

           tree.insert("", tk.END, values=row)

          conn.close()

connect()










root = tk.Tk()
root.geometry("400x400")

tree= ttk.Treeview(root, column=("column1", "column2"), show='headings')
tree.heading("#1", text="NUMBER")
tree.heading("#2", text="FIRST NAME")


#Insert()
tree.pack()
b2 = tk.Button(text="view data", command=View)
show()
b2.pack()

root.mainloop()



