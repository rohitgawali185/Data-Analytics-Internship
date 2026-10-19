
# Student Marks Analysis Using Tuple

student_name = "Rohit"

marks = (85, 90, 78, 95, 82)

print("STUDENT PERFORMANCE REPORT")
print("--------------------------")
print("Student Name:", student_name)

print("All Marks:", marks)
print("First Subject Marks:", marks[0])
print("Last Subject Marks:", marks[-1])

total_marks = sum(marks)
highest_marks = max(marks)
lowest_marks = min(marks)
average_marks = total_marks / len(marks)

print("--------------------------")
print("Total Marks:", total_marks)
print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)
print("Average Marks:", round(average_marks, 2))
print("Number of Subjects:", len(marks))

print("Marks 90 Exists:", 90 in marks)
print("Number of Times 85 Appears:", marks.count(85))
print("Index of 95:", marks.index(95))
