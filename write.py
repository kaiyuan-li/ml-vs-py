import sqlite3
from const import TABLE_NAME
from datetime import datetime

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('test.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()
# Drop the existing table if it exists
drop_table_query = f'''
    DROP TABLE IF EXISTS {TABLE_NAME};
'''

cursor.execute(drop_table_query)

# Commit the changes to the database
conn.commit()

# Define the SQL statement to create a table with timestamp and value columns
create_table_query = f'''
    CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
        timestamp TIMESTAMP,
        value INTEGER
    );
'''

# Execute the SQL statement to create the table
cursor.execute(create_table_query)

# Commit the changes and close the connection
conn.commit()

size = 1_000_000;
print(f"number of rows: {size}")
for _ in range(size):
    # Insert a  sample row into the table with 6 decimals after seconds
    current_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    sample_value = 0

    insert_query = f'''
        INSERT INTO {TABLE_NAME} (timestamp, value) VALUES (?, ?);
    '''

    cursor.execute(insert_query, (current_timestamp, sample_value))

# Commit the changes and close the connection
conn.commit()
conn.close()