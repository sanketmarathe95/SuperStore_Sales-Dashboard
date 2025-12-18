
# SuperStore Sales Analysis using Python

import pandas as pd

# Load dataset
df = pd.read_csv('superstore.csv')

# 1. Total Sales and Profit
total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
print(f'Total Sales: {total_sales:.2f}')
print(f'Total Profit: {total_profit:.2f}')

# 2. Category-wise Analysis
category_analysis = df.groupby('Category')[['Sales', 'Profit']].sum().reset_index()
print('\nCategory-wise Analysis:')
print(category_analysis)

# 3. Top 10 Products by Sales
top_products = (
    df.groupby('Product Name')['Sales']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
print('\nTop 10 Products by Sales:')
print(top_products)

# 4. Region-wise Performance
region_analysis = df.groupby('Region')[['Sales', 'Profit']].sum().reset_index()
print('\nRegion-wise Performance:')
print(region_analysis)

# 5. Segment-wise Performance
segment_analysis = df.groupby('Segment')[['Sales', 'Profit']].sum().reset_index()
print('\nSegment-wise Performance:')
print(segment_analysis)
