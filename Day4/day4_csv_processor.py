
import csv
import os

# ==================================
# DAY 4 - CSV DATA PROCESSOR
# ==================================

file_name = "students.csv"

try:
    # Check whether file exists
    if not os.path.exists(file_name):
        raise FileNotFoundError(
            f"{file_name} does not exist."
        )

    total_marks = 0
    valid_students = 0
    invalid_students = 0

    print("STUDENT DATA REPORT")
    print("-" * 40)

    # Read CSV file
    with open(file_name, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        required_columns = {"Name", "Age", "Marks"}

        if not reader.fieldnames or not required_columns.issubset(reader.fieldnames):
            raise ValueError(
                "CSV must contain Name, Age and Marks columns."
            )

        for row in reader:
            try:
                name = row["Name"].strip()
                age = int(row["Age"])
                marks = float(row["Marks"])

                # Validate data
                if not name or age <= 0 or not 0 <= marks <= 100:
                    raise ValueError("Invalid student details.")

                print(
                    f"Name: {name}, Age: {age}, Marks: {marks}"
                )

                total_marks += marks
                valid_students += 1

            except (ValueError, TypeError):
                invalid_students += 1
                print("Invalid record skipped:", row)

    # Calculate average
    if valid_students > 0:
        average_marks = total_marks / valid_students
        print("-" * 40)
        print("Valid Students:", valid_students)
        print("Invalid Students:", invalid_students)
        print("Total Marks:", total_marks)
        print(f"Average Marks: {average_marks:.2f}")
    else:
        print("No valid student records found.")

except FileNotFoundError as error:
    print("File Error:", error)

except PermissionError:
    print("Error: Permission denied while reading the file.")

except (OSError, csv.Error, ValueError) as error:
    print("Processing Error:", error)

finally:
    print("CSV processing completed.")
