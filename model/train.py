import sys
sys.path.append("..")

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import joblib
from utils.preprocessing import clean_text

# Load dataset
df = pd.read_csv("../data/phishing_dataset.csv")  # columns: "Email Text", "Email Type"

# Drop rows with missing values
df.dropna(subset=["Email Text", "Email Type"], inplace=True)

# Clean the email text
df["cleaned_text"] = df["Email Text"].apply(clean_text)
X = df["cleaned_text"]

# Convert the target labels into binary format
y = df["Email Type"].apply(lambda x: 1 if "phishing email" in x.lower() else 0)

# Vectorization
vectorizer = TfidfVectorizer(stop_words='english', max_features=500)
X_vec = vectorizer.fit_transform(X)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

# Model training
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Save model and vectorizer
joblib.dump(clf, "../model/rf_model.pkl")
joblib.dump(vectorizer, "../model/vectorizer.pkl")

print("Model and vectorizer saved successfully.")
