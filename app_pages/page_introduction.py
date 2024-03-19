import streamlit as st


def page_introduction_body():
    st.write("## Introduction")

    st.write(
        """This dashboard provides insight into the health of cherry trees 
        by assessing whether their leaves contain powdery mildew."""
    )
    st.write("---")
    st.write(
        "The project has 2 main goals: \n"
        """* Undertake a visual study of healthy and powdery mildew-containing 
        cherry leaves to understand the differences  \n"""
        """* Predict whether or not a cherry leaf has powdery mildew from 
        real-time passed images"""
    )
    st.write("---")
    st.write(
        """The pages in this dashboard contain further project information, the 
        visual study and predictor outlined above, and technical information 
        about the machine learning model created for this project."""
    )
