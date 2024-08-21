# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 09:07:15 2024

@author: Administrator
"""



import pandas as pd
import os
from MockOrderDataImporter.df_to_sqlite_writer import DataFrameToSQLite  # Ensure the path is correct

class DataToSQLite:
    def __init__(self, db_path, table_name):
        self.db_path = db_path
        self.table_name = table_name
        self.data = None

    def load_data(self):
        """Attempt to load the CSV file from different paths."""
        potential_paths = [
            '../../MockOrderDataGenerator/output/mock_partner_order.csv',
            '../../../MockOrderDataGenerator/output/mock_partner_order.csv',
            '../MockOrderDataGenerator/output/mock_partner_order.csv'
        ]

        for path in potential_paths:
            if os.path.exists(path):
                try:
                    self.data = pd.read_csv(path)
                    print(f"Data loaded from: {path}")
                    return
                except Exception as e:
                    print(f"Failed to read data from {path}: {e}")

        if self.data is None:
            raise FileNotFoundError("CSV file could not be found in any of the specified paths.")

    def save_to_sqlite(self):
        """Save the loaded data to the SQLite database."""
        if self.data is not None:
            df_to_sqlite = DataFrameToSQLite(db_path=self.db_path, table_name=self.table_name)
            df_to_sqlite.write_df_to_sqlite(self.data)
            print(f"Data successfully written to {self.table_name} in the SQLite database.")
        else:
            print("No data to save. Make sure to load data first.")

    def run(self):
        """Run the full data loading and saving process."""
        self.load_data()
        self.save_to_sqlite()


if __name__ == "__main__":
    # Configure SQLite database path and table name
    db_path = '../../output/sm.db'
    table_name = 'ods_saas_partner_order'

    # Create and run the DataToSQLite class instance
    data_to_sqlite = DataToSQLite(db_path=db_path, table_name=table_name)
    data_to_sqlite.run()