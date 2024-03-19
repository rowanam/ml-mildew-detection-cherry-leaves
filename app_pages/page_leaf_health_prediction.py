import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (
    load_model_and_predict,
    resize_input_image,
)


def page_leaf_health_prediction_body():
    st.write("## Leaf Health Predictor")

    st.write(
        """Upload cherry leaf images to generate predictions of whether or 
        not they contain powdery mildew."""
    )
    st.info(
        """*Note:* the model used here was trained only on healthy or powdery 
        mildew-containing cherry leaves. If any other type of image is uploaded, 
        it will still generate a prediction of one of these classes, even though 
        this wouldn't be relevant to that image."""
    )
    st.write(
        """One or multiple images can be added using the file uploader below. To 
        get a sample of images to test the live prediction, download the images 
        from the dataset, 
        [here](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves)."""
    )
    st.write(
        """After running the predictions, you can download the outputs by clicking 
        the 'Download Report' button."""
    )

    st.success(
        """This page relates to business requirement 2 - *The client is interested 
        in predicting if a cherry leaf is healthy or contains powdery mildew.*"""
    )

    st.write("---")

    images_buffer = st.file_uploader(
        "Upload cherry leaf images. You can upload more than one.",
        type=["png", "jpg"],
        accept_multiple_files=True,
    )

    if images_buffer is not None:
        df_report = pd.DataFrame([])
        for image in images_buffer:

            img_pil = Image.open(image)
            st.info(f"Leaf image: **{image.name}**")
            img_array = np.array(img_pil)
            st.image(
                img_pil,
                caption=f"Image Size: {img_array.shape[1]}px width x {img_array.shape[0]}px height",
            )

            version = "v1"
            resized_img = resize_input_image(img=img_pil)
            pred_proba, pred_class = load_model_and_predict(
                resized_img, version=version
            )

            df_report = df_report.append(
                {"Name": image.name, "Result": pred_class}, ignore_index=True
            )

        if not df_report.empty:
            st.success("Analysis Report")
            st.table(df_report)
            st.markdown(download_dataframe_as_csv(df_report), unsafe_allow_html=True)
