# Student Marks Analysis Using for Loop

student_name = "Rohit"

marks = {
    "English": 85,
    "Mathematics": 90,
    "Science": 78,
    "Computer": 95,
    "History": 82
}

total_marks = 0
highest_marks = 0
high_score_count = 0

print("STUDENT MARKS REPORT")
print("----------------------")
print("Student Name:", student_name)

for subject, score in marks.items():
    print(subject, ":", score)

    total_marks += score

    if score > highest_marks:
        highest_marks = score

    if score >= 80:
        high_score_count += 1

average_marks = total_marks / len(marks)

print("----------------------")
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)
print("Highest Marks:", highest_marks)
print("Subjects with 80+ Marks:", high_score_count)