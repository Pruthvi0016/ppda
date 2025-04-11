

import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('6Mcd.csv')

# Assuming the variable of interest is 'Q1' (replace 'Q1' with the actual column name if different)
plt.figure(figsize=(10, 6))
plt.plot(df['Q1'], marker='o', linestyle='-', color='b', label='Q1 Trend')
plt.title('Trend of Q1 (Matplotlib)')
plt.xlabel('Index')
plt.ylabel('Q1')
plt.legend()
plt.grid()
plt.show()

# Using seaborn for the same variable
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x=df.index, y='Q1', marker='o', label='Q1 Trend')
plt.title('Trend of Q1 (Seaborn)')
plt.xlabel('Index')
plt.ylabel('Q1')
plt.legend()
plt.grid()
plt.show()
