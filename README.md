# DatabaseConnector
## Overview

This project provides a class for connecting to a MySQL database and writing data from a Pandas DataFrame into a specified table. The main output of this project is SQL statements that are executed to insert data into the database. This makes it easier to automate and manage database operations, particularly for inserting large datasets.


## Output

The primary output of this project is SQL INSERT statements that are generated and executed to populate a MySQL or SQLite database table with data from a Pandas DataFrame.

Additionally, the project provides options to output the DataFrame data in different formats:

    JSON: The DataFrame can be converted to a JSON format for easy integration with other systems.
    CSV: The DataFrame can be exported to a CSV file, allowing for easy sharing and analysis in spreadsheet tools.

## Class
DataFrameToMySQL

Purpose: Handles the connection to a MySQL database, generates the appropriate SQL INSERT statements, and writes the DataFrame data into a specified table.

Key Methods:
        connect(): Establishes a connection to the MySQL database.
        write_df_to_mysql(df): Converts the DataFrame into SQL INSERT statements and writes the data to the MySQL table.
        close(): Closes the database connection.

## Usage

- Define a DataFrame: Prepare your data in a Pandas DataFrame.

- Initialize the Class: Set up the DataFrameToMySQL class with your database connection details.

- Write Data to MySQL: Use the write_df_to_mysql method to generate and execute SQL INSERT statements, inserting the DataFrame data into the database table.

- Export Data (Optional):

JSON: Use the export_to_json(df, filepath) method to save the DataFrame as a JSON file.
CSV: Use the export_to_csv(df, filepath) method to save the DataFrame as a CSV file.

## Example

python

### Sample DataFrame
        data = {'name': ['Alice', 'Bob'], 'age': [25, 30], 'city': ['New York', 'Los Angeles']}
        df = pd.DataFrame(data)

### Initialize the DataFrameToMySQL class with connection details
        df_to_mysql = DataFrameToMySQL(
            host='localhost',
            user='root',
            password='root',
            database='sm',  
            table_name='test_database'    
        )

### Write the DataFrame to MySQL
        df_to_mysql.write_df_to_mysql(df)

Notes

    Ensure the MySQL server is running and the database and table exist before running the script.
    Modify the host, user, password, database, and table_name parameters as per your environment.
    This class can be adapted for SQLite by modifying the connection logic and SQL syntax where necessary.
