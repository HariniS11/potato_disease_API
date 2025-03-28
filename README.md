# Potato Disease Prediction using CNN

## 📌 Project Overview
This project focuses on building a **Potato Disease Prediction System** using a **Convolutional Neural Network (CNN)**. The model is trained to classify images of potato leaves into categories based on their health status. After achieving an accuracy of **90%**, the model was deployed using **FastAPI** for inference. API requests were tested using **Postman**.

---

## 🛠️ Tech Stack
- **Python**
- **TensorFlow/Keras**: For building and training the CNN model
- **FastAPI**: For creating the API server
- **Postman**: For testing API endpoints
- **NumPy, Pandas, Matplotlib**: For data preprocessing and visualization

---

## 📊 Dataset
- The dataset contains images of potato leaves classified into three categories:
  - Healthy
  - Early Blight
  - Late Blight
- Preprocessed using techniques like resizing, normalization, and augmentation.

---

## 🚀 Project Structure
```
Potato-Disease-Prediction/
├── dataset/
├── model/
│   ├── potato_disease_model.keras
├── api/
│   ├── server.py
├── requirements.txt
├── README.md
```

---

## 🧑‍💻 Model Training
- A CNN model was built using **Keras** with multiple convolutional layers, max pooling, and dense layers.
- Achieved **90% accuracy** after hyperparameter tuning.

**Steps:**
1. Data Loading and Preprocessing
2. Model Creation using CNN
3. Model Training and Evaluation
4. Saving the Model (`potato_disease_model.keras`)

---

## 🌐 API Development with FastAPI
- Created a FastAPI server (`server.py`) to load the trained model and serve predictions.
- API supports image input for classification.

**Endpoints:**
- `POST /predict` → Predict disease from uploaded potato leaf image

---

## 🔎 API Testing using Postman
1. Start the FastAPI server:
    ```bash
    uvicorn server:app --reload
    ```
2. Open Postman and send a POST request to `http://localhost:8000/predict` with an image file.
3. View the prediction result in the Postman response.

---

## 📦 Installation and Usage
1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/potato-disease-prediction.git
    cd potato-disease-prediction
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the FastAPI server:
    ```bash
    uvicorn api.server:app --reload
    ```
4. Test using Postman by sending a POST request to `http://localhost:8000/predict`

---

## ⚡ Future Improvements
- Add more classes for classification.
- Improve model accuracy using hyperparameter tuning.
- Deploy the model to a cloud platform for broader accessibility.

---

## 💡 Conclusion
This project provided hands-on experience in building a machine learning pipeline from **model training** to **deployment**. Using FastAPI for serving predictions and Postman for API testing has enriched your practical knowledge. Keep exploring and learning!

---

## 🤝 Acknowledgments
- Dataset from [Public Dataset Source]
- TensorFlow and Keras Documentation
- FastAPI and Postman Guides

---

## 📬 Contact
For any questions or suggestions, feel free to reach out via GitHub issues or email.

