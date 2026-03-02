

import sqlite3

conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()

# Show tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables:", tables)

# Function to print first 5 rows from a table
def print_first_rows(table_name):
    try:
        cursor.execute(f"SELECT * FROM {table_name} LIMIT 5;")
        rows = cursor.fetchall()
        print(f"\nFirst 5 rows from {table_name}:")
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(f"Error accessing {table_name}: {e}")

# Print rows from each table
for table in ['institutions', 'hospitals', 'restaurants']:
    print_first_rows(table)

"""
Instruction for agent: return only 10 suggestion list
"""
conn.close()