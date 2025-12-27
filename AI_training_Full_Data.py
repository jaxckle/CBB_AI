import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
data = pd.read_csv("cbb.csv")

# Clean target
data["CATEGORY"] = data["CATEGORY"].map(
    lambda x: 1 if x == "Champions" else 0
)
data = data.dropna(subset=["CATEGORY"])

# Define features and target (USE SAME DATAFRAME)
X = data.drop(columns=[
    "CATEGORY", "YEAR", "TEAM", "CONF", "G", "POSTSEASON"
])
y = data["CATEGORY"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=40, stratify=y
)

# Model (weaker trees to reduce overfitting)
rf = RandomForestClassifier(
    n_estimators=200,
    max_depth=4,
    min_samples_leaf=10,
    min_samples_split=20,
    random_state=40,
    class_weight="balanced"
)

rf.fit(X_train, y_train)

# Evaluation
y_pred = rf.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(classification_report(y_test, y_pred, digits=4))

# Cross-validation (recall matters most)
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=40)
scores = cross_val_score(rf, X, y, cv=cv, scoring="recall")

print("Champion recall per fold:", scores)
print("Mean recall:", scores.mean())

# Feature importance
importance = pd.Series(
    rf.feature_importances_,
    index=X.columns
).sort_values(ascending=False)

print(importance.head(10))
