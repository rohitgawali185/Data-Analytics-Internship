student_name = "Rohit"

english = 85
maths = 90
science = 78
computer = 95
history = 82

total_marks = english + maths + science + computer + history
average_marks = total_marks / 5
target_marks = 80

print("STUDENT PERFORMANCE REPORT")
print("--------------------------")
print("Student Name:", student_name)
print("English Marks:", english)
print("Maths Marks:", maths)
print("Science Marks:", science)
print("Computer Marks:", computer)
print("History Marks:", history)

print("Total Marks:", total_marks)
print("Average Marks:", average_marks)

if average_marks >= target_marks:
    print("Performance: Target Achieved")