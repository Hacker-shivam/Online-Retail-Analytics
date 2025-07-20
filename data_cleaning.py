import pandas as pd
df = pd.read_excel(r"F:\internship\online+retail\Online Retail.xlsx")  # ✅ raw string
print(df.head())  # Show top rows
print(df.info())  # Check for nulls and data types
# Drop rows with missing CustomerID
df = df.dropna(subset=['CustomerID'])

# Remove negative or zero values
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]

# Create a TotalPrice column
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

# Convert InvoiceDate to datetime and create Month column
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['Month'] = df['InvoiceDate'].dt.to_period('M')
# Monthly Revenue
monthly_revenue = df.groupby('Month')['TotalPrice'].sum().reset_index()

# Top 10 Products
top_products = df.groupby('Description')['TotalPrice'].sum().sort_values(ascending=False).head(10)

# Revenue by Country
country_revenue = df.groupby('Country')['TotalPrice'].sum().sort_values(ascending=False)
df.to_csv("cleaned_online_retail.csv", index=False)
