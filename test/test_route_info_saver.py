import os
import sys
current_file_path = os.path.abspath(sys.argv[0])
parent_directory = os.path.abspath(os.path.join(os.path.dirname(current_file_path), '../../MockOrderDataImporter/main'))
sys.path.insert(0, parent_directory)
import unittest
import mysql.connector
from route_info_saver import RouteInfoToMySQL  # Replace with the correct import path if needed

class TestRouteInfoToMySQL(unittest.TestCase):

    def setUp(self):
        # Database configuration
        self.db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'root',
            'database': 'sm',
            'table_name': 'route_info'
        }

        # Parameters for the search
        self.queries = ["restaurant", "school"]
        self.latitude = -12.4634  # Latitude of Darwin
        self.longitude = 130.8456  # Longitude of Darwin
        self.radius = 1  # Search radius in degrees

        # Create an instance of RouteInfoToMySQL and run the process
        self.route_info_to_mysql = RouteInfoToMySQL(self.queries, self.latitude, self.longitude, self.radius, self.db_config)
        self.route_info_to_mysql.run()

    def test_data_written_to_mysql(self):
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host=self.db_config['host'],
            user=self.db_config['user'],
            password=self.db_config['password'],
            database=self.db_config['database']
        )
        cursor = connection.cursor()

        # Check if there is at least one row in the table
        cursor.execute(f"SELECT COUNT(*) FROM {self.db_config['table_name']}")
        row_count = cursor.fetchone()[0]

        # Assert that there is at least one row in the table
        self.assertGreater(row_count, 0, "No data has been written to the MySQL table.")

        # Clean up by closing the cursor and connection
        cursor.close()
        connection.close()

if __name__ == "__main__":
    unittest.main()