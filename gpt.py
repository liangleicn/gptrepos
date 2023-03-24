import sqlite3
import pandas as pd
import tkinter as tk
from tkinter import ttk

# Connect to the database
conn = sqlite3.connect('mydatabase.db')

# Query the database and convert the results to a DataFrame
query = 'SELECT * FROM mytable'
df = pd.read_sql(query, conn)

# Create the GUI window and table
root = tk.Tk()
root.title('SQLite Table Dashboard')
table = ttk.Treeview(root)

# Add columns to the table
table['columns'] = ('User Name', 'Platform Name', 'Starting Time', 'Version Number')

# Format the columns
table.column('#0', width=0, stretch=tk.NO)
table.column('User Name', anchor=tk.CENTER, width=100)
table.column('Platform Name', anchor=tk.CENTER, width=100)
table.column('Starting Time', anchor=tk.CENTER, width=150)
table.column('Version Number', anchor=tk.CENTER, width=100)

# Add headings to the columns
table.heading('#0', text='', anchor=tk.CENTER)
table.heading('User Name', text='User Name', anchor=tk.CENTER)
table.heading('Platform Name', text='Platform Name', anchor=tk.CENTER)
table.heading('Starting Time', text='Starting Time', anchor=tk.CENTER)
table.heading('Version Number', text='Version Number', anchor=tk.CENTER)

# Insert the data into the table
for index, row in df.iterrows():
    table.insert('', index, text='', values=(row['user_name'], row['platform_name'], row['starting_time'], row['version_number']))

# Pack the table and run the GUI loop
table.pack(expand=tk.YES, fill=tk.BOTH)
root.mainloop()
