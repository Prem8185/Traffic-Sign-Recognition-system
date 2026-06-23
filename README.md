# 🚦 Traffic Sign Recognition and Driver Assistance System

A Deep Learning-based Traffic Sign Recognition and Driver Assistance System developed using MobileNetV2, TensorFlow, Streamlit, and Google Gemini AI.

The system recognizes traffic signs from uploaded images or camera input, generates meaningful explanations of detected signs, and provides driver assistance recommendations to support safer and more informed driving decisions.

---

## 📌 Features

• Traffic Sign Recognition using MobileNetV2

• Upload Image and Camera Input Support

• Real-Time Traffic Sign Analysis

• AI-Based Traffic Sign Meaning Generation

• Driver Assistance Recommendations

• Streamlit Web Interface

• MobileNetV2 Fallback System

• Cloud Deployment

---

## 🌍 Live Demo

🔗 Streamlit Application

https://traffic-sign-recognition-system-vaph4odonftkerb48xxqjh.streamlit.app/

---

## 🛠️ Technologies Used

• Python

• TensorFlow

• Keras

• Streamlit

• OpenCV

• NumPy

• Google Gemini API

• GitHub

---

## 🧠 Deep Learning Model

• Model Architecture: MobileNetV2

• Framework: TensorFlow / Keras

• Transfer Learning Approach

• Image Classification Model

• Optimized for Traffic Sign Recognition

---

## 📂 Dataset

German Traffic Sign Recognition Benchmark (GTSRB)

The dataset contains multiple traffic sign categories used for training and evaluating the classification model.

---

## 🚀 System Workflow

```text
Traffic Sign Image
        ↓
Image Preprocessing
        ↓
MobileNetV2 Classification
        ↓
Traffic Sign Prediction
        ↓
Gemini AI Analysis
        ↓
Traffic Sign Meaning
        ↓
Driver Assistance Recommendation
```

---

## 📸 Supported Input Methods

### Upload Image

Upload JPG, JPEG, or PNG traffic sign images directly from your device.

### Camera Input

Capture traffic sign images using your device camera for instant recognition and analysis.

---

## ⚡ Intelligent Prediction System

The application uses a hybrid prediction pipeline:

1. MobileNetV2 identifies the traffic sign.

2. Gemini AI generates:
   - Traffic Sign Name
   - Sign Meaning
   - Driver Advice

3. If Gemini becomes unavailable, the application automatically switches to the MobileNetV2 fallback system which is trained on own to ensure uninterrupted predictions.

---

## 💡 Applications

• Driver Assistance Systems

• Smart Transportation Systems

• Autonomous Vehicles

• Traffic Monitoring Solutions

• Road Safety Applications

• Intelligent Transportation Systems (ITS)

---

## 📁 Project Structure

```text
Traffic-Sign-Recognition-System

├── app.py
├── class_names.py
├── requirements.txt
├── runtime.txt
├── .gitignore
└── models
    └── traffic_sign.keras
```

---

## ⚙️ Installation & Local Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Prem8185/Traffic-Sign-Recognition-System.git
```

### 2️⃣ Navigate to the Project Folder

```bash
cd Traffic-Sign-Recognition-System
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Gemini API Keys

Create a `.streamlit/secrets.toml` file and add:

```toml
GEMINI_API_KEY_1 = "your_api_key"
GEMINI_API_KEY_2 = "your_api_key"
GEMINI_API_KEY_3 = "your_api_key"
```

### 5️⃣ Run the Application

```bash
streamlit run app.py
```

### 6️⃣ Open in Browser

```text
http://localhost:8501
```

The application will launch locally and be ready for traffic sign detection and driver assistance analysis.

---

## 👨‍💻 Developer

**Prem Kumar**

B.Tech – Electronics and Communication Engineering (ECE)

---

🚗 Applications

- Driver Assistance Systems
- Autonomous Vehicles
- Smart Transportation Systems
- Road Safety Monitoring
- Traffic Sign Recognition

---

🔄 Project Workflow

## 🚀 How It Works

```text
Traffic Sign Image
        ↓
Image Preprocessing
        ↓
MobileNetV2 Classification
        ↓
Traffic Sign Prediction
        ↓
Gemini AI Analysis
        ↓
Traffic Sign Meaning
        ↓
Driver Assistance Recommendation
```

---

📈 Future Enhancements

- Real-Time Video Detection
- Object Detection Integration
- Multi-Language Support
- Dashboard Analytics
- Advanced Driver Assistance Features

---
