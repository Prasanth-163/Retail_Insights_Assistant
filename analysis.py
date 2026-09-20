import pandas as pd

# Load cleaned dataset
file_path = "data/amazon_sales_cleaned.csv"
df = pd.read_csv(file_path)

# Convert date
df["Date"] = pd.to_datetime(df["Date"])


# 1. Get total sales
def get_total_sales():
    return df["Amount"].sum()


# 2. Get total quantity sold
def get_total_quantity():
    return df["Qty"].sum()


# 3. Get sales by category
def get_sales_by_category():
    return (
        df.groupby("Category")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )


# 4. Get sales by state
def get_sales_by_state():
    return (
        df.groupby("ship-state")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )


# 5. Get top products
def get_top_products(n=5):
    return (
        df.groupby("SKU")["Amount"]
        .sum()
        .sort_values(ascending=False)
        .head(n)
    )


# Test the functions
if __name__ == "__main__":

    print("\n========== RETAIL INSIGHTS ==========")

    print("\nTotal Sales:")
    print(f"₹{get_total_sales():,.2f}")

    print("\nTotal Quantity:")
    print(get_total_quantity())

    print("\nTop Categories:")
    print(get_sales_by_category().head(5))

    print("\nTop States:")
    print(get_sales_by_state().head(5))

    print("\nTop 5 Products:")
    print(get_top_products())