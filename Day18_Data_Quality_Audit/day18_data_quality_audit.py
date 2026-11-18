
# ============================================================
# DAY 18 - DATA QUALITY AUDIT
# Project: Retail Sales & Customer Analysis
# ============================================================

import pandas as pd
from pathlib import Path

# ------------------------------------------------------------
# 1. PROJECT PATH
# ------------------------------------------------------------

base_path = Path(__file__).resolve().parents[2]

dataset_path = (
    base_path
    / "data"
    / "raw"
    / "archive"
    / "Sample - Superstore.csv"
)

report_path = base_path / "report" / "Day18_Data_Quality_Audit"
report_path.mkdir(parents=True, exist_ok=True)

# ------------------------------------------------------------
# 2. LOAD DATASET
# ------------------------------------------------------------

data = pd.read_csv(dataset_path, encoding="latin1")

print("=" * 65)
print("             DAY 18 - DATA QUALITY AUDIT")
print("=" * 65)

# ------------------------------------------------------------
# 3. RECORDS AND COLUMNS
# ------------------------------------------------------------

print("\n1. DATASET OVERVIEW")

print("Total Records:", data.shape[0])
print("Total Columns:", data.shape[1])

# ------------------------------------------------------------
# 4. MISSING VALUES
# ------------------------------------------------------------

print("\n2. MISSING VALUES")

missing_values = data.isnull().sum()

print(missing_values[missing_values > 0])

# ------------------------------------------------------------
# 5. DUPLICATE RECORDS
# ------------------------------------------------------------

print("\n3. DUPLICATE RECORDS")

duplicate_count = data.duplicated().sum()

print("Total Duplicate Records:", duplicate_count)

# ------------------------------------------------------------
# 6. DATA TYPES
# ------------------------------------------------------------

print("\n4. DATA TYPES")

print(data.dtypes)

# ------------------------------------------------------------
# 7. INVALID DATE CHECK
# ------------------------------------------------------------

print("\n5. INVALID DATE CHECK")

date_columns = ["Order Date", "Ship Date"]

for column in date_columns:

    if column in data.columns:

        converted_dates = pd.to_datetime(
            data[column],
            errors="coerce"
        )

        invalid_count = (
            data[column].notna() & converted_dates.isna()
        ).sum()

        print(column, "Invalid Dates:", invalid_count)

# ------------------------------------------------------------
# 8. NEGATIVE VALUES
# ------------------------------------------------------------

print("\n6. NEGATIVE VALUES")

numeric_columns = ["Sales", "Quantity", "Discount", "Profit"]

for column in numeric_columns:

    if column in data.columns:

        negative_count = (data[column] < 0).sum()

        print(column, "Negative Values:", negative_count)

# ------------------------------------------------------------
# 9. UNUSUAL VALUES - IQR METHOD
# ------------------------------------------------------------

print("\n7. UNUSUAL VALUES (IQR METHOD)")

for column in ["Sales", "Quantity", "Discount", "Profit"]:

    if column in data.columns:

        first_quartile = data[column].quantile(0.25)
        third_quartile = data[column].quantile(0.75)

        iqr = third_quartile - first_quartile

        lower_limit = first_quartile - 1.5 * iqr
        upper_limit = third_quartile + 1.5 * iqr

        unusual_count = (
            (data[column] < lower_limit) |
            (data[column] > upper_limit)
        ).sum()

        print(column, "Potential Outliers:", unusual_count)

# ------------------------------------------------------------
# 10. CREATE DATA QUALITY AUDIT REPORT
# ------------------------------------------------------------

audit_results = []

audit_results.append({
    "Issue": "Dataset Overview",
    "Column": "All Columns",
    "Count": data.shape[0],
    "Details": f"{data.shape[0]} records and {data.shape[1]} columns"
})

for column in data.columns:

    missing_count = data[column].isnull().sum()

    if missing_count > 0:

        audit_results.append({
            "Issue": "Missing Values",
            "Column": column,
            "Count": missing_count,
            "Details": "Missing values detected"
        })

audit_results.append({
    "Issue": "Duplicate Records",
    "Column": "All Columns",
    "Count": duplicate_count,
    "Details": "Complete duplicate rows"
})

for column in date_columns:

    if column in data.columns:

        converted_dates = pd.to_datetime(
            data[column],
            errors="coerce"
        )

        invalid_count = (
            data[column].notna() & converted_dates.isna()
        ).sum()

        audit_results.append({
            "Issue": "Invalid Dates",
            "Column": column,
            "Count": invalid_count,
            "Details": "Dates that could not be converted"
        })

for column in numeric_columns:

    if column in data.columns:

        negative_count = (data[column] < 0).sum()

        audit_results.append({
            "Issue": "Negative Values",
            "Column": column,
            "Count": negative_count,
            "Details": "Negative numeric values; requires investigation"
        })

# DATA TYPE ISSUES

for column in date_columns:

    if column in data.columns:

        if not pd.api.types.is_datetime64_any_dtype(data[column]):

            audit_results.append({
                "Issue": "Data Type",
                "Column": column,
                "Count": 1,
                "Details": "Date column stored as string"
            })


# POTENTIAL OUTLIERS

for column in ["Sales", "Quantity", "Discount", "Profit"]:

    if column in data.columns:

        first_quartile = data[column].quantile(0.25)
        third_quartile = data[column].quantile(0.75)

        iqr = third_quartile - first_quartile

        lower_limit = first_quartile - 1.5 * iqr
        upper_limit = third_quartile + 1.5 * iqr

        unusual_count = (
            (data[column] < lower_limit) |
            (data[column] > upper_limit)
        ).sum()

        audit_results.append({
            "Issue": "Potential Outliers",
            "Column": column,
            "Count": unusual_count,
            "Details": "Requires investigation"
        })


audit_report = pd.DataFrame(audit_results)

audit_report.to_csv(
    report_path / "Day18_Data_Quality_Audit_Report.csv",
    index=False
)

# ------------------------------------------------------------
# 11. SAVE DATA PROFILE
# ------------------------------------------------------------

data_profile = pd.DataFrame({
    "Column": data.columns,
    "Data_Type": data.dtypes.astype(str).values,
    "Missing_Values": data.isnull().sum().values,
    "Unique_Values": data.nunique().values
})

data_profile.to_csv(
    report_path / "Day18_Data_Profile.csv",
    index=False
)

# ------------------------------------------------------------
# 12. FINAL SUMMARY
# ------------------------------------------------------------

print("\n" + "=" * 65)
print("             AUDIT COMPLETED")
print("=" * 65)

print("Total Records:", data.shape[0])
print("Total Columns:", data.shape[1])
print("Missing Values:", data.isnull().sum().sum())
print("Duplicate Records:", duplicate_count)

print("\nReports Saved Successfully!")

print("Location:", report_path)
