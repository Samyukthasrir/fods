import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Example data (replace with your actual data)
data = {
    'product_category': ['Category A', 'Category B', 'Category C', 'Category A', 'Category B'],
    'sales_amount': [1000, 1500, 800, 1200, 2000],
    'date_column': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-01', '2023-01-02'],
    'other_variable': [50, 30, 40, 60, 70]
}

df = pd.DataFrame(data)

# Plotting all three types of plots
plt.figure(figsize=(18, 6))

# Line plot
plt.subplot(1, 3, 1)
sns.lineplot(x='date_column', y='sales_amount', hue='product_category', data=df)
plt.title('Sales Trends Across Product Categories')
plt.xlabel('Date')
plt.ylabel('Total Sales Amount')
plt.xticks(rotation=45)
plt.tight_layout()

# Scatter plot
plt.subplot(1, 3, 2)
sns.scatterplot(x='sales_amount', y='other_variable', hue='product_category', data=df)
plt.title('Sales Scatter Plot Across Product Categories')
plt.xlabel('Sales Amount')
plt.ylabel('Other Variable')
plt.tight_layout()

# Bar plot
plt.subplot(1, 3, 3)
sns.barplot(x='product_category', y='sales_amount', data=df, estimator=sum)
plt.title('Total Sales by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Total Sales Amount')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
