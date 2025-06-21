# main.py
import sys
import joblib
from utils.preprocessing import clean_text
from database.db import init_db, save_result

# Load model and vectorizer
model = joblib.load("model/rf_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")


# Predict if email phishing or safe with the trained model
def predict_email(text):
    cleaned = clean_text(text)
    vec = vectorizer.transform([cleaned])
    prediction = model.predict(vec)[0]
    return "Phishing" if prediction == 1 else "Safe"


if __name__ == "__main__":
    init_db()
    print("Welcome to PhishingShield!")
    print("Paste the full email text below. Press Ctrl+D (on macOS/Linux) or Ctrl+Z (on Windows) when done:\n")
    email_text = sys.stdin.read()
    result = predict_email(email_text)
    print(f"\n Prediction: {result}")
    save_result(email_text, result)  # save a result to data base
