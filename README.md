# 🚦 Traffic Sign Recognition and Driver Assistance System

A Machine Learning-based Traffic Sign Recognition and Driver Assistance System developed using MobileNetV2, TensorFlow, Google Gemini AI and Streamlit.

The system recognizes traffic signs from uploaded images or camera input, generates meaningful explanations of detected signs, and provides driver assistance recommendations to support safer and more informed driving decisions.

---

## 📌 Features

* Traffic Sign Recognition using MobileNetV2
* Upload Image and Camera Input Support
* Real-Time Traffic Sign Analysis & Meaning Generation
* Driver Assistance Recommendations
* MobileNetV2 Fallback Prediction System
* Cloud Deployment Support

---

## 🌍 Live Demo

🔗 * [App Link](https://traffic-sign-recognition-system-vaph4odonftkerb48xxqjh.streamlit.app/) - click here to view the app *

---

## 🛠️ Technologies Used

* Python
* TensorFlow
* Keras
* MobileNetV2
* Streamlit
* OpenCV
* NumPy
* Google Gemini API
* GitHub

---

## 🧠 Deep Learning Model

* Model Architecture: MobileNetV2
* Framework: TensorFlow / Keras
* Dataset: German Traffic Sign Recognition Benchmark (GTSRB)
* Task: Traffic Sign Classification

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

## ⚡ Intelligent Prediction System & Fallback Mechanism

The application uses a hybrid prediction pipeline to ensure high availability:

1. **Primary Layer:** MobileNetV2 identifies the traffic sign, and the Google Gemini API generates the contextual meaning and real-time driver advice.
2. **Fallback Layer:** If the Gemini API becomes unavailable (due to rate limits, network issues, or missing keys), the system automatically switches to a local fallback pretrained mechanism. It leverages native pretrained structural mappings (`class_names.py`) to provide uninterrupted traffic sign identification.

---

## 📂 Project Structure

```text
Traffic-Sign-Recognition-System/
├── .streamlit/
│   └── secrets.toml
├── models/
│   └── traffic_sign.keras
├── app.py
├── class_names.py
├── requirements.txt
├── runtime.txt
└── .gitignore
```

---

## ⚙️ Installation & Local Setup

### 1. Clone Repository

```bash
git clone https://github.com
cd Traffic-Sign-Recognition-System
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Gemini API Keys

Create a file at `.streamlit/secrets.toml` and add your keys:

```toml
GEMINI_API_KEY_1="your_api_key"
GEMINI_API_KEY_2="your_api_key"
GEMINI_API_KEY_3="your_api_key"
```

### 4. Run Application

```bash
streamlit run app.py
```

---

## 💡 Applications

* Driver Assistance Systems
* Intelligent Transportation Systems
* Smart Traffic Monitoring
* Road Safety Solutions
* Autonomous Vehicle Research

---

## 👨‍💻 Developer

**Prem Kumar**  
B.Tech – Electronics and Communication Engineering (ECE)  

---

