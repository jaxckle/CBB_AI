import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

# Load dataset
data = pd.read_csv("full_even_yearly_data.csv")
data_cleaned = data.copy()
data_cleaned["CATEGORY"] = data_cleaned["CATEGORY"].map(
        lambda x: 1 if x == "Champions" else 0
    )


    # Define features and target variable
X = data.drop(columns=["CATEGORY", "YEAR"])
y = data["CATEGORY"]

X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    # Stratified split to maintain class distribution because winners are rare
    # Initialize and train the model
rf = RandomForestClassifier(
        # number of trees in the forest
        n_estimators=300,
        # is the maximum depth of the tree
        max_depth=6,
        # minimum number of samples required to be at a leaf node
        min_samples_leaf=5,
        # random state for reproducibility
        random_state=42,
        # class weights to handle imbalanced classes
        class_weight="balanced"
    )

rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy:.4f}")

print(classification_report(y_test, y_pred))


    # 47% accuracy with basic features and smaller dataset