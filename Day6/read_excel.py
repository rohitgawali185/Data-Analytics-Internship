import pandas as pd

df = pd.read_csv("employees.csv")
df.to_excel("employees.xlsx", index=False)

excel_df = pd.read_excel("employees.xlsx")

# print(excel_df)
# print(df.head(3))
# print(df.tail(2))
# df.info()
#print(df.describe())
# print("Number of Rows:", df.shape[0])
# print("Number of Columns:", df.shape[1])
# print("Column Names:", list(df.columns))
# print("Data Types:")
# print(df.dtypes)
#print(df["Name"])
# print(df[["Name", "Salary"]])
