import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Let panda read file
df = pd.read_csv("project.csv")

#Step 2: Clean up data
df.columns = df.columns.str.strip()

#Extra: create a map that can change the panda data type to the database data types
data_type = {
    "object": "varchar",
    "int64": 'int',
    "float64": "float",
    "datetime64": "timestamp",
    "timedelta64[ns]": "varchar"
}

# Change the data type
change = ", ".join("{} {}".format(n,d) for (n,d) in zip(df.columns, df.dtypes.replace(data_type)))
print(change)

#Step 3:Connect to a SQL database
conn = sqlite3.connect("data.db")
cursor = conn.cursor()

#Step 4: Load data to SQL file
#if_exists has three modes: replace, fail, append
df.to_sql("project", conn, if_exists="append")



# Step 5: clean and insert data
# query = "SELECT index, Period, Data_value FROM project"
df = pd.read_sql_query("SELECT Data_value, Period FROM project", conn)
# Step 6: Plot the data
df.plot(kind = 'pie', y = "Data_value", figsize=(12,6))
plt.show()
#Step ?: Close the connection
conn.close()

