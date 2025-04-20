import streamlit as st
import requests

st.title("Tomato Disease Prediction 🌿🍅")

uploaded_file = st.file_uploader("Upload a Tomato Leaf Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    # Send file to FastAPI
    if st.button("Predict"):
        files = {"file": uploaded_file.getvalue()}
        response = requests.post("http://localhost:8001/predict", files={"file": uploaded_file})
        
        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted: {result['class']} with {result['confidence']*100:.2f}% confidence")
        else:
            st.error("Prediction failed. Check server or image file.")
