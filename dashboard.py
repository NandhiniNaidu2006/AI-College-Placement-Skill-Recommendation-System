import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)


# Load dataset
data = pd.read_csv("placement_data.csv")


# Input features
X = data[
    [
        "cgpa",
        "aptitude",
        "communication",
        "projects",
        "internships"
    ]
]


# Target
y = data["placement"]


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# Create model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# Train model
model.fit(X_train, y_train)


# Prediction
y_prediction = model.predict(X_test)


# Calculate actual metrics
accuracy = accuracy_score(
    y_test,
    y_prediction
)

precision = precision_score(
    y_test,
    y_prediction,
    zero_division=0
)

recall = recall_score(
    y_test,
    y_prediction,
    zero_division=0
)

f1 = f1_score(
    y_test,
    y_prediction,
    zero_division=0
)


# Convert to percentage
labels = [
    "Accuracy",
    "Precision",
    "Recall",
    "F1-Score"
]

values = [
    accuracy * 100,
    precision * 100,
    recall * 100,
    f1 * 100
]


# Create chart
plt.figure(figsize=(8, 5))

plt.bar(
    labels,
    values
)

plt.title(
    "Actual ML Model Performance"
)

plt.xlabel(
    "Evaluation Metrics"
)

plt.ylabel(
    "Score (%)"
)

plt.ylim(
    0,
    100
)


# Display values on bars
for i, value in enumerate(values):

    plt.text(
        i,
        value + 2,
        f"{value:.1f}%",
        ha="center"
    )


plt.tight_layout()


# Save chart
plt.savefig(
    "static/model_performance.png"
)


plt.show()


# Print actual values
print("MODEL PERFORMANCE")

print(
    "Accuracy:",
    round(accuracy * 100, 2),
    "%"
)

print(
    "Precision:",
    round(precision * 100, 2),
    "%"
)

print(
    "Recall:",
    round(recall * 100, 2),
    "%"
)

print(
    "F1-Score:",
    round(f1 * 100, 2),
    "%"
)

print(
    "Actual model performance chart created successfully!"
)