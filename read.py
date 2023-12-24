import sqlite3
import time
from const import TABLE_NAME

import pandas as pd

start = time.time()
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

rows = cursor.execute(f'''
SELECT * FROM {TABLE_NAME};
''').fetchall()

# Replace column_names with the actual column names of your table
column_names = [desc[0] for desc in cursor.description]

# Create a DataFrame
df = pd.DataFrame(rows, columns=column_names)
df['timestamp'] = pd.to_datetime(df['timestamp'])

elapsed = time.time() - start

print(f'Execution time: {elapsed} seconds')
conn.close()

# Print the type of the DataFrame
print("Type of element:")
print(type(df['timestamp'].iloc[0]))

# Print the size of the DataFrame (number of rows and columns)
print("\nSize of DataFrame:")
print(f"Number of rows: {df['timestamp'].shape[0]}")