# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 01:39:31 2024

@author: Administrator
This unit test checks whether the MySQLExporter class successfully 
generates CSV and JSON files from a MySQL query, 
ensuring that the files are created and then cleaned up afterward.
"""

import unittest
import os
import sys
current_file_path = os.path.abspath(sys.argv[0])
parent_directory = os.path.abspath(os.path.join(os.path.dirname(current_file_path), '../../MockOrderDataImporter/main'))
sys.path.insert(0, parent_directory)

from mysql_exporter import MySQLExporter  # Adjust the import path as needed

class TestMySQLExporter(unittest.TestCase):

    def setUp(self):
        # Database configuration
        self.db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'root',
            'database': 'sm'  # Replace 'sm' with your database name
        }
        self.table = 'route_info'
        self.csv_filename = f'{self.table}_output.csv'
        self.json_filename = f'{self.table}_output.json'

        # Create an instance of MySQLExporter
        self.exporter = MySQLExporter(self.db_config)

    def test_files_generated(self):
        # Perform the export
        query = f'SELECT * FROM {self.table}'
        try:
            self.exporter.query_to_csv(query, self.csv_filename)
            self.exporter.query_to_json(query, self.json_filename)

            # Check if the files are created
            self.assertTrue(os.path.isfile(self.csv_filename), "CSV file was not created.")
            self.assertTrue(os.path.isfile(self.json_filename), "JSON file was not created.")
        finally:
            # Clean up by deleting the files after the test
            if os.path.isfile(self.csv_filename):
                os.remove(self.csv_filename)
            if os.path.isfile(self.json_filename):
                os.remove(self.json_filename)
            self.exporter.disconnect()

if __name__ == "__main__":
    unittest.main()
