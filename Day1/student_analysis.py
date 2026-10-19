
import pandas as pd

# Load student dataset
df = pd.read_csv("student_data.csv")

# Display the dataset
print("STUDENT DATA")
print(df)

# Count total students
print("\nTotal Students:", len(df))

# Calculate average marks
average_marks = df["Marks"].mean()
print("Average Marks:", round(average_marks, 2))

# Find highest and lowest marks
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())

# Classify students as Pass or Fail
df["Result"] = df["Marks"].apply(
    lambda marks: "Pass" if marks >= 40 else "Fail"
)

print("\nSTUDENT RESULTS")
print(df)

# Save the analysis results
df.to_csv("student_analysis_results.csv", index=False)

print("\nAnalysis completed successfully!")
