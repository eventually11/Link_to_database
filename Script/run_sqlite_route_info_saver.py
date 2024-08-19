# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 07:50:50 2024

@author: Administrator
"""

import os
import sys
import pandas as pd
import yaml
import sqlite3
from MockOrderDataImporter.sqlite_route_info_saver import RouteInfoToSQLite

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

def main():
    # Database configuration
    db_path = load_config('../config/config.yaml')['sqlite_db_path']
    table_name = "route_info"

    # Parameters for the search
    queries = ["restaurant", "school"]
    latitude = -12.4634  # Latitude of Darwin
    longitude = 130.8456  # Longitude of Darwin
    radius = 1  # Search radius in degrees

    # Create an instance of RouteInfoToSQLite and run the process
    route_info_to_sqlite = RouteInfoToSQLite(queries, latitude, longitude, radius, db_path, table_name)
    route_info_to_sqlite.run()

if __name__ == "__main__":
    main()
