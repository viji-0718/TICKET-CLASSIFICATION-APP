import streamlit as st
import pandas as pd
import os
import requests

st.title("🎯 Ticket Classification Result")

# File upload
uploaded_file = st.file_uploader("Upload your ticket.csv file", type="csv")

if uploaded_file is not None:
    # Save file locally
    save_path = os.path.join("uploads", uploaded_file.name)
    os.makedirs("uploads", exist_ok=True)  # create folder if not exists
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"✅ File saved at: {save_path}")

    # Read file into DataFrame
    df = pd.read_csv(save_path)
    st.write("📊 Preview of uploaded data:")
    st.write(df.head())

# User input
user_input = st.text_input("Enter your issue:")
if user_input:
    response = requests.post("http://127.0.0.1:8000/predict", params={"text": user_input})
    if response.status_code == 200:
        result = response.json()
        st.success(f"Predicted Category: {result['category']}")
    else:
        st.error("Error connecting to backend API")