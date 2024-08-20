# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 02:03:09 2024

@author: Administrator
The goal is to test if the SQLiteExporter class correctly exports data from a SQLite database to both CSV and JSON formats.
"""

import unittest
import sqlite3
import pandas as pd
import os
from MockOrderDataImporter.sqlite_exporter import SQLiteExporter

class TestSQLiteExporter(unittest.TestCase):
    def setUp(self):

        self.db_path = ":memory:"
        self.exporter = SQLiteExporter(self.db_path)
        self.exporter.connect()


        self.exporter.conn.execute('''CREATE TABLE test_table (id INTEGER, name TEXT)''')
        self.exporter.conn.execute('''INSERT INTO test_table (id, name) VALUES (1, 'Alice'), (2, 'Bob')''')
        self.exporter.conn.commit()

    def test_query_to_csv(self):

        query = "SELECT * FROM test_table"
        csv_filename = "test_output.csv"
        
        self.exporter.query_to_csv(query, csv_filename)
        self.assertTrue(os.path.exists(csv_filename))


        df = pd.read_csv(csv_filename)
        self.assertEqual(len(df), 2) 
        self.assertListEqual(df['name'].tolist(), ['Alice', 'Bob'])


        os.remove(csv_filename)

    def test_query_to_json(self):

        query = "SELECT * FROM test_table"
        json_filename = "test_output.json"
        
        self.exporter.query_to_json(query, json_filename)
        self.assertTrue(os.path.exists(json_filename))


        df = pd.read_json(json_filename, lines=True)
        self.assertEqual(len(df), 2)  
        self.assertListEqual(df['name'].tolist(), ['Alice', 'Bob'])


        os.remove(json_filename)

    def tearDown(self):
        
        self.exporter.disconnect()

if __name__ == '__main__':
    unittest.main()
