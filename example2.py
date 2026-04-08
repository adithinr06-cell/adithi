def check_attendance(attended_classes, total_classes):
    if total_classes == 0:
        print("Total classes cannot be zero.")
        return None

    percentage = (attended_classes / total_classes) * 100
    print(f"Attendance Percentage: {percentage:.2f}%")

    if percentage >= 75:
        print("Status: Eligible")
        return "Eligible"
    elif 65 <= percentage < 75:
        print("Status: Short Attendance")
        return "Short Attendance"
    else:
        print("Status: Detained")
        return "Detained"


# Call the function
attended = int(input("Enter attended classes: "))
total = int(input("Enter total classes: "))

result = check_attendance(attended, total)
print("Returned Value:", result)

#result = check_attendance(60, 80)
#print("Returned Value:", result)