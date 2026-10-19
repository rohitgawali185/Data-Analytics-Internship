import pandas as pd

data = {
    "Name": ["Amit", "Priya", "Rahul", "Sneha"],
    "Age": [21, 22, None, 23],
    "Salary": [25000, None, 22000, 35000]
}

df = pd.DataFrame(data)

print(df.isnull())
print("\nMissing Values:")
print(df.isnull().sum())