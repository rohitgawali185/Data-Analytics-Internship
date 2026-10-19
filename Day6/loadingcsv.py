import pandas as pd

data = {
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Rohan"],
    "Age": [21, 22, 20, 23, 21],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [25000, 30000, 22000, 35000, 28000]
}

df = pd.DataFrame(data)
df.to_csv("employees.csv", index=False)

df = pd.read_csv("employees.csv")

print(df)