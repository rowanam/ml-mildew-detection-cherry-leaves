import streamlit as st


def page_project_hypotheses_body():
    st.write("## Project Hypotheses")

    st.write("### Visual Differences")
    st.success(
        "*Hypothesis*: Cherry leaves with and without powdery mildew will have significant visual differences that will allow classification by a neural network."
    )
    st.write(
        "Visual inspection of samples of each class of leaves reveals that powdery mildew-containing leaves tend to have white spots on their surfaces. Though the average and variability plots were relativly similar, there was a visible occurence of white spots in the average powdery mildew image and more texture in the variability plot."
    )
    st.write(
        "This hypothesis proved correct, as there was enough visual differentiation between the image classes to train a model with a very high accuracy in distinguishing healthy and powdery mildew-containing leaves."
    )

    st.write("---")

    st.write("### Greater Variabilty in Powdery Mildew Leaves")
    st.success(
        "*Hypothesis*: Images of leaves with powdery mildew will have greater color variability."
    )
    st.write(
        "Since healthy leaves tend to have a fairly uniform green color, while leaves with powdery mildew additionally present with white coloration, it is hypothesized that analysis of the variability of pixels in the images will reveal that the latter has higher variability."
    )
    st.write(
        "This hypothesis is likely correct, as the variability plot of powdery mildewed leaves reveals more differentiation than the plot of healthy leaf variability, which is more uniformly black within the leaf shape."
    )
