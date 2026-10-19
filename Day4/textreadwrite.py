# Writing data into a text file

file = open("student.txt", "w")
file.write("Student Name: Rohit\n")
file.write("Course: Python Programming\n")
file.write("Day: 4 - File Handling\n")
file.close()

# Reading data from the file

file = open("student.txt", "r")
data = file.read()

print(data)

file.close()