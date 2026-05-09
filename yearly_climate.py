import numpy as np

# Setting seed as per the assignment image
np.random.seed(42)
temps = np.random.randint(-5, 46, size=(3, 365))

# 1. Heatwave days (temp > 40)
heatwave_counts = np.sum(temps > 40, axis=1)
print(f"Heatwave days for each city: {heatwave_counts}")

# 2. Hottest day
hottest_val = temps.max()
# Find location (city, day)
hottest_idx = np.unravel_index(temps.argmax(), temps.shape)
print(f"Hottest Temp: {hottest_val}°C in City {hottest_idx[0]+1} on Day {hottest_idx[1]+1}")

# 3. Most stable climate (lowest standard deviation)
stds = temps.std(axis=1)
stable_city = np.argmin(stds)
print(f"Most stable city is City {stable_city + 1} with Std Dev: {stds[stable_city]:.2f}")

# 4. Rescale to Fahrenheit and top 5
temps_f = (temps * 9/5) + 32
# Flatten to find top 5 across everything
flat_temps_f = temps_f.flatten()
top_5_indices = np.argsort(flat_temps_f)[-5:][::-1]

print("\nTop 5 Hottest Days (Fahrenheit):")
for idx in top_5_indices:
    city = idx // 365
    day = idx % 365
    print(f"Temp: {flat_temps_f[idx]:.1f}°F, City: {city+1}, Day: {day+1}")