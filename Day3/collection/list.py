
# Student Marks Analysis Using List

student_name = "Rohit"

marks = [85, 90, 78, 95, 82]

print("STUDENT PERFORMANCE REPORT")
print("--------------------------")
print("Student Name:", student_name)

print("All Marks:", marks)
print("First Subject Marks:", marks[0])
print("Last Subject Marks:", marks[-1])

marks.append(88)

print("Marks After Adding New Score:", marks)

marks[2] = 80

print("Marks After Updating Score:", marks)

total_marks = sum(marks)
highest_marks = max(marks)
lowest_marks = min(marks)
average_marks = total_marks / len(marks)

print("--------------------------")
print("Total Marks:", total_marks)
print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)
print("Average Marks:", average_marks)
print("Number of Subjects:", len(marks))
