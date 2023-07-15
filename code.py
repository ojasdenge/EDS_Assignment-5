import pandas as pd import itertools 
# Read the CSV file into a DataFrame 
df = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Files/grainsales.csv') 

# Which was the best month for sales? How much was earned that month? 
monthly_sales = df.groupby('Months')['Sales'].sum() 
best_month = monthly_sales.idxmax() 
best_month_sales = monthly_sales[best_month] 
print("Best Month for Sales:", best_month) 
print("Sales Amount:", best_month_sales) 

# Which product sold the most? 
product_sales = df.groupby('GrainName')['Sales'].sum() 
best_product = product_sales.idxmax() 
best_product_sales = product_sales[best_product] 
print("Best Selling Product:", best_product) 
print("Sales Amount:", best_product_sales)

import pandas as pd 
import itertools 

# Read the CSV file into a DataFrame 
df = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Files/grainsales.csv') 

# Example of Pandas operations:
# 1. Group by 'GrainName' and calculate the sum of sales 
grouped_sales = df.groupby('GrainName')['Sales'].sum() 
print(grouped_sales) 

# 2. Filter the DataFrame based on a condition 
filtered_data = df[df['State'] == 'Maharashtra'] 
print(filtered_data) 

# 3. Sort the DataFrame by 'Sales' in descending order 
sorted_data = df.sort_values('Sales', ascending=False) 
print(sorted_data) 

# 4. Calculate the total sales for each month 
monthly_sales = df.groupby('Months')['Sales'].sum() 
print(monthly_sales) 

# 5. Calculate the average sales for each grain 
average_sales = df.groupby('GrainName')['Sales'].mean() 
print(average_sales) 

# 6. Count the number of occurrences of each grain 
grain_counts = df['GrainName'].value_counts() 
print(grain_counts) 

# 7. Calculate the total sales for each state and city 
state_city_sales = df.groupby(['State', 'City'])['Sales'].sum() 
print(state_city_sales) 

# 8. Select rows where the sales are greater than 2 million 
high_sales = df[df['Sales'] > 2000000] 
print(high_sales) 

# 9. Add a new column 'Total' that represents the cumulative sales for each grain 
df['Total'] = df.groupby('GrainName')['Sales'].cumsum() 
print(df) 

# 10. Calculate the maximum sales for each month and year
max_sales = df.groupby(['Months', 'Year'])['Sales'].max() 
print(max_sales) 

# 11. Remove duplicate rows from the DataFrame 
df = df.drop_duplicates() 
print(df) 

# 12. Rename the columns 
df = df.rename(columns={'GrainName': 'Grain', 'State': 'StateName', 'City': 'CityName'}) 
print(df) 
# 13. Reset the index of the DataFrame 
df = df.reset_index(drop=True) 
print(df) 

# 14. Export the DataFrame to a CSV file 
df.to_csv('output.csv', index=False)
