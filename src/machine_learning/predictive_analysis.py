import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from tensorflow.keras.models import load_model
from PIL import Image
from src.data_management import load_pkl_file


def resize_input_image(img, version):
    """
    Reshape image to average image size
    """
    # image_shape = load_pkl_file(file_path=f"outputs/{version}/image_shape.pkl")
    image_shape = (256, 256, 3)
    img_resized = img.resize((image_shape[1], image_shape[0]), Image.LANCZOS)
    my_image = np.expand_dims(img_resized, axis=0)

    return my_image


def load_model_and_predict(my_image, version):
    """
    Load and perform ML prediction over live images
    """

    model = load_model(f"outputs/{version}/leaf_health_clf_model.h5")

    class_names = load_pkl_file(file_path=f"outputs/{version}/class_names.pkl")

    # predict on the data, returns an array of probabilities
    prediction_probs = model.predict(my_image)

    # get the index of the highest probability, use to select label from class_names
    prediction_class = class_names[np.argmax(prediction_probs, axis=1)[0]]

    if prediction_class == "healthy":
        st.write("The predictive analysis indicates that the leaf is **healthy**.")
    else:
        st.write("The predictive analysis indicates that the leaf has **powdery mildew**.")

    return prediction_probs, prediction_class
