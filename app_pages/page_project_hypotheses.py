import streamlit as st


def page_project_hypotheses_body():
    st.write("## Project Hypotheses")

    st.write("### Model Can be Created from Visual Differences")
    st.success(
        "*Hypothesis*: Cherry leaves with and without powdery mildew will have significant visual differences that will allow classification by a neural network."
    )
    st.write(
        "Visual inspection of samples of each class of leaves reveals that powdery mildew-containing leaves tend to have white spots on their surfaces. Though the average and variability plots were relativly similar, there was a visible occurence of white spots in the average powdery mildew image and more texture in the variability plot."
    )
    st.write(
        "This hypothesis proved correct, as there was enough visual differentiation between the image classes to train a model with very high accuracy (over the 97% accuracy requirement) in distinguishing healthy and powdery mildew-containing leaves."
    )

    st.write("---")

    st.write("### Greater Variabilty in Powdery Mildew Leaf Images")
    st.success(
        "*Hypothesis*: Images of leaves with powdery mildew will have greater color variability."
    )
    st.write(
        "Since healthy leaves tend to have a fairly uniform green color, while leaves with powdery mildew additionally present with white coloration, it is hypothesized that analysis of the variability of pixels in the images will reveal that the latter has higher variability."
    )
    st.write(
        "The analyses pertaining to this hypothesis were inconclusive. While the plot of variability *between* different powdery mildew leaf images displayed greater variability on the leaf surface as compared to the corresponding plot for healthy images, the variability of pixel values *within* the powdery leaf images were on average lower than those of healthy leaves."
    )

    st.write("---")

    st.write(
        "### Higher Leaf Proportion and Thus Greater Variabilty in Central Portion of Powdery Mildew Leaf Images"
    )
    st.success(
        "*Hypothesis*: The central portions of the images are more likely to contain only leaf surface without the background, and in this portion powdery mildew leaf images will display greater variability than the centers of the healthy images."
    )
    st.write(
        "Following variability analyses related to the previous hypothesis, it was found that variability was not greater in the powdery mildew images when using the entire images. A potential explanation for this result is that there might be differences in the background between the two classes of images. This possibility is raised for example by the average image studies (see Images Study page), which reveal a slightly lighter average background color in healthy leaf images."
    )
    st.write(
        "To investigate whether the unexpected result of the variability study was due to differences in the background and not the leaves themselves, a further hypothesis was tested. From visually inspecting the images, the leaves tend to be centered and take up most of the images. Therefore, narrowing the study to only the central portions, for example approximately the central thirds, of the images is more likely to capture only the leaf surfaces without the background. It is hypothesized that these portions of the images will contain greater variability in powdery mildew leaf images."
    )
    st.write(
        "This hypothesis is likely correct. When the analysis was restricted to the central thirds of the leaf images, the averages values of green in the pixels of the healthy images increased significantly, providing at least one indication that these portions contain leaf surface and less background. In these portions of the images, the variability was higher across all color channels within the powdery mildew leaf images, as predicted. However, the difference was relatively small and thus not strong enough to conclusively validate the hypothesis."
    )
