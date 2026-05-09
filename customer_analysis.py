import pandas as pd

# 1. Load CSV (You will need to provide the actual data/file)
# df = pd.read_csv('orders.csv')

# For testing, I'm creating a dummy dataframe:
data = {
    'CustomerID': [101, 102, 103, 104],
    'OrderAmount': [500, None, 1200, 800],
    'OrderDate': ['2026-05-01', '2026-05-02', '2026-05-03', '2026-05-04'],
    'Region': ['North', 'South', 'North', 'East']
}
df = pd.DataFrame(data)

# 2. Basic info
print(df.info())
print(df.describe())

# 3. Drop missing OrderAmount
df = df.dropna(subset=['OrderAmount'])

# 4. Filter specific region
north_customers = df[df['Region'] == 'North']
print("\nNorth Region Customers:")
print(north_customers)

# 5. Sort by OrderAmount descending
df_sorted = df.sort_values(by='OrderAmount', ascending=False)

# 6. Average per region
avg_region = df.groupby('Region')['OrderAmount'].mean()
print("\nAverage Order Value per Region:")
print(avg_region)