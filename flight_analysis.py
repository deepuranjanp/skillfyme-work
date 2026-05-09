import pandas as pd

# 1. Load and Clean
# df = pd.read_csv('flights.csv')

# Dummy data for testing
flight_data = {
    'FlightID': ['AI101', '6E202', 'UK303', 'AI102'],
    'Airline': ['Air India', 'IndiGo', 'Vistara', 'Air India'],
    'Destination': ['Delhi', 'Mumbai', 'Jaipur', 'Delhi'],
    'DelayInMinutes': [45, 15, 70, 10]
}
df = pd.DataFrame(flight_data)
df = df.dropna(subset=['DelayInMinutes'])

# 2. Filter > 30 mins
delayed_30 = df[df['DelayInMinutes'] > 30]

# 3, 4, 5. Group by Airline
stats = df.groupby('Airline')['DelayInMinutes'].agg(['count', 'mean'])
print("\nAirline Delay Stats:")
print(stats)

# 6. Destination with highest cumulative delay
top_dest = df.groupby('Destination')['DelayInMinutes'].sum().idxmax()
print(f"\nDestination with highest cumulative delay: {top_dest}")

# 7. Severity Column
def get_severity(mins):
    if mins < 30: return "Low"
    elif mins <= 60: return "Medium"
    else: return "High"

df['Severity'] = df['DelayInMinutes'].apply(get_severity)
print("\nFinal Data with Severity:")
print(df)