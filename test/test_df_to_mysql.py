# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 11:45:30 2024

@author: Administrator

This script tests whether data from a
 Pandas DataFrame is correctly written to a 
 MySQL table by comparing the last two rows inserted.
"""

import os
import sys
current_file_path = os.path.abspath(sys.argv[0])
parent_directory = os.path.abspath(os.path.join(os.path.dirname(current_file_path), '../main'))
sys.path.insert(0, parent_directory)
import unittest
import pandas as pd
import mysql.connector
from df_to_mysql import DataFrameToMySQL  # Replace 'your_module' with the actual module name

class TestDataFrameToMySQL(unittest.TestCase):

    def setUp(self):
        # Sample DataFrame
        self.data = {'name': ['Alice', 'Bob'], 'age': [25, 30], 'city': ['New York', 'Los Angeles']}
        self.df = pd.DataFrame(self.data)

        # Initialize the DataFrameToMySQL class with connection details
        self.df_to_mysql = DataFrameToMySQL(
            host='localhost',
            user='root',
            password='root',
            database='sm',
            table_name='test_database'
        )

        # Write the DataFrame to MySQL
        self.df_to_mysql.write_df_to_mysql(self.df)

    def test_data_written_to_mysql(self):
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='sm'
        )
        cursor = connection.cursor()

        # Retrieve data from the MySQL table
        cursor.execute("SELECT name, age, city FROM test_database ORDER BY id DESC LIMIT 2;")
        rows = cursor.fetchall()

        # Expected data
        expected_data = [('Bob', 30, 'Los Angeles'),('Alice', 25, 'New York')]

        # Check if the retrieved data matches the expected data
        self.assertEqual(rows, expected_data)

        # Clean up by closing the cursor and connection
        cursor.close()
        connection.close()

if __name__ == '__main__':
    unittest.main()
