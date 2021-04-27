# Model-Deployment-to-GCP
Image classification model deployment to GCP. Using Streamlit for interface.


## How to get started?

* A [Google Cloud account](https://cloud.google.com/gcp) and a [Google Cloud Project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).
* [Google Cloud SDK installed](https://cloud.google.com/sdk/docs/install) (gcloud CLI utitly)
* Trained machine learning model(s), this app will use an image classification model trained on a number of different classes of food from [Food101 dataset](https://www.kaggle.com/dansbecker/food-101)

**Warning :** Google Cloud is a paid service, this may cost money, be sure to shut down any Google Cloud service you no longer need to use to avoid charges. 
If you don't have credits (you get $300USD when you first sign up), you will be charged. Delete and shutdown your work when finished to avoid charges.

## Current progress...

If you go through the steps below, you should end up with a [Streamlit](http://streamlit.io/)-powered web application for classifying images of food (deployed on Google Cloud if you want).

The app running locally - uploading an image, basic foundation of app is completed.:
![app demo](https://github.com/Shripad1020/Model-Deployment-to-GCP/blob/master/images/app_progress_1.png)

## Steps to follow

We're going to tackle this in 3 parts:
1. Getting the app running (running Streamlit on our local machines) - ***Completed***
2. Deploying a machine learning model to AI Platform (getting Google Cloud to host one of our models)
3. Deploying our app to App Engine (getting our app on the internet)

## To do
- [ ] Getting the app running
  - [x] Run app on local machine. i.e. predictions
  - [x] Train model
  - [ ] Complete logger method
  - [ ] Use try except for KeyError
- [ ] Deploying a machine learning model
- [ ] Deploying our app to App Engines