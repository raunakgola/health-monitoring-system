Health Diagnosis Web App 🩺
===========================

Overview
--------

This is a web application built with Streamlit that provides users with a simple and interactive way to check their health status. The app offers two main functionalities:

1.  **Medical Health Diagnosis** 🫀
2.  **Mental Health Diagnosis** 🧠

Users can input their health parameters and receive a diagnosis on their health status with recommendations.

File Structure
--------------

-   **App.py**: The main application file containing the Streamlit interface.
-   **Images/**: Folder containing images used in the application interface.
-   **Models/**: Folder containing trained machine learning models for predictions.
-   **Medical Health.ipynb**: Jupyter notebook for medical health model training and analysis.
-   **Mental Health.ipynb**: Jupyter notebook for mental health model training and analysis.
-   **README.md**: Documentation file providing an overview of the project.
-   **Requirements.txt**: List of required Python packages for the project.

Usage
-----

### Running the Application

1.  Clone the repository.
2.  Install dependencies by running:

    ```
    pip install -r Requirements.txt
    ```

4.  Run the application with:

    ```
    streamlit run App.py
    ```

### Using the Application

1.  Choose either **Medical Health** or **Mental Health** diagnosis from the sidebar.
2.  Fill in the required details based on your selected diagnosis option.
3.  Click the **Predict** button to get the diagnosis and recommendations.

Model Details
-------------

-   **Medical Health Prediction**:
    -   Model: Logistic Regression (loaded as `LR_model.pkl`)
    -   Inputs include gender, age, blood pressure, cholesterol level, BMI, smoking, and diabetes status.
-   **Mental Health Prediction**:
    -   Model: Decision Tree (loaded as `DT_model.pkl`)
    -   Inputs include gender, country, occupation, stress levels, coping habits, and self-care history.

Requirements
------------

The required packages for this project are listed in `Requirements.txt`. You can install them with:


```
pip install -r Requirements.txt
```

Key packages include:

-   `streamlit`
-   `pickle`
-   `pandas`
-   `sklearn`
-   `numpy`

Screenshots
-----------

!["interface of app"](https://github.com/user-attachments/assets/c3d19660-cf8f-464e-8d8b-626e043a2bd1){width=300px height=200px}
![image](https://github.com/user-attachments/assets/b800c3e5-df6c-4375-9cf1-04b9b5ae5076)



License
-------

Specify the license for your project here.
