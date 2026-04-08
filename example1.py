# Python program for 4 students' marks

# Taking input for 4 students
students = {}

for i in range(4):
    name = input(f"Enter name of student {i+1}: ")
    marks = int(input(f"Enter marks of {name}: "))
    students[name] = marks

# Display student details
print("\nStudent Marks:")
for name, marks in students.items():
    print(f"{name}: {marks}")

# Calculate average marks
total = sum(students.values())
average = total / 4

print(f"\nTotal Marks = {total}")
print(f"Average Marks = {average}")

# Find highest and lowest marks
highest = max(students, key=students.get)
lowest = min(students, key=students.get)

print(f"Highest Marks: {highest} ({students[highest]})")
print(f"Lowest Marks: {lowest} ({students[lowest]})")