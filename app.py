import streamlit as st
from app_pages.multipage import MultiPage
from app_pages.page_introduction import page_introduction_body
from app_pages.page_summary import page_summary_body
from app_pages.page_images_study import page_images_study_body
from app_pages.page_leaf_health_prediction import page_leaf_health_prediction_body


# create an instance of the app
app = MultiPage(app_name="Cherry Leaf Health")

# add app pages
app.add_page("Introduction", page_introduction_body)
app.add_page("Project Summary", page_summary_body)
app.add_page("Images Study", page_images_study_body)
app.add_page("Leaf Health Predictor", page_leaf_health_prediction_body)

app.run()