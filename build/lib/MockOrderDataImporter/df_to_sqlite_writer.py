# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 07:40:30 2024

@author: Administrator
Description:
This script demonstrates how to write a Pandas DataFrame to a sqlite database table. 
It defines a class `DataFrameTosqlite` that connects to a sqlite database, writes the DataFrame 
to a specified table, and handles the connection lifecycle.

Class:
- DataFrameToMySQL: Handles the connection to sqlite and writes the DataFrame to a table.

Usage:
- Define a DataFrame with your data.
- Initialize the `DataFrameTosqlite` class with your sqlite connection details.
- Call the `write_df_to_sqlite` method to write the DataFrame to the sqlite table.

Example:
- In the `__main__` section, a sample DataFrame is created and written to the `test_database` table 
  in the sqlite database specified.


"""


import sqlite3
import pandas as pd

class DataFrameToSQLite:
    def __init__(self, db_path, table_name):
        self.db_path = db_path
        self.table_name = table_name
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_path)
            self.cursor = self.connection.cursor()
            print(f"SQLite connection is established to {self.db_path}")
        except sqlite3.Error as e:
            print(f"Error: {e}")

    def write_df_to_sqlite(self, df):
        try:
            self.connect()
            if self.connection:
                print(f"Writing DataFrame to SQLite table: {self.table_name}")
                df.to_sql(self.table_name, self.connection, if_exists='append', index=False)
                self.connection.commit()
                print("DataFrame written to SQLite successfully")
        except sqlite3.Error as e:
            print(f"Error: {e}")
        finally:
            self.close()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print("SQLite connection is closed")

# Usage example
if __name__ == '__main__':
    # Sample DataFrame
    data = {'name': ['Alice', 'Bob'], 'age': [25, 30], 'city': ['New York', 'Los Angeles']}
    df = pd.DataFrame(data)

    # Initialize the DataFrameToSQLite class with the database path and table name
    df_to_sqlite = DataFrameToSQLite(
        db_path='example.db',  # Path to the SQLite database file
        table_name='test_table'  # Table name
    )

    # Write the DataFrame to SQLite
    df_to_sqlite.write_df_to_sqlite(df)
