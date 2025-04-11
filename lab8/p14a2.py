import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("5ds_salaries.csv")

sns.histplot(df['salary_in_usd'], kde=True, bins=30, color='blue')
plt.title('Distribution of Salary in USD')
plt.xlabel('Salary in USD')
plt.ylabel('Frequency')
plt.show()
