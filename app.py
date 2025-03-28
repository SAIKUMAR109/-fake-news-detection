import requests
import streamlit as st

# Streamlit UI for Fake News Detection
st.title("Fake News Detection System")

# User Inputs
news_text = st.text_area("Enter News Article Text")
submit = st.button("Check Authenticity")

# Backend API URL
API_URL = "http://127.0.0.1:8000/predict"

if submit:
    if news_text.strip():
        # Prepare request data
        request_data = {"text": news_text}
        
        # Send request to backend
        response = requests.post(API_URL, json=request_data)
        
        if response.status_code == 200:
            result = response.json()["prediction"]
            if result == "Fake News":
                st.error(f"⚠️ This news appears to be: {result}")
            else:
                st.success(f"✅ This news appears to be: {result}")
        else:
            st.error("Error processing the news article")
    else:
        st.warning("Please enter some text to analyze.")
