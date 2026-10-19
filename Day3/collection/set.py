
# Student Marks Analysis Using Set

student_name = "Rohit"

marks = {85, 90, 78, 95, 82, 90, 85}

print("STUDENT PERFORMANCE REPORT")
print("--------------------------")
print("Student Name:", student_name)

print("Unique Marks:", marks)
print("Total Unique Marks:", len(marks))

marks.add(88)
print("After Adding Marks:", marks)

marks.remove(78)
print("After Removing 78:", marks)

print("90 Exists:", 90 in marks)
print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))
print("Sum of Unique Marks:", sum(marks))

print("--------------------------")
print("Set Analysis Completed")
