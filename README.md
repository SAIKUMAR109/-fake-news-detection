# -fake-news-detection
 Fake News Detection using Machine Learning
📋 Overview
This project focuses on building a machine learning model to detect fake news from real news articles. Using Natural Language Processing (NLP) techniques and classification algorithms, the model predicts whether a news article is "Real" or "Fake" based on its content.

📊 Dataset
The dataset contains news articles with the following columns:

id – Unique identifier for each article
title – Headline of the news
author – Author of the article
text – Main content of the news article
label – Target variable (0 = Real, 1 = Fake)
📥 Dataset Source: realtime - Fake News Dataset

🛠️ Technologies Used

language: Python 🐍
Libraries:
Pandas & NumPy – Data manipulation
NLTK – Text preprocessing
Scikit-learn – ML algorithms
Matplotlib & Seaborn – Data visualization
Flask or Streamlit – Model deployment

🔍 Exploratory Data Analysis (EDA)
Handling missing values
Word frequency analysis
Generating word clouds for fake and real news
Visualizing the most common words in both categories

🧹 Data Preprocessing
Removing stopwords, punctuation, and special characters
Converting text to lowercase
Tokenization and Lemmatization
Converting text to numerical features using TF-IDF Vectorization

🤖 Machine Learning Models
The following models were tested:

Logistic Regression
Naive Bayes Classifier (Best performance)
Support Vector Machine (SVM)
Random Forest Classifier

🚀 Best Model: Naive Bayes with an accuracy of ~92%.

