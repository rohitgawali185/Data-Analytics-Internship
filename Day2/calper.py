name = input("Enter student name: ")

m1 = float(input("Enter subject 1 marks: "))
m2 = float(input("Enter subject 2 marks: "))
m3 = float(input("Enter subject 3 marks: "))

total = m1 + m2 + m3
percentage = total / 3

print("Student:", name)
print("Total Marks:", total)
print("Percentage:", round(percentage, 2))