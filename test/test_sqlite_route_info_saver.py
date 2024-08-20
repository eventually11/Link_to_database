# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 01:43:23 2024

@author: Administrator
The test uses mock objects and unit testing methods to verify the reliability of the core functional modules. It ensures that the code correctly handles data, connects to the database, and processes errors under different conditions.
"""

import unittest
import sqlite3
import pandas as pd
from unittest.mock import MagicMock
from MockOrderDataImporter.sqlite_route_info_saver import RouteInfoToSQLite, DataFrameToSQLite
from MockOrderDataGenerator.route_info_collector import RouteInfoCollector

class TestRouteInfoToSQLite(unittest.TestCase):
    def setUp(self):
        # Mock database path and table name
        self.db_path = ":memory:"  # 使用内存数据库进行测试
        self.table_name = "route_info"
        self.queries = ["restaurant", "school"]
        self.latitude = -12.4634
        self.longitude = 130.8456
        self.radius = 1

        # Create an instance of RouteInfoToSQLite for testing
        self.route_info_to_sqlite = RouteInfoToSQLite(
            self.queries, self.latitude, self.longitude, self.radius, self.db_path, self.table_name
        )

        # Mock the RouteInfoCollector methods
        self.route_info_to_sqlite.collector = MagicMock(spec=RouteInfoCollector)
        self.route_info_to_sqlite.collector.get_route_info.return_value = pd.DataFrame({
            "place_name": ["Test Restaurant", "Test School"],
            "distance_km": [0.5, 1.0],
            "duration_min": [2, 5]
        })

    def test_collect_route_info(self):
        # Test if the collect_route_info method correctly sets the DataFrame
        self.route_info_to_sqlite.collect_route_info()
        self.assertIsNotNone(self.route_info_to_sqlite.df_route_info)
        self.assertEqual(len(self.route_info_to_sqlite.df_route_info), 2)

    def test_write_df_to_sqlite(self):
        # Test if the data is written to SQLite successfully
        df_to_sqlite = DataFrameToSQLite(self.db_path, self.table_name)
        df = pd.DataFrame({
            "place_name": ["Test Restaurant", "Test School"],
            "distance_km": [0.5, 1.0],
            "duration_min": [2, 5]
        })
        df_to_sqlite.write_df_to_sqlite(df)

        # Check if data is written to the in-memory SQLite database
        connection = sqlite3.connect(self.db_path)
        result_df = pd.read_sql(f"SELECT * FROM {self.table_name}", connection)
        connection.close()

        self.assertEqual(len(result_df), 2)
        self.assertListEqual(list(result_df['place_name']), ["Test Restaurant", "Test School"])

    def test_run(self):
        # Test the full run method
        self.route_info_to_sqlite.collect_route_info = MagicMock()
        self.route_info_to_sqlite.write_to_sqlite = MagicMock()

        self.route_info_to_sqlite.run()

        self.route_info_to_sqlite.collect_route_info.assert_called_once()
        self.route_info_to_sqlite.write_to_sqlite.assert_called_once()

if __name__ == '__main__':
    unittest.main()
