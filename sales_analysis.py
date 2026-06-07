import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample Sales Data
data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        'Revenue': [15000, 18000, 22000, 21000, 25000, 30000],
        'Customers': [200, 240, 300, 280, 320, 400]}
df = pd.DataFrame(data)

# Sales Trend
plt.figure(figsize=(8,5))
sns.lineplot(x=df['Month'], y=df['Revenue'], marker='o', label='Revenue')
sns.lineplot(x=df['Month'], y=df['Customers'], marker='s', label='Customers')
plt.title('Monthly Revenue & Customer Trend')
plt.xlabel('Month')
plt.ylabel('Value')
plt.legend()
plt.show()
