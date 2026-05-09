import numpy as np

# 1. Generate 7-day data for 3 cities (3x7)
# Let's assume temperatures are between 15 and 40 degrees
temp_data = np.random.randint(15, 40, size=(3, 7))
print("Temperature Data (Cities as rows, Days as columns):")
print(temp_data)

# 2. Calculations
avg_per_city = temp_data.mean(axis=1)
max_temp = temp_data.max()
diff_city1_city2 = temp_data[0] - temp_data[1]

print(f"\nAverage Temp per City: {avg_per_city}")
print(f"Maximum Temp of the Week: {max_temp}")
print(f"Difference (City 1 - City 2): {diff_city1_city2}")

# 3. Reshape to display day-wise (7x3)
day_wise = temp_data.reshape(7, 3)
print("\nDay-wise Temperatures (7 Days x 3 Cities):")
print(day_wise)