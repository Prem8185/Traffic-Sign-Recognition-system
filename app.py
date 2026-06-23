import streamlit as st
import google.generativeai as genai
from PIL import Image
import numpy as np
import cv2

from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

from class_names import class_names

# ==========================
# PAGE SETTINGS
# ==========================

st.set_page_config(
    page_title="Traffic Sign Detector",
    page_icon="🚦",
    layout="centered"
)

# ==========================
# GEMINI API
# ==========================

# ==========================
# GEMINI API
# ==========================

API_KEYS = [
    st.secrets["GEMINI_API_KEY_1"],
    st.secrets["GEMINI_API_KEY_2"],
    st.secrets["GEMINI_API_KEY_3"]
]

def gemini_prediction(prompt, image):

    models = [
        "gemini-3.1-flash-lite",
        "gemini-2.5-flash",
    ]

    last_error = None

    for api_key in API_KEYS:

        genai.configure(
            api_key=api_key
        )

        for model_name in models:

            try:

                model = genai.GenerativeModel(
                    model_name
                )

                response = model.generate_content(
                    [prompt, image]
                )

                return response.text

            except Exception as e:

                last_error = str(e)

    raise Exception(last_error)

# ==========================
# FALLBACK MODEL
# ==========================

fallback_model = load_model(
    "models/traffic_sign.keras"
)

# ==========================
# FALLBACK FUNCTION
# ==========================

def mobilenet_prediction(image):

    image_np = np.array(image.convert("RGB"))

    image_np = image_np.astype(np.uint8)

    image_resized = cv2.resize(
        image_np,
        (96, 96)
    )

    image_resized = preprocess_input(
        image_resized.astype("float32")
    )

    image_resized = np.expand_dims(
        image_resized,
        axis=0
    )

    prediction = fallback_model.predict(
        image_resized,
        verbose=0
    )

    predicted_class = np.argmax(
        prediction
    )

    confidence = np.max(
        prediction
    ) * 100

    if predicted_class < len(class_names):
        sign_name = class_names[predicted_class]
    else:
        sign_name = f"Class {predicted_class}"

    return f"""
🚦 Traffic Sign:

{sign_name}

🎯 Confidence:

{confidence:.2f}%
"""

# ==========================
# CUSTOM CSS
# ==========================

st.markdown("""
<style>

.main-title {
    text-align: center;
    font-size: 38px;
    font-weight: bold;
    color: #4CAF50;
}

.sub-title {
    text-align: center;
    font-size: 18px;
    color: gray;
    margin-bottom: 20px;
}

.result-card {
    background-color: #f8f9fa;
    color: black;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #dcdcdc;
    font-size: 18px;
    line-height: 2;
    margin-top: 15px;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# HEADER
# ==========================

st.markdown(
    '<div class="main-title">🚦 Traffic Sign Recognition Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Traffic Sign Detection using MobileNetV2 + Gemini Model</div>',
    unsafe_allow_html=True
)


# ==========================
# IMAGE SOURCE
# ==========================

source = st.radio(
    "Select Image Source",
    ["📁 Upload Image", "📸 Use Camera"],
    horizontal=True
)

image = None

if source == "📁 Upload Image":

    uploaded_file = st.file_uploader(
        "Upload Traffic Sign",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        image = image.resize((224, 224))

elif source == "📸 Use Camera":

    camera_file = st.camera_input(
        "Capture Traffic Sign"
    )

    if camera_file is not None:
        image = Image.open(camera_file)
        image = image.resize((224, 224))

# ==========================
# PREDICTION
# ==========================

if image is not None:

    st.image(
        image,
        caption="Selected Image",
        use_container_width=True
    )

    with st.spinner("🔍 Analyzing Traffic Sign..."):

        prompt = """
        Identify the traffic sign.

        Return exactly in this format:

        🚦 Traffic Sign:
        <sign name>

        📖 Meaning:
        <meaning>

        🚗 Driver Advice:
        <advice>

        IMPORTANT:
        Put each heading on a separate line.
        Put the answer below the heading.
        Do not write everything in one sentence.
        Keep the answer short and professional.
        """

        try:

            result_text = gemini_prediction(
                prompt,
                image
            )

        except Exception:

            st.warning(
                "⚠️ Advanced model unavailable. Using MobileNetV2 fallback model."
            )

            result_text = mobilenet_prediction(
                image
            )

    st.success(
        "✅ Analysis Complete"
    )

    formatted_text = result_text.replace(
        "\n",
        "<br>"
    )

    st.markdown(
        f"""
        <div class="result-card">
        {formatted_text}
        </div>
        """,
        unsafe_allow_html=True
    )

# ==========================
# FOOTER
# ==========================

st.write("")

st.caption(
    "Developed by Prem Kumar | Traffic Sign Recognition Project"
)

