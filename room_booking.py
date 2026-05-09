# Conference Room Booking System

# Dictionary of lists to store bookings
# Key: Room Name, Value: List of tuples (user, start, end)
bookings = {
    "Room A": [],
    "Room B": []
}

def add_booking():
    room = input("Enter Room Name (Room A / Room B): ")
    if room not in bookings:
        print("Invalid Room.")
        return

    user = input("Enter User Name: ")
    start = int(input("Enter Start Time (e.g., 9): "))
    end = int(input("Enter End Time (e.g., 11): "))

    # Check for time conflicts
    conflict = False
    for b_user, b_start, b_end in bookings[room]:
        # Logic: if new start is before existing end AND new end is after existing start
        if start < b_end and end > b_start:
            conflict = True
            break

    if conflict:
        print("Error: Time slot overlap! Booking rejected.")
    else:
        bookings[room].append((user, start, end))
        print("Booking successful!")

# Main Loop
while True:
    action = input("\nType 'book' to add, 'view' to see schedule, or 'exit': ").lower()
    if action == 'book':
        add_booking()
    elif action == 'view':
        print("\n--- Full Schedule ---")
        print(bookings)
    elif action == 'exit':
        break