
# Student Performance Analysis Using Dictionary

student = {
    "name": "Rohit",
    "English": 85,
    "Mathematics": 90,
    "Science": 78,
    "Computer": 95,
    "History": 82
}

print("STUDENT PERFORMANCE REPORT")
print("--------------------------")

print("Student Name:", student["name"])
print("English Marks:", student["English"])
print("Mathematics Marks:", student["Mathematics"])
print("Science Marks:", student["Science"])
print("Computer Marks:", student["Computer"])
print("History Marks:", student["History"])

total_marks = (
    student["English"]
    + student["Mathematics"]
    + student["Science"]
    + student["Computer"]
    + student["History"]
)

average_marks = total_marks / 5

print("--------------------------")
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)

student["Geography"] = 88
print("After Adding Geography:", student)

student["Science"] = 80
print("Updated Science Marks:", student["Science"])

print("Number of Records:", len(student))
print("Student Name Exists:", "name" in student)
print("All Subject Details:", student.items())
