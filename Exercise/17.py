import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Data Loading and Exploration
df = pd.read_csv('sales_data.csv')
print("Descriptive Statistics using NumPy:")
print(np.array(df.describe()))
print("\nDescriptive Statistics using Pandas:")
print(df.describe())
print("\nFirst few rows of the dataset:")
print(df.head())

# Data Cleaning and Manipulation
print("\nMissing values:")
print(df.isnull().sum())
df['Date'] = pd.to_datetime(df['Date'])
df['Total_Price'] = df['Quantity'] * df['Price_per_Unit']

# Data Visualization
product_sales = df.groupby('Product_Name')['Total_Price'].sum()
plt.figure(figsize=(10, 6))
product_sales.plot(kind='bar', color='red')
plt.title('Total Sales for Each Product')
plt.xlabel('Product')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 6))
sales_trend = df.groupby('Date')['Total_Price'].sum()
sales_trend.plot(kind='line', marker='o', color='orange')
plt.title('Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales ($)')
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df['Quantity'], df['Total_Price'], color='green')
plt.title('Relationship between Quantity and Total Price')
plt.xlabel('Quantity')
plt.ylabel('Total Price ($)')
plt.show()

# Advanced Analysis
correlation_coefficient = np.corrcoef(df['Quantity'], df['Total_Price'])[0, 1]
print("\nCorrelation Coefficient between Quantity and Total Price:", correlation_coefficient)

average_spending_per_customer = df.groupby('Customer_ID')['Total_Price'].mean()
print("\nAverage Total Spending per Customer:")
print(average_spending_per_customer)

top_5_products = product_sales.nlargest(5)
plt.figure(figsize=(10, 6))
top_5_products.plot(kind='bar', color='purple')
plt.title('Top 5 Products by Total Sales')
plt.xlabel('Product')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=45)
plt.show()
