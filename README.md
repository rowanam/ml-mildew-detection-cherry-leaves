# Cherry Leaf Mildew Detection

The goal of this project is to provides insight into the health of cherry trees by assessing whether their leaves contain powdery mildew.

It has 2 main goals:

* Undertake a visual study of healthy and powdery mildew-containing cherry leaves to understand the differences
* Predict whether or not a cherry leaf has powdery mildew from real-time passed images

The outputs of this project can be viewed on a dashboard - the live link is [here](https://cherry-leaf-health-2ff1edcf83ab.herokuapp.com/).

## Dataset Content

The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). A fictitious user story was then created where predictive analytics can be applied to a real project.

The dataset contains over 4,000 images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

## Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

* 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

## Hypotheses and how to validate?

**Hypothesis: Cherry leaves with and without powdery mildew will have significant visual differences that will allow classification by a neural network.**

* The presence of visual differences can be investigated through visual inspection of sample image montages and average and variability image studies.
* The hypothesis will be validated if the neural network model is able to make predictions of leaf health to a level of 97% accuracy.

**Hypothesis: Images of leaves with powdery mildew will have greater color variability.**

* Since healthy leaves tend to have a fairly uniform green color, while leaves with powdery mildew additionally present with white coloration, it is hypothesized that analysis of the variability of pixels in the images will reveal that the latter has higher variability, both between different images of the same class and within individual images.
* This can be validated through variability image studies between and within images, comparing the two classes.

**Hypothesis: The central portions of the images are more likely to contain only leaf surface without the background, and in this portion powdery mildew leaf images will display greater variability than the centers of the healthy images.**

* Following variability analyses related to the previous hypothesis, it was found that variability was not greater in the powdery mildew images when using the entire images. Since this could be due to differences in the background and not the leaves themselves (see the Project Limitations section below), a further hypothesis was tested. From visually inspecting the images, the leaves tend to be centered and take up most of the images. Therefore, narrowing the study to only the central portions, for example approximately the central thirds, of the images is more likely to capture only the leaf surfaces without the background. It is hypothesized that these portions of the images will contain greater variability in powdery mildew leaf images.
* This can be validated through:
    - observing the color distributions in these portions of the images and comparing them to the full images
    - comparing variability within the images between the two classes, with the analysis restricted to (approximately) the central thirds of the images

## The rationale to map the business requirements to the Data Visualizations and ML tasks

Business requirement 1: **Data Visualization**

* Display image montages for healthy and powdery mildew cherry leaves
* Display images showing the average and standard deviation of each image class
* Display an image showing the difference between the two average images
* Display plots showing variability within the images of each class

Business requirement 2: **Classifiication**

* Give the client the ability to upload a leaf image and generate a prediction of whether it has powdery mildew or not
* Provide a report of the images and predictions that can be downloaded

## ML Business Case

### Powdery mildew classification

* The client is interested in an ML model that can predict if a cherry leaf is healthy or contains powdery mildew
* Currently, the classification process has a duration of around 30 minutes per tree and requires an expert employee to make the prediction
* The client has request a dashboard where cherry leaf images can be uploaded and that will display the classification prediction and the associated probability
* This will benefit the client since it will help them to significantly speed up their powdery mildew identification process, as well as reducing the need for trained staff. Therefore they will be able limit the amount of compromised product they supply to the market while still optimizing product output levels and efficiency.
* The client has supplied a dataset with labeled images of both powdery mildew-infected and healthy cherry leaves
* The data suggests a binary classifier
* The success metric agreed upon as the criterium for project success is **97% accuracy** overall

## Dashboard Design (Streamlit)

### Page 1: Introduction

* Brief outline of project goals and dashboard content

### Page 2: Project Summary

* General project information
* Business case and requirements
* Project dataset information

### Page 3: Images Study

This page relates to business requirement 1 - *The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.*

