import pandas as pd

# Step 1: Create sample dataset
data = {
    "Customer_ID": [101, 102, 103, 104, 105],
    "Customer_Name": ["Amit", "Priya", "Rahul", "Sneha", "Rohan"],
    "Age": [21, 22, None, 23, 21],
    "City": ["Pune", "Mumbai", "Pune", "Nashik", "Mumbai"],
    "Purchase_Amount": [1500, 2500, 1800, None, 3200]
}

df = pd.DataFrame(data)

# Step 2: Save and load CSV
df.to_csv("customer_data.csv", index=False)
df = pd.read_csv("customer_data.csv")

# Step 3: Explore the dataset
print("\nFIRST FIVE ROWS")
print(df.head())

print("\nLAST FIVE ROWS")
print(df.tail())

print("\nDATASET INFORMATION")
df.info()

print("\nSTATISTICAL SUMMARY")
print(df.describe())

# Step 4: Dataset dimensions
print("\nROWS:", df.shape[0])
print("COLUMNS:", df.shape[1])
print("COLUMN NAMES:", df.columns.tolist())

# Step 5: Data types
print("\nDATA TYPES")
print(df.dtypes)

# Step 6: Select columns
print("\nCUSTOMER NAMES")
print(df["Customer_Name"])

print("\nSELECTED COLUMNS")
print(df[["Customer_Name", "Purchase_Amount"]])

# Step 7: Missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Step 8: Duplicate rows
print("\nDUPLICATE ROWS:", df.duplicated().sum())

# Step 9: Create data dictionary
data_dictionary = pd.DataFrame({
    "Column_Name": df.columns,
    "Data_Type": df.dtypes.astype(str).values,
    "Description": [
        "Unique identifier assigned to each customer",
        "Name of the customer",
        "Age of the customer in years",
        "City where the customer lives",
        "Amount spent by the customer"
    ],
    "Missing_Values": df.isnull().sum().values
})

data_dictionary.to_csv("data_dictionary.csv", index=False)

print("\nDATA DICTIONARY")
print(data_dictionary)

print("\nEXPLORATION COMPLETED SUCCESSFULLY!")