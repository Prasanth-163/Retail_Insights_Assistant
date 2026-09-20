import pandas as pd

# Load dataset
file_path = "data/Amazon Sale Report(in).csv"

df = pd.read_csv(file_path, low_memory=False)

print("Original shape:", df.shape)

# 1. Remove unnecessary column
df = df.drop(columns=["Unnamed: 22"])

# 2. Convert Date to datetime
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# 3. Convert numeric columns
df["Qty"] = pd.to_numeric(df["Qty"], errors="coerce")
df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")

# 4. Remove rows where essential sales information is missing
df = df.dropna(subset=["Date", "Qty", "Amount"])

# 5. Save cleaned dataset
output_path = "data/amazon_sales_cleaned.csv"
df.to_csv(output_path, index=False)

print("Cleaned shape:", df.shape)

print("\nRemaining missing values:")
print(df.isnull().sum())

print("\nCleaned dataset saved to:")
print(output_path)