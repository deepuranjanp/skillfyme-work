# Parking Management System

total_vehicles = 0

print("--- Mall Parking Rate Calculator ---")
print("Type 'exit' as the entry time to stop the program.\n")

while True:
    entry_input = input("Enter Entry Time (e.g., 08 for 8 AM) or 'exit': ").lower()
    
    if entry_input == 'exit':
        break
        
    entry_time = int(entry_input)
    exit_time = int(input("Enter Exit Time (24-hour format, e.g., 14 for 2 PM): "))
    
    # Validation: Mall operates 6 AM to 12 AM (24)
    if entry_time < 6 or exit_time > 24 or entry_time >= exit_time:
        print("Entry Rejected: Mall is closed or invalid times entered.")
        continue
    
    duration = exit_time - entry_time
    total_vehicles += 1
    charge = 0
    
    # Calculating rates based on duration
    if duration <= 2:
        charge = duration * 20
    elif duration <= 5:
        # First 2 hours at 20 + next hours at 15
        charge = (2 * 20) + ((duration - 2) * 15)
    else:
        # First 2 at 20 + next 3 at 15 + remaining at 10
        charge = (2 * 20) + (3 * 15) + ((duration - 5) * 10)
    
    # Applying 50% discount for every 5th vehicle
    if total_vehicles % 5 == 0:
        print("Congratulations! You are our 5th customer. 50% discount applied.")
        charge = charge * 0.5
        
    print(f"Vehicle Number: {total_vehicles}")
    print(f"Total Duration: {duration} hours")
    print(f"Total Amount Due: ₹{charge}")
    print("-" * 30)

print(f"\nFinal Report: Total vehicles processed today: {total_vehicles}")