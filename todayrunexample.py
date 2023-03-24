import sqlite3
from datetime import datetime, timedelta

# Connect to the database
conn = sqlite3.connect('mydatabase.db')
c = conn.cursor()

# Define the time window to check
end_date = datetime.now()
start_date = end_date - timedelta(days=7)

# Define the exclude lists
machine_list_name = ['machine1', 'machine2', 'machine3']
developer_list_name = ['dev1', 'dev2', 'dev3']
already_involved_list_name = ['user1', 'user2', 'user3']

# Query the database
c.execute("SELECT DISTINCT user_name FROM mytable WHERE boot_time >= ? AND boot_time <= ?", (start_date.strftime("%Y%m%d"), end_date.strftime("%Y%m%d")))
users = [row[0] for row in c.fetchall() if row[0] not in machine_list_name and row[0] not in developer_list_name and row[0] not in already_involved_list_name]

# Print the resulting user list
print(users)

# Close the connection to the database
conn.close()
