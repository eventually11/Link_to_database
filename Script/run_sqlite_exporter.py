# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 07:51:33 2024

@author: Administrator
"""

import os
import yaml
from MockOrderDataImporter.sqlite_exporter import SQLiteExporter

def load_config(config_file):
    """
    Loads the configuration from a YAML file.

    Parameters
    ----------
    config_file : str
        The path to the configuration file.

    Returns
    -------
    dict
        The loaded configuration settings.
    """
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config


def export_database_data(config):
    """
    Exports data from an SQLite database to CSV and JSON files.

    Parameters
    ----------
    config : dict
        Configuration dictionary loaded from the YAML file.
    """
    db_path = config # Path to the SQLite database file
    table = 'route_info'
    exporter = SQLiteExporter(db_path)
    query = f'SELECT * FROM {table}'
    csv_filename = f'{table}_output.csv'
    json_filename = f'{table}_output.json'

    try:
        exporter.query_to_csv(query, csv_filename)
        exporter.query_to_json(query, json_filename)
    finally:
        exporter.disconnect()
        print(f"Data exported to '{csv_filename}' and '{json_filename}'.")

def main():
    # Load configuration settings
    config = load_config('../config/config.yaml')
    
    # Export data from SQLite database
    export_database_data(config['sqlite_db_path'])

if __name__ == "__main__":
    main()
