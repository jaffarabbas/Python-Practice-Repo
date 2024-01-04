import pandas as pd
from concurrent.futures import ThreadPoolExecutor

# Function to read a sheet into a DataFrame
def read_sheet(sheet_name):
    return pd.read_excel('C:\\Users\\DARKLORD\\Downloads\\2023121128335ATL_IT.xlsx', sheet_name=sheet_name)

# List of sheet names
sheet_names = ['Part1','Part2','Part3','Part4','Part5','Part6','Part7','Part8','Part9','Part10','Part11','Part12','Part13','Part14']

# Number of threads (adjust as needed)
num_threads = 14

# Create a ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=num_threads) as executor:
    # Use executor.map to parallelize sheet reading
    dfs = list(executor.map(read_sheet, sheet_names))

# Concatenate DataFrames into a single DataFrame
combined_df = pd.concat(dfs, ignore_index=True)

# Convert the Pandas DataFrame to a DataTable
datatable = combined_df.to_dict(orient='records')

print(datatable)
