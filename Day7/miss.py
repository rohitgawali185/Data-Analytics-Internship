import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "Amit", "Sneha"],
    "Age": [22, None, 24, None],
    "Salary": [25000, 30000, None, 28000]
}

df = pd.DataFrame(data)

print(df.isnull().sum())
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

print(df)
data = {
    "Name": ["Rahul", "Priya", "Rahul", "Amit"],
    "Age": [22, 23, 22, 24]
}

df = pd.DataFrame(data)

print("Duplicate records:", df.duplicated().sum())

df = df.drop_duplicates()

print(df)
data = {
    "Age": ["21", "22", "23"],
    "Salary": ["25000", "30000", "28000"]
}

df = pd.DataFrame(data)

df["Age"] = pd.to_numeric(df["Age"])
df["Salary"] = pd.to_numeric(df["Salary"])

print(df.dtypes)
data = {
    "City": [" pune ", "PUNE", "Mumbai ", "mumbai"]
}

df = pd.DataFrame(data)

df["City"] = df["City"].str.strip().str.title()

print(df)
data = {
    "Date": ["2026-01-15", "2026-02-20", "2026-03-10"]
}

df = pd.DataFrame(data)

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

print(df)
print(df.dtypes)