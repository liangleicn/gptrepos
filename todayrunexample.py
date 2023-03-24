import sqlite3
import datetime

# Connect to the SQLite database
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Get today's date in the same format as the boot_time column
today = datetime.datetime.now().strftime('%Y%m%d')

# Execute the query to retrieve rows where boot_time is today
cursor.execute("SELECT user_name FROM mytable WHERE boot_time = ?", (today,))
rows = cursor.fetchall()

# Print the results
if len(rows) > 0:
    print("The following users have booted up today:")
    for row in rows:
        print(row[0])
else:
    print("No users have booted up today.")

# Close the database connection
conn.close()
