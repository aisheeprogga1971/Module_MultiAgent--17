import sqlite3

conn = sqlite3.connect("data/my_database.db")
cursor = conn.cursor()

# Attach the old databases
cursor.execute("ATTACH 'data/institutions.db' AS inst;")
cursor.execute("ATTACH 'data/hospitals.db' AS hosp;")
cursor.execute("ATTACH 'data/restaurants.db' AS rest;")

# Drop tables if they exist (so we can copy them again)
cursor.execute("DROP TABLE IF EXISTS institutions;")
cursor.execute("DROP TABLE IF EXISTS hospitals;")
cursor.execute("DROP TABLE IF EXISTS restaurants;")

# Copy tables into the new database
cursor.execute("CREATE TABLE institutions AS SELECT * FROM inst.institutions;")
cursor.execute("CREATE TABLE hospitals AS SELECT * FROM hosp.hospitals;")
cursor.execute("CREATE TABLE restaurants AS SELECT * FROM rest.restaurants;")

conn.commit()
conn.close()

print("All tables copied successfully into my_database.db")