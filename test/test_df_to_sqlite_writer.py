# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 01:51:04 2024

@author: Administrator

"""

import unittest
import sqlite3
import pandas as pd
from MockOrderDataImporter.df_to_sqlite_writer import DataFrameToSQLite

class TestDataFrameToSQLite(unittest.TestCase):
    def setUp(self):

        self.db_path = "../output/sm.db"
        self.table_name = "test_table"
        self.df_to_sqlite = DataFrameToSQLite(self.db_path, self.table_name)
        
   
        self.sample_data = {'name': ['Alice', 'Bob'], 'age': [25, 30], 'city': ['New York', 'Los Angeles']}
        self.sample_df = pd.DataFrame(self.sample_data)
        
    def test_connection(self):
    
        self.df_to_sqlite.connect()
        self.assertIsNotNone(self.df_to_sqlite.connection)
        self.df_to_sqlite.close()

    def test_write_df_to_sqlite(self):
      
        self.df_to_sqlite.write_df_to_sqlite(self.sample_df)
        

        conn = sqlite3.connect(self.db_path)
        result_df = pd.read_sql(f"SELECT * FROM {self.table_name}", conn)
        conn.close()
        

        pd.testing.assert_frame_equal(result_df, self.sample_df)
        
    def tearDown(self):
 
        self.df_to_sqlite.close()

if __name__ == '__main__':
    unittest.main()
