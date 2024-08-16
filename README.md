# Health Monitoring System: Physical and Mental Health Assessment
## Overview
This project is a comprehensive health monitoring system that utilizes advanced machine learning models to assess both physical and mental health. The system allows users to input health-related data. The system is designed with a user-friendly interface and is accessible from any device with an internet connection.

## Features
Dual Health Assessment: The system evaluates both physical and mental health metrics, offering a holistic view of the user’s overall health.
Machine Learning Models: Multiple models, including Support Vector Machine (SVM), Decision Tree, Logistic Regression, K-Nearest Neighbors (KNN), Naive Bayes, and Random Forest, are used to ensure high accuracy in predictions.
User-Friendly Interface: Easy-to-navigate UI that allows users to input data, receive results, and access actionable insights.

## Project Structure
The project is organized into the following key components:

/data: Contains the datasets used for training and testing the machine learning models.
/Jupyter files: Includes the scripts for training the machine learning models and the saved model files.
/models: Having ht pickled models files
/ui: Contains the code for the user interface, including frontend only.
/docs: Documentation related to the project, including the requirement file.

## Installation
To set up and run the project locally, follow these steps:

1. Clone the Repository:
git clone https://github.com/yourusername/health-monitoring-system.git
cd health-monitoring-system

2. Install Dependencies:
Ensure you have Python 3.7+ installed. Install the required Python packages using pip:
pip install -r requirements.txt

3. Download the Datasets:
[Medical health dataset](https://www.kaggle.com/datasets/abhayayare/health-metrics-dataset)
[Mental health dataset](https://www.kaggle.com/datasets/bhavikjikadara/mental-health-dataset)

4. Train the Models:
Train the machine learning models by running the Jupyter files.

5. Run the UI:
Launch the user interface by running the following command "streamlit run App.py"

## Usage
Once the system is running, users can:

* Input Data: Enter health-related information through the user interface.
* Receive Assessment: The system will analyze the data and provide real-time feedback on physical and mental health.

## Models Used
Decision Tree: Provides a visual representation of decisions and their possible consequences and this model used for the mental health classification.
Logistic Regression: this model is particularly for mental health assessment.

## Contributing
Contributions to this project are welcome. If you would like to contribute, please follow these steps:

* Fork the repository.
* Create a new branch for your feature or bugfix.
* Submit a pull request with a description of your changes.


Acknowledgments
We would like to thank the contributors and the open-source community for their support and the resources provided for this project.
