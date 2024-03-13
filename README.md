# Cherry Leaf Mildew Detection

The goal of this project is to provides insight into the health of cherry trees by assessing whether their leaves contain powdery mildew.

It has 2 main goals:

* Undertake a visual study of healthy and powdery mildew-containing cherry leaves to understand the differences
* Predict whether or not a cherry leaf has powdery mildew from real-time passed images

The outputs of this project can be viewed on a dashboard - the live link is HERE.

## Dataset Content

The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). A fictitious user story was then created where predictive analytics can be applied to a real project.

The dataset contains over 4,000 images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

## Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

* 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.


## Hypotheses and how to validate?

**Cherry leaves with and without powdery mildew will have significant visual differences that will allow classification by a neural network.**

* The presence of visual differences can be investigated through visual inspection of sample image montages and average and variability image studies.
* The hypothesis will be validated if the neural network model is able to make predictions of leaf health to a high degree of accuracy.

**Images of leaves with powdery mildew will have greater color variability.**

* Since healthy leaves tend to have a fairly uniform green color, while leaves with powdery mildew additionally present with white coloration, it is hypothesized that analysis of the variability of pixels in the images will reveal that the latter has higher variability.
* This can be validated through variability image studies.

## The rationale to map the business requirements to the Data Visualisations and ML tasks

Business requirement 1: **Data Visualization**

* Display image montages for healthy and powdery mildew cherry leaves
* Display images showing the average and standard deviation of each image class
* Display an image showing the difference between the two average images

Business requirement 2: **Classifiication**

* Give the client the ability to upload a leaf image and generate a prediction of whether it has powdery mildew or not

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

* Outline of images study
* Checkboxes for each study
    - Image montage
    - Average and variability images
    - Difference between average infected and healthy images

### Page 4: Powdery Mildew Detector

* Link to download a set of sample images for prediction testing
* Mildew detection
    - A file uploader widget
    - Outputs image display with a statement of predicted class and associated probability
    - A button to download the results as a table

### Page 5: Project Hypothesis and Validation

Visual Differences:

* Hypothesis: Cherry leaves with and without powdery mildew will have significant visual differences that will allow classification by a neural network.
* Justification, validations and conclusion

Greater Variabilty in Powdery Mildew Leaves:

* Hypothesis: Images of leaves with powdery mildew will have greater color variability.
* Justification, validations and conclusion

### Page 6: ML Performance Metrics

* Label distributions for train, validation and test sets
* Model training history comparing train and validation sets
    - Accuracy plot
    - Loss plot
* Model evaluation result
    - Test set loss and accuracy

## Unfixed Bugs

No bugs were found during testing.

## Deployment

### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
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
