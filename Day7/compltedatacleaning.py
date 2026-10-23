import pandas as pd

# Create sample dataset
data = {
    "Name": ["Rahul", "Priya", "Rahul", "Amit", "Sneha"],
    "Age": [22, None, 22, 24, 23],
    "City": [" pune ", "PUNE", " pune ", "Mumbai", "mumbai"],
    "Salary": [25000, 30000, 25000, None, 28000],
    "Date": [
        "2026-01-10",
        "2026-02-15",
        "2026-01-10",
        "2026-03-20",
        "invalid"
    ]
}

df = pd.DataFrame(data)

# Display original dataset
print("BEFORE CLEANING")
print(df)

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

print("\nDuplicate Records Before Cleaning:")
print(df.duplicated().sum())

# Remove exact duplicate rows
df = df.drop_duplicates().copy()

# Correct numerical data types
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")

# Handle missing numerical values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Salary"] = df["Salary"].fillna(df["Salary"].median())

# Standardize text categories
df["City"] = df["City"].str.strip().str.title()

# Convert dates
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Display cleaned dataset
print("\nAFTER CLEANING")
print(df)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nData Types After Cleaning:")
print(df.dtypes)

# Save cleaned dataset
df.to_csv("cleaned_data.csv", index=False)

print("\nCleaned dataset saved successfully.")
df.to_csv("cleaned_data.csv", index=False)