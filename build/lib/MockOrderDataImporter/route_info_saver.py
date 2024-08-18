# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 12:14:32 2024

@author: Administrator
Description:
This script collects route information for specified locations (e.g., restaurants, schools) using the OpenStreetMap API and calculates distances and durations using the OSRM API. The collected data is then written to a MySQL database table. The script encapsulates this functionality in the `RouteInfoToMySQL` class, which automates the entire process from data collection to database insertion.

Usage:
- Define the search parameters (location types, coordinates, radius).
- Configure the MySQL database connection.
- Run the `RouteInfoToMySQL` class to perform the operations.
"""

import os
import sys
current_file_path = os.path.abspath(sys.argv[0])
parent_directory = os.path.abspath(os.path.join(os.path.dirname(current_file_path), '../../MockOrderDataImporter/main'))
parent_directory2 = os.path.abspath(os.path.join(os.path.dirname(current_file_path), '../../MockOrderDataGenerator/main'))
sys.path.insert(0, parent_directory)
sys.path.insert(0, parent_directory2)
import pandas as pd
from df_to_mysql_writer import DataFrameToMySQL
from route_info_collector import RouteInfoCollector

class RouteInfoToMySQL:
    def __init__(self, queries, latitude, longitude, radius, db_config):
        self.queries = queries
        self.latitude = latitude
        self.longitude = longitude
        self.radius = radius
        self.db_config = db_config
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

    def write_to_mysql(self):
        # Create an instance of DataFrameToMySQL with connection details
        df_to_mysql = DataFrameToMySQL(
            host=self.db_config['host'],
            user=self.db_config['user'],
            password=self.db_config['password'],
            database=self.db_config['database'],
            table_name=self.db_config['table_name']
        )

        # Write the DataFrame to MySQL
        df_to_mysql.write_df_to_mysql(self.df_route_info)

    def run(self):
        self.collect_route_info()
        self.write_to_mysql()

# Usage example
if __name__ == "__main__":
    # Database configuration
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'root',
        'database': 'sm',
        'table_name': 'route_info'
    }

    # Parameters for the search
    queries = ["restaurant", "school"]
    latitude = -12.4634  # Latitude of Darwin
    longitude = 130.8456  # Longitude of Darwin
    radius = 1  # Search radius in degrees

    # Create an instance of RouteInfoToMySQL and run the process
    route_info_to_mysql = RouteInfoToMySQL(queries, latitude, longitude, radius, db_config)
    route_info_to_mysql.run()