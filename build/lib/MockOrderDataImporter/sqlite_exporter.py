# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 07:46:13 2024

@author: Administrator

This script is designed to export data from an SQLite database to both 
CSV and JSON formats using Python. It contains a reusable class 
 that handles the connection, query execution, and file saving operations.
"""

import sqlite3
import pandas as pd

class SQLiteExporter:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = None

    def connect(self):
        """Establish a connection to the SQLite database."""
        if self.conn is not None:
            print("Already connected to the database.")
            return
        
        self.conn = sqlite3.connect(self.db_path)
        print("Connected to the SQLite database.")

    def disconnect(self):
        """Close the SQLite database connection."""
        if self.conn is not None:
            self.conn.close()
            print("Disconnected from the SQLite database.")
        else:
            print("No connection to close.")
    
    def query_to_csv(self, query, csv_filename):
        """Execute a query and save the result to a CSV file."""
        if self.conn is None:
            self.connect()
        
        df = pd.read_sql(query, self.conn)
        df.to_csv(csv_filename, index=False)
        print(f"Data saved to {csv_filename}.")

    def query_to_json(self, query, json_filename):
        """Execute a query and save the result to a JSON file."""
        if self.conn is None:
            self.connect()
        
        df = pd.read_sql(query, self.conn)
        df.to_json(json_filename, orient='records', lines=True)
        print(f"Data saved to {json_filename}.")

# Usage example:
# if __name__ == "__main__":
#     db_path = 'C:\\Program Files\\DB Browser for SQLite\\sm.db'  # Path to the SQLite database file
#     table = 'route_info'
#     exporter = SQLiteExporter(db_path)
#     query = f'SELECT * FROM {table}'
#     csv_filename = f'{table}_output.csv'
#     json_filename = f'{table}_output.json'
    
#     try:
#         exporter.query_to_csv(query, csv_filename)
#         exporter.query_to_json(query, json_filename)
#     finally:
        # exporter.disconnect()
