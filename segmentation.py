import pandas as pd

import matplotlib.pyplot as plt

from sklearn.cluster import KMeans


print("Program Started...")


# Load dataset
df = pd.read_csv("data/customer_churn.csv")

print("Dataset Loaded Successfully")


# Show first rows
print(df.head())


# Select features
X = df[['Age', 'MonthlyCharges', 'Tenure']]

print("Features Selected")


# Create model
kmeans = KMeans(n_clusters=3, random_state=42)

print("Model Created")


# Train model
kmeans.fit(X)

print("Model Training Completed")


# Add clusters
df['Cluster'] = kmeans.labels_

print("Clusters Added")


# Print output
print(df[['Age', 'MonthlyCharges', 'Tenure', 'Cluster']].head(10))


# Graph
plt.scatter(
    df['MonthlyCharges'],
    df['Tenure'],
    c=df['Cluster']
)

plt.xlabel("Monthly Charges")
plt.ylabel("Tenure")

plt.title("Customer Segmentation")


# Save graph image
plt.savefig("segmentation.png")

print("Graph Saved Successfully")


# Show graph
plt.show()

print("Program Finished")