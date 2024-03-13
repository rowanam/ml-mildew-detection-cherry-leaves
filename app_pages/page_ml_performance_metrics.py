import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf_model import load_test_evaluation


def page_ml_performance_metrics_body():
    st.write("## ML Performance Metrics")

    version = "v1"

    st.write("### Distributions of Target Labels")
    st.write(
        "The original dataset contained balanced target labels, so no over- or undersampling was required. The images were split into train, validation and test sets in a 7:1:2 ratio."
    )
    labels_distribution = plt.imread(f"outputs/{version}/labels_distribution.png")
    st.image(
        labels_distribution,
        caption="Label Distributions in Train, Validation and Test Sets",
    )

    st.write("---")

    st.write("### Model Training History")
    st.write(
        "The model achieved high accuracy and low losses in both the train and validation sets quickly, so training was stopped after a low number of epochs to avoid overfitting."
    )
    col1, col2 = st.beta_columns(2)
    with col1:
        model_accuracy = plt.imread(f"outputs/{version}/model_training_accuracy.png")
        st.image(model_accuracy, caption="Model Training Accuracy")
    with col2:
        model_losses = plt.imread(f"outputs/{version}/model_training_losses.png")
        st.image(model_losses, caption="Model Training Losses")

    st.write("---")

    st.write("### Test Set Performance")

    st.write(
        "The test set (20% of the original data) was unseen by the model during training and thus used to simulate real-time data and test the generalizability of the model."
    )
    st.write(
        "The model was able to predict on this set with over 99% accuracy. This meets the business requirements, which stipulated 97% accuracy."
    )
    st.dataframe(
        pd.DataFrame(load_test_evaluation(version), index=["Loss", "Accuracy"])
    )
