from flask import Flask, request, jsonify
import pickle
import nltk
from nltk.tokenize import word_tokenize
import re
import string

# Load the trained NLP model and vectorizer
model_path = "fake_news_model.pkl"
vectorizer_path = "tfidf_vectorizer.pkl"

with open(model_path, "rb") as f:
    model = pickle.load(f)

with open(vectorizer_path, "rb") as f:
    vectorizer = pickle.load(f)

# Initialize Flask app
app = Flask(__name__)

# Preprocessing function
def preprocess_text(text):
    text = text.lower()
    text = re.sub(f"[{string.punctuation}]", "", text)
    tokens = word_tokenize(text)
    return " ".join(tokens)

# Prediction endpoint
@app.route("/predict", methods=["POST"])
def predict_news():
    try:
        data = request.get_json()
        processed_text = preprocess_text(data["text"])
        transformed_text = vectorizer.transform([processed_text])
        prediction = model.predict(transformed_text)[0]
        result = "Fake News" if prediction == 1 else "Real News"
        return jsonify({"prediction": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
