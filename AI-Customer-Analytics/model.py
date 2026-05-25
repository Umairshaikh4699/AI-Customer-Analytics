import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# Load dataset
df = pd.read_csv("data/customer_churn.csv")


# Show columns
print(df.columns)


# Features
X = df[['Age', 'MonthlyCharges', 'Contract', 'Tenure']]


# Target
y = df['Churn']


# Convert Yes/No to 1/0
y = y.map({'Yes':1, 'No':0})


# Convert text columns
X = pd.get_dummies(X)


# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create model
model = RandomForestClassifier()


# Train
model.fit(X_train, y_train)


# Predict
prediction = model.predict(X_test)


# Accuracy
accuracy = accuracy_score(y_test, prediction)

print("Accuracy:", accuracy)