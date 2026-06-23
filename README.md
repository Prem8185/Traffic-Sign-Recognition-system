🚦 Traffic Sign Recognition and Driver Assistance System

📌 Overview

The Traffic Sign Recognition and Driver Assistance System is an AI-powered web application that detects and identifies traffic signs from images captured through a camera or uploaded by a user.

The system combines a deep learning model based on MobileNetV2 with advanced AI-powered traffic sign interpretation to provide:

- Traffic Sign Identification
- Sign Meaning Explanation
- Driver Assistance Recommendations

The application is deployed using Streamlit and designed to support intelligent transportation and driver awareness systems.

---

🎯 Features

- Upload traffic sign images
- Capture traffic signs using a camera
- Automatic traffic sign recognition
- Real-time sign classification
- Driver assistance recommendations
- MobileNetV2-based fallback prediction system
- User-friendly web interface
- Cloud deployment using Streamlit

---

🧠 Technologies Used

Programming Language

- Python

Deep Learning

- TensorFlow
- Keras
- MobileNetV2

Computer Vision

- OpenCV
- Pillow

AI Integration

- Google Gemini API

Web Application

- Streamlit

Deployment

- Streamlit Community Cloud

---

🏗 Project Architecture

Traffic Sign Image

↓

Image Preprocessing

↓

MobileNetV2 Classification Model

↓

Traffic Sign Prediction

↓

AI-Based Interpretation

↓

Meaning Generation

↓

Driver Assistance Recommendation

---

📂 Project Structure

Traffic-Sign-Recognition-System/
│
├── app.py
├── class_names.py
├── requirements.txt
├── runtime.txt
├── models/
│   └── traffic_sign.keras
│
└── README.md

🚀 How to Run Locally

Clone Repository

git clone https://github.com/Prem8185/Traffic-Sign-Recognition-system.git

Open Project

cd Traffic-Sign-Recognition-system

Install Dependencies

pip install -r requirements.txt

Run Application

streamlit run app.py

---

📸 Application Capabilities

- Detect traffic signs from uploaded images
- Detect traffic signs from camera captures
- Display traffic sign name
- Explain traffic sign meaning
- Provide driver guidance

---

🎓 Learning Outcomes

Through this project, I gained practical experience in:

- Deep Learning
- Computer Vision
- CNN-Based Image Classification
- MobileNetV2 Architecture
- AI Integration
- Streamlit Deployment
- Model Deployment on Cloud Platforms
- Driver Assistance Applications

---

👨‍💻 Developer

Prem Kumar

Final Year B.Tech (ECE)

---

⭐ Future Enhancements

- Real-time video traffic sign detection
- Lane detection integration
- Object detection for vehicles and pedestrians
- Voice-based driver alerts
- Advanced Driver Assistance System (ADAS) features
