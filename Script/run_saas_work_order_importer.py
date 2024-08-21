# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 11:04:13 2024

@author: Administrator
"""

from MockOrderDataImporter.saas_work_order_importer import DataToSQLite

if __name__ == "__main__":
    # Configure SQLite database path and table name
    db_path = '../output/sm.db'
    table_name = 'ods_work_order_order'

    # Create and run the DataToSQLite class instance
    data_to_sqlite = DataToSQLite(db_path=db_path, table_name=table_name)
    data_to_sqlite.run()