# Student Marks Analysis Using while Loop

student_name = "Rohit"

marks = [85, 90, 78, 95, 82]
subjects = ["English", "Mathematics", "Science", "Computer", "History"]

j = 0
total_marks = 0
highest_marks = 0
passed_subjects = 0

print("STUDENT PERFORMANCE REPORT")
print("---------------------------")
print("Student Name:", student_name)

while j < len(marks):
    print(subjects[j], "Marks:", marks[j])

    total_marks += marks[j]

    if marks[j] > highest_marks:
        highest_marks = marks[j]

    if marks[j] >= 35:
        passed_subjects += 1

    j += 1

average_marks = total_marks / len(marks)

print("---------------------------")
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)
print("Highest Marks:", highest_marks)
print("Subjects Passed:", passed_subjects)