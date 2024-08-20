# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 07:50:50 2024

@author: Administrator
The project focuses on the collection and storage of route information. It involves calling APIs to gather route data for specified locations and storing this data in an SQLite database. The project is divided into three modules: data collection, data transformation, and data storage.
"""

import os
import sys
import pandas as pd
import sqlite3
from MockOrderDataGenerator.route_info_collector import RouteInfoCollector

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
            print("SQLite connection is established")
        except sqlite3.Error as e:
            print(f"Error: {e}")

    def write_df_to_sqlite(self, df):
        try:
            self.connect()
            df.to_sql(self.table_name, self.connection, if_exists='append', index=False)
            print(f"DataFrame written to SQLite table: {self.table_name} successfully")
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

class RouteInfoToSQLite:
    def __init__(self, queries, latitude, longitude, radius, db_path, table_name):
        self.queries = queries
        self.latitude = latitude
        self.longitude = longitude
        self.radius = radius
        self.db_path = db_path
        self.table_name = table_name
        self.df_route_info = None

    def collect_route_info(self):
        # Create an instance of the RouteInfoCollector
        collector = RouteInfoCollector(self.queries, self.latitude, self.longitude, self.radius)
        
        # Perform the search and calculate routes
        collector.search_places()
        collector.calculate_routes()

        # Retrieve the final DataFrame with route information
        self.df_route_info = collector.get_route_info()
        # Replace NaN values with 0 in specific columns
        self.df_route_info[['distance_km', 'duration_min']] = self.df_route_info[['distance_km', 'duration_min']].fillna(0)

    def write_to_sqlite(self):
        # Create an instance of DataFrameToSQLite with connection details
        df_to_sqlite = DataFrameToSQLite(db_path=self.db_path, table_name=self.table_name)

        # Write the DataFrame to SQLite
        df_to_sqlite.write_df_to_sqlite(self.df_route_info)

    def run(self):
        self.collect_route_info()
        self.write_to_sqlite()

# Usage example
# if __name__ == "__main__":
#     # Database configuration
#     db_path = "route_info.db"
#     table_name = "route_info"

#     # Parameters for the search
#     queries = ["restaurant", "school"]
#     latitude = -12.4634  # Latitude of Darwin
#     longitude = 130.8456  # Longitude of Darwin
#     radius = 1  # Search radius in degrees

#     # Create an instance of RouteInfoToSQLite and run the process
#     route_info_to_sqlite = RouteInfoToSQLite(queries, latitude, longitude, radius, db_path, table_name)
#     route_info_to_sqlite.run()
