import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread

import itertools
import random


def page_images_study_body():
    st.write("## Images Study")

    st.write(
        "Analyses were carried out on the cherry leaf images to understand the differences between healthy and powdery mildew-containing leaves."
    )
    st.write(
        "View a random sample of images from each class in the image montage section. Explore the various image analyses in the other sections."
    )

    st.info(
        "This page relates to business requirement 1 - *The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.*"
    )

    version = "v1"

    st.write("---")

    # image montage checkbox
    if st.checkbox("Sample image montage"):
        st.write("* To refresh the montage, click on the 'Create Montage' button")
        data_dir = "inputs/datasets/cherry-leaves"
        labels = os.listdir(data_dir + "/validation")
        label_to_display = st.selectbox(label="Select label", options=labels, index=0)
        if st.button("Create Montage"):
            image_montage(
                dir_path=data_dir + "/validation",
                label_to_display=label_to_display,
                nrows=4,
                ncols=3,
                figsize=(10, 13),
            )
        st.write("---")

    # average and variability checkbox
    if st.checkbox("Average and variability of class images"):
        avg_var_healthy = plt.imread(f"outputs/{version}/avg_var_healthy.png")
        avg_var_powdery_mildew = plt.imread(
            f"outputs/{version}/avg_var_powdery_mildew.png"
        )

        st.write(
            "The mean and standard deviation of images within each class was calculated and plotted to display the average and variability of the images."
        )
        st.write(
            "The leaves have overall similar shapes and colors, so the average and variability look relatively similar. However, it can be noted in the powdery mildew leaves that the average image contains paler 'spots' and that there is more variability within the leaf outline."
        )

        st.write("### Healthy")
        st.image(avg_var_healthy)
        st.write("### Powdery mildew")
        st.image(avg_var_powdery_mildew)

        st.write("---")

    # difference between averages checkbox
    if st.checkbox("Difference between average images"):
        avg_diff = plt.imread(f"outputs/{version}/avg_diff.png")

        st.write(
            "Subtracting the average of one image class from the other did not reveal significant insights."
        )
        st.image(avg_diff)


def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15, 10)):
    sns.set_style("white")
    labels = os.listdir(dir_path)

    # subset the class you are interested to display
    if label_to_display in labels:

        # checks if your montage space is greater than subset size
        # how many images in that folder
        images_list = os.listdir(dir_path + "/" + label_to_display)
        if nrows * ncols < len(images_list):
            img_idx = random.sample(images_list, nrows * ncols)
        else:
            print(
                f"Decrease nrows or ncols to create your montage. \n"
                f"There are {len(images_list)} in your subset. "
                f"You requested a montage with {nrows * ncols} spaces"
            )
            return

        # create list of axes indices based on nrows and ncols
        list_rows = range(0, nrows)
        list_cols = range(0, ncols)
        plot_idx = list(itertools.product(list_rows, list_cols))

        # create a Figure and display images
        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
        for x in range(0, nrows * ncols):
            img = imread(dir_path + "/" + label_to_display + "/" + img_idx[x])
            axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)

            axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
            axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
        plt.tight_layout()

        st.pyplot(fig=fig)
        # plt.show()

    else:
        print("The label you selected doesn't exist.")
        print(f"The existing options are: {labels}")