* Outline of images study
* Checkboxes for each study
    - Image montage
        - Label dropdown
        - Montage creation button
    - Average and variability images
        - Average and variability plots for healthy leaves
        - Average and variability plots for powdery mildew leaves
    - Difference between average healthy and powdery mildew-containing images
        - Dfference between averages plot
    - Variability within images
        - Histograms of rgb channel variability for healthy and powdery mildew full images
        - Table of average rgb channel variabilities for healthy and powdery mildew full images
        - Histograms of rgb channel variability for healthy and powdery mildew centers of images
        - Table of average rgb channel variabilities for healthy and powdery mildew centers of images

### Page 4: Powdery Mildew Detector

This page relates to business requirement 2 - *The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.*

* Link to download a set of sample images for prediction testing
* Mildew detection
    - A file uploader widget
    - Outputs image display with a statement of predicted class and associated probability
    - A button to download the results as a table

### Page 5: Project Hypothesis and Validation

* Model Can be Created from Visual Differences

    - Hypothesis: Cherry leaves with and without powdery mildew will have significant visual differences that will allow classification by a neural network.
    - Justification, validations and conclusion

* Greater Variabilty in Powdery Mildew Leaf Images:

    - Hypothesis: Images of leaves with powdery mildew will have greater color variability.
    - Justification, validations and conclusion

* Higher Leaf Proportion and Thus Greater Variabilty in Central Portion of Powdery Mildew Leaf Images

    - Hypothesis: The central portions of the images are more likely to contain only leaf surface without the background, and in this portion powdery mildew leaf images will display greater variability than the centers of the healthy images.
    - Justification, validations and conclusion

### Page 6: ML Performance Metrics

* Label distributions for train, validation and test sets
* Model training history comparing train and validation sets
    - Accuracy plot
    - Loss plot
* Model evaluation result
    - Test set loss and accuracy

## Project Limitations

### Non-cherry-leaf images

The model was trained using only images of healthy and powdery mildew-containing cherry leaves. Therefore, passing any other type of image will lead the model to output a "prediction" of one of these classes, even though this would have no relevance for the image.

### Image dataset quality

It was noted during the images study that there may be some qualitative differences between the images of each class in the provided dataset. The differences observed include:

* Powdery mildew leaves seem to point upward more often, while healthy leaves point up or down
* Potential differences in background or image quality. This was seen in -
    - visual inspection of the images
    - plotting the difference between the average of the healthy and the average of the powdery mildew leaf images. In the individual plots, you can observe that the background of the healthy leaf images is on average lighter than in powedery mildew leaf images. Consequently, the difference plot of the two average images displays some light around the edges of the leaf shape.
    - analysis of variability in the images, where healthy leaf images displayed higher variability than powdery mildew leaves, contrary to expectations. Furthermore, there were significant differences in the distributions between the two classes, but these distributions became less different when the background was mostly removed from the analysis.

While this is not conclusive evidence of a quality problem in the dataset, it is an indication that there could be an issue. The model should continue to be evaluated for performance on real-time data, and if prediction accuracy becomes lower, this would be an avenue to explore.

## Unfixed Bugs

No bugs were found during testing.

## Deployment

### Heroku

* The app live link is here: [Cherry Leaf Health Dashboard](https://cherry-leaf-health-2ff1edcf83ab.herokuapp.com/)
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file. 


## Main Data Analysis and Machine Learning Libraries

* [Numpy](https://numpy.org/) - used to store and handle image data, and to calculate the average and variability values for the visualization study
* [Pandas](https://pandas.pydata.org/) - used to store data to output as plots (target labels distribution, model learning curves) and download data as table (dashboard live prediction results)
* [Matplotlib](https://matplotlib.org/) - used to create image montage figures and data analysis plots
* [Seaborn](https://seaborn.pydata.org/) - used to create styled data analysis plots (such as labels distributions, model learning curves)
* [TensorFlow](https://www.tensorflow.org/) - used to create and train the ML classification model

## Other Software Tools Used

* [Python](https://www.python.org/)
* [Jupyter Notebooks](https://jupyter.org/)
* [Streamlit](https://docs.streamlit.io/) - prototype dashboard creation

## Credits

### Content

The fictional business case story was created by Code Institute.

The dataset used in the project comes from [Kaggle](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves).

### Media

The sample images on the dashboard were pulled from the Kaggle database.

All plots and charts were generated by the developer.
