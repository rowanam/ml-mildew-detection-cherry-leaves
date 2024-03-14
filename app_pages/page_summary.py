import streamlit as st


def page_summary_body():
    st.write("## Project Summary")

    st.write("The project client, Farmy & Foods, is facing a challenge where their **cherry tree plantations have been presenting powdery mildew**, a fungal disease that affects many plant species.")
    st.write("The current verification of whether a given cherry tree contains powdery mildew is a time-consuming manual approach, which is not scalable to thousands of trees across multiple farms. However, trees with powdery mildew need to be identified in order to apply a compound to kill the fungus.")

    st.info("To save time in this process, the client requests a Machine Learning system that can detect instantly from a leaf image whether a tree is healthy or has powdery mildew.")

    st.write("### Business Case")

    st.success(
        "The business requirements are as follows:  \n"
        "* **1** - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.  \n"
        "* **2** - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew."
    )

    st.write("A successful project will help the client minimize the amount of compromised product they supply to the market")
    
    st.write("Additionally, a similar manual process is in place for detecting pests in other crops, and if this initiative is successful, there will be an opportunity to implement this project for other crops.")

    st.write("### Dataset")

    st.write("The dataset used in this project contains over 4,000 images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew.")

    st.write("The full dataset can be found here: [cherry leaves dataset](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves).")

    st.write("---")
    st.write("*For more project information, see the [project README](https://github.com/rowanam/ml-mildew-detection-cherry-leaves) on GitHub.*")
