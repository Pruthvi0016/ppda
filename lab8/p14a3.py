import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("5ds_salaries.csv")

# Create a pair plot
sns.pairplot(df)
plt.show()
