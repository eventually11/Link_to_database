# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 11:09:00 2024

@author: Administrator
Description:
This script demonstrates how to write a Pandas DataFrame to a MySQL database table. 
It defines a class `DataFrameToMySQL` that connects to a MySQL database, writes the DataFrame 
to a specified table, and handles the connection lifecycle.

Class:
- DataFrameToMySQL: Handles the connection to MySQL and writes the DataFrame to a table.

Usage:
- Define a DataFrame with your data.
- Initialize the `DataFrameToMySQL` class with your MySQL connection details.
- Call the `write_df_to_mysql` method to write the DataFrame to the MySQL table.

Example:
- In the `__main__` section, a sample DataFrame is created and written to the `test_database` table 
  in the MySQL database specified.

Notes:
- Ensure the MySQL server is running, and the database and table exist before running this script.
- Adjust the `host`, `user`, `password`, `database`, and `table_name` parameters to match your environment.
"""

import mysql.connector
from mysql.connector import Error
import pandas as pd

class DataFrameToMySQL:
    def __init__(self, host, user, password, database, table_name):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.table_name = table_name
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                print("MySQL connection is established")
        except Error as e:
            print(f"Error: {e}")

    def write_df_to_mysql(self, df):
        try:
            self.connect()
            if self.connection.is_connected():
                print(f"Writing DataFrame to MySQL table: {self.table_name}")
                for _, row in df.iterrows():
                    placeholders = ', '.join(['%s'] * len(row))
                    columns = ', '.join(row.index)
                    sql = f"INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders})"
                    self.cursor.execute(sql, tuple(row))
                self.connection.commit()
                print("DataFrame written to MySQL successfully")
        except Error as e:
            print(f"Error: {e}")
        finally:
            self.close()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection is not None and self.connection.is_connected():
            self.connection.close()
            print("MySQL connection is closed")

# Usage example
if __name__ == '__main__':
    # Sample DataFrame
    data = {'name': ['Alice', 'Bob'], 'age': [25, 30], 'city': ['New York', 'Los Angeles']}
    df = pd.DataFrame(data)

    # Initialize the DataFrameToMySQL class with connection details
    df_to_mysql = DataFrameToMySQL(
        host='localhost',
        user='root',
        password='root',
        database='sm',  
        table_name='test_database'    
    )

    # Write the DataFrame to MySQL
    df_to_mysql.write_df_to_mysql(df)
