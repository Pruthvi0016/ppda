import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('6Mcd.csv')

# Assuming the two correlated columns are 'Q1' and 'Q2' (replace with actual column names if different)
plt.figure(figsize=(8, 6))
sns.scatterplot(x=df['Q1'], y=df['Q2'], color='blue', alpha=0.7)
plt.title('Scatter Plot of Q1 vs Q2')
plt.xlabel('Q1')
plt.ylabel('Q2')
plt.grid()
plt.show()
