import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/customer_churn.csv")

sns.countplot(x='Churn', data=df)

plt.show()