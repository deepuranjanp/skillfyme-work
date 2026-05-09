# Student Grading System

# 1. Ask the user to input their name and marks for 3 subjects
name = input("Enter student name: ")
subject1 = float(input("Enter marks for Subject 1: "))
subject2 = float(input("Enter marks for Subject 2: "))
subject3 = float(input("Enter marks for Subject 3: "))

# 2. Calculate the average of the three marks
average = (subject1 + subject2 + subject3) / 3

# 3. Use conditional statements to determine the grade
if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "D"

# 4. Print the result using formatted output
print("\n--- Student Report ---")
print(f"Name: {name}")
print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")