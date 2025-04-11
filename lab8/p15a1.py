

import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv(r"C:\RV UNIVESITY DISC C\SEM 2\Python (PPDA)\6Mcd.csv")

# Calculate the correlation matrix
correlation_matrix = df.corr(numeric_only=True)

# Plot the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Matrix Heatmap")
plt.show()
