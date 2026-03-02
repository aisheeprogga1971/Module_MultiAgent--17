
"""
    Datasets
"""

import pandas as pd
import sqlite3

def convert_csv_to_db(csv_path, db_name, table_name):
    df = pd.read_csv(csv_path)
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    
    conn = sqlite3.connect(db_name)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()
    print(f"{table_name} database created successfully!")

if __name__ == "__main__":
    convert_csv_to_db("csv/institutions.csv", "data/institutions.db", "institutions")
    convert_csv_to_db("csv/hospitals.csv", "data/hospitals.db", "hospitals")
    convert_csv_to_db("csv/restaurants.csv", "data/restaurants.db", "restaurants")