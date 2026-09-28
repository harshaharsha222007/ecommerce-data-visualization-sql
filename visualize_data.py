import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create directory to save images
os.makedirs('visualizations', exist_ok=True)

# Set style
sns.set_theme(style="whitegrid")
plt.rcParams.update({'font.size': 12, 'axes.labelsize': 14, 'axes.titlesize': 16})

# 1. Load Data
df = pd.read_csv('orders_dataset.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['YearMonth'] = df['Date'].dt.to_period('M')

# --- Visual 1: Product Performance (Bar Chart) ---
plt.figure(figsize=(10, 6))
product_revenue = df.groupby('Product')['TotalPrice'].sum().sort_values(ascending=False).reset_index()
sns.barplot(data=product_revenue, x='TotalPrice', y='Product', hue='Product', palette='viridis', legend=False)
plt.title('Gross Revenue Distribution by Product Line')
plt.xlabel('Total Revenue ($)')
plt.ylabel('Product Category')
plt.tight_layout()
plt.savefig('visualizations/product_revenue.png', dpi=300)
plt.close()

# --- Visual 2: Order Status Operational Integrity (Pie Chart) ---
plt.figure(figsize=(8, 8))
status_counts = df['OrderStatus'].value_counts()
colors = ['#4CAF50', '#2196F3', '#FFC107', '#FF5722', '#9C27B0']
plt.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=140, colors=colors[:len(status_counts)], 
        wedgeprops={'edgecolor': 'white', 'linewidth': 2})
plt.title('Order Fulfillment Status Distribution')
plt.tight_layout()
plt.savefig('visualizations/order_status_distribution.png', dpi=300)
plt.close()

# --- Visual 3: Marketing Attribution Runway (Donut Chart) ---
plt.figure(figsize=(8, 8))
referral_counts = df['ReferralSource'].value_counts()
plt.pie(referral_counts, labels=referral_counts.index, autopct='%1.1f%%', startangle=90, 
        colors=sns.color_palette('pastel'), pctdistance=0.85)
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title('Acquisition Funnel Traffic via Referral Channels')
plt.tight_layout()
plt.savefig('visualizations/traffic_acquisition.png', dpi=300)
plt.close()

print("Successfully generated files inside 'visualizations/' folder.")
