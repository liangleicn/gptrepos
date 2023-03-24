import sqlite3
import datetime

# Connect to the SQLite database
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Get the current date and time in the same format as the boot_time column
now = datetime.datetime.now().strftime('%Y%m%d%H')

# Execute the query to retrieve rows where boot_time is now
cursor.execute("SELECT user_name FROM mytable WHERE boot_time = ?", (now,))
rows = cursor.fetchall()

# Print the results
if len(rows) > 0:
    print("The following users have booted up now:")
    for row in rows:
        print(row[0])
else:
    print("No users have booted up now.")

# Close the database connection
conn.close()
