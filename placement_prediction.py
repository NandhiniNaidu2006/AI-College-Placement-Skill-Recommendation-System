import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv("placement_data.csv")

X = data.drop("placement", axis=1)
y = data["placement"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

print("AI MODEL TRAINED SUCCESSFULLY!")
new_student = pd.DataFrame(
    [[8.0, 80, 75, 3, 1]],
    columns=["cgpa", "aptitude", "communication", "projects", "internships"]
)

prediction = model.predict(new_student)
probability = model.predict_proba(new_student)[0][1] * 100

if prediction[0] == 1:
    print("PLACEMENT PREDICTION: LIKELY TO BE PLACED")
else:
    print("PLACEMENT PREDICTION: NEEDS IMPROVEMENT")

print("PLACEMENT PROBABILITY:", round(probability, 2), "%")