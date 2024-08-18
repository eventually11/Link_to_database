# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 01:21:12 2024

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Description:
This script defines the `MySQLExporter` class, which is designed to connect to a MySQL database, execute SQL queries, and export the results to both CSV and JSON file formats. The class provides methods for establishing and closing a database connection, running queries, and saving the query results in a structured format suitable for further analysis or reporting.

Usage:
- Initialize the `MySQLExporter` class with database connection details.
- Use the `query_to_csv` method to export query results to a CSV file.
- Use the `query_to_json` method to export query results to a JSON file.
- Ensure the database connection is properly closed after operations are completed.

Example:
- The script demonstrates how to use the `MySQLExporter` class to run a query on a specified table and save the output in both CSV and JSON formats.
"""

import mysql.connector
import pandas as pd

class MySQLExporter:
    def __init__(self, db_config):
        self.db_config = db_config
        self.conn = None

    def connect(self):
        """Establish a connection to the database."""
        if self.conn is not None and self.conn.is_connected():
            print("Already connected to the database.")
            return
        
        self.conn = mysql.connector.connect(**self.db_config)
        print("Connected to the database.")

    def disconnect(self):
        """Close the database connection."""
        if self.conn is not None and self.conn.is_connected():
            self.conn.close()
            print("Disconnected from the database.")
        else:
            print("No connection to close.")
    
    def query_to_csv(self, query, csv_filename):
        """Execute a query and save the result to a CSV file."""
        if self.conn is None or not self.conn.is_connected():
            self.connect()
        
        df = pd.read_sql(query, self.conn)
        df.to_csv(csv_filename, index=False)
        print(f"Data saved to {csv_filename}.")

    def query_to_json(self, query, json_filename):
        """Execute a query and save the result to a JSON file."""
        if self.conn is None or not self.conn.is_connected():
            self.connect()
        
        df = pd.read_sql(query, self.conn)
        df.to_json(json_filename, orient='records', lines=True)
        print(f"Data saved to {json_filename}.")

# Usage example:
if __name__ == "__main__":
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'root',
        'database': 'sm'  
    }
    table='route_info'
    exporter = MySQLExporter(db_config)
    query = 'SELECT * FROM {0}'.format(table)  
    csv_filename = '{0}_output.csv'.format(table)
    json_filename = '{0}_output.json'.format(table)
    
    try:
        exporter.query_to_csv(query, csv_filename)
        exporter.query_to_json(query, json_filename)
    finally:
        exporter.disconnect()

