import streamlit as st
import pickle
import numpy as np
from tensorflow.keras.applications import InceptionV3
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_v3 import preprocess_input


# Load saved model and class names
with open("models/svm_model.pkl", "rb") as f:   
    model = pickle.load(f)

with open("models/class_names.pkl", "rb") as f:
    class_names = pickle.load(f)

with open("models/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Load InceptionV3 for feature extraction
feature_extractor = InceptionV3(
    weights="imagenet",
    include_top=False,
    pooling="avg"
)

st.title("Waste Classification")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = image.load_img(uploaded_file, target_size=(299, 299))
    st.image(img, caption="Uploaded Image", use_column_width=True)

    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    
    features = feature_extractor.predict(img_array)
    features = features.flatten().reshape(1, -1)

    # Apply same scaling as training
    features = scaler.transform(features)

    prediction = model.predict(features)[0]
    predicted_class = class_names[prediction]

    st.success(f"Predicted class: {predicted_class}")

    # Confidence (shown ONLY once)
    if hasattr(model, "predict_proba"):
        probs = model.predict_proba(features)
        confidence = np.max(probs) * 100
        st.info(f"Confidence: {confidence:.2f}%")
    else:
        st.info("Confidence not available for this model (SVM)")
