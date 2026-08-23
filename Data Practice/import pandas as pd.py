import pandas as pd

# 1. Create a raw dictionary of mock real estate data
raw_data = {
    "Price_USD": [250000, 410000, 315000, None, 520000, 600000],
    "Bedrooms": [3, 4, 3, 2, 5, 9],
    "Square_Feet": [1800, 2500, 2100, 1200, 3100, 4200],
    "Bathrooms": [2, 3, 2, 1, 4, 5]
}


# 2. Convert the dictionary into a structured Pandas DataFrame
df = pd.DataFrame(raw_data)
print("--- Original Dataset ---")
print(df)

# 3. Clean the data: Fill the missing 'None' price with the average price
mean_price = df['Price_USD'].mean()
df['Price_USD'] = df['Price_USD'].fillna(mean_price)

print("\n--- Cleaned Dataset (Missing Price Filled) ---")
print(df)

# 4. Generate automated mathematical statistics
print("\n--- Statistical Summary ---")
print(df.describe())

