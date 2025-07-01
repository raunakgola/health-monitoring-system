import streamlit as st  # Import Streamlit library for creating the web app
import pickle  # Import pickle for loading saved models
import pandas as pd  # Import pandas for data handling (though unused here)
import sklearn  # Import sklearn (used indirectly through saved models)


# Set up the Streamlit page configuration
st.set_page_config("Diagnosis", layout='wide')

# Display the title and subtitle
st.title("Welcome to Health Diagnosis web app 🩺")
st.subheader("A application where you can check Medical Health🫀 or Mental Health🧠")

# Create two columns for layout organization
col1, col2 = st.columns(2)

# Sidebar for user inputs
with st.sidebar:
    # Select the diagnosis type: Medical or Mental Health
    heatlth_category = st.radio('Choose any one diagnosis option', [0, 1],format_func=lambda x: 'Medical Health🫀' if x == 1 else 'Mental Health🧠')

    # If Medical Health is selected
    if heatlth_category == 1:
        # Get user inputs for medical health parameters
        gender = st.selectbox("Select your Gender",('Male', 'Female'))
        age = st.number_input("Enter your age ", min_value=18, max_value=80)
        sys_bp = st.number_input("Enter systolic BP ", min_value=105, max_value=150)
        dia_bp = st.number_input("Enter diastolic BP ", max_value=95, min_value=65)
        cholesterol = st.number_input("Enter your Cholesterol", max_value=240, min_value=140)
        BMI = st.number_input("Enter your BMI in Kg/m²", max_value=40, min_value=25)
        smoke = st.selectbox("Do you smoke?", [True, False], format_func=lambda x: 'YES' if x == 1 else 'NO')
        diabetes = st.selectbox("Do you have diabetes?", [True, False], format_func=lambda x: 'YES' if x == 1 else 'NO')

        # When the Predict button is clicked
        if st.button("Predict"):
            # Prepare the input data for the model
            df = pd.DataFrame({
                'Gender': [gender],
                'Age': [age],
                'Systolic BP': [sys_bp],
                'Diastolic BP': [dia_bp],
                'Cholesterol': [cholesterol],
                'BMI': [BMI],
                'Smoker': [smoke],
                'Diabetes': [diabetes]
            })

            # Load the pre-trained medical health model
            model1 = pickle.load(open("Models/DT_Medical_data.pkl", "rb"))

            # Get the prediction result
            pred = model1.predict(df)[0]

            # Display the result based on the prediction
            if pred == 1:
                with col1:
                    st.header("Good")
                    st.write("You're in great shape! Keep up the good work by eating healthy, exercising regularly, and getting enough sleep.")
                    st.write("Your overall health is excellent. Consider scheduling a routine check-up to maintain your well-being.")
                with col2:
                    st.image("Images/good.png")
            elif pred == 2:
                with col1:
                    st.header("Fair")
                    st.write("Your health is fair. It's important to focus on improving your diet and increasing physical activity.")
                    st.write("You might be experiencing some minor health issues. Consult a doctor to get a proper diagnosis and treatment.")
                with col2:
                    st.image("Images/fair.png")
            else:
                with col1:
                    st.header("Bad")
                    st.write("Your health is currently at risk. Seek immediate medical attention and follow the doctor's advice.")
                    st.write("You need to prioritize your health. Make lifestyle changes and follow a treatment plan as recommended.")
                with col2:
                    st.image("Images/bad.png")

    # If Mental Health is selected
    if heatlth_category == 0:

        # Get user inputs for mental health parameters
        gender1 = st.selectbox("Select your Gender", ('Female', 'Male'))
        country = st.selectbox("Which country do you belong?",('United States', 'Poland', 'Australia', 'Canada', 'United Kingdom', 'South Africa', 'Sweden', 
                                                                'New Zealand', 'Netherlands', 'India', 'Belgium', 'Ireland', 'France', 'Portugal', 'Brazil', 
                                                                'Costa Rica', 'Russia', 'Germany', 'Switzerland', 'Finland', 'Israel', 'Italy', 'Bosnia and Herzegovina', 
                                                                'Singapore', 'Nigeria', 'Croatia', 'Thailand', 'Denmark', 'Mexico', 'Greece', 'Moldova', 'Colombia', 'Georgia', 
                                                                'Czech Republic', 'Philippines'))
        occupation = st.selectbox("What's your Occupation?", ('Corporate', 'Student', 'Business', 'Housewife', 'Others'))
        self_emp = st.selectbox("Are you self-employed?", ('No', 'Yes'))
        familiy_history = st.selectbox("Do you have a family history of mental illness?",('No', 'Yes'))
        Indoor = st.selectbox("How much time do you spend indoors?",('1-14 days', 'Go out Every day', 'More than 2 months', '15-30 days', '31-60 days'))
        grow_stress = st.selectbox("Does your stress grow?", ('Yes', 'No', 'Maybe'))
        habit = st.selectbox("Have you tried changing your habits?", ('No', 'Yes', 'Maybe'))
        mental_his = st.selectbox("Do you have a history of mental illness?", ('Yes', 'No', 'Maybe'))
        mood_swings = st.selectbox("How much do you experience mood swings?", ('Medium', 'Low', 'High'))
        struggle = st.selectbox("Do you struggle to cope?", ('No', 'Yes'))
        interest = st.selectbox("Do you have work interest?", ('No', 'Maybe', 'Yes'))
        weak = st.selectbox("Do you have social weaknesses?", ('Yes', 'No', 'Maybe'))
        interview = st.selectbox("Have you gone through any mental health interviews?", ('No', 'Maybe', 'Yes'))
        care = st.selectbox("Do you care for your mental health?", ('Not sure', 'No', 'Yes'))

        # When the Predict button is clicked
        if st.button("Predict"):
            # Prepare the input data for the model
            df1 = pd.DataFrame({
                'Gender': [gender1],
                'Country': [country],
                'Occupation': [occupation],
                'self_employed': [self_emp],
                'family_history': [familiy_history],
                'Days_Indoors': [Indoor],
                'Growing_Stress': [grow_stress],
                'Changes_Habits': [habit],
                'Mental_Health_History': [mental_his],
                'Mood_Swings': [mood_swings],
                'Coping_Struggles': [struggle],
                'Work_Interest': [interest],
                'Social_Weakness': [weak],
                'mental_health_interview': [interview],
                'care_options': [care]
            })

            # Load the pre-trained mental health model
            model2 = pickle.load(open("Models/DT_mental_health.pkl", "rb"))

            # Get the prediction result
            pred = model2.predict(df1)[0]

            # Display the result based on the prediction
            if pred == 0:
                with col1:
                    st.header("Good")
                    st.write("You're doing great! Keep practicing self-care, and explore new ways to nurture your well-being.")
                    st.write("Your mental health is strong. Consider engaging in activities that bring you joy and fulfillment.")
                with col2:
                    st.image("Images/good1.png")
            elif pred == 1:
                with col1:
                    st.header("Fair")
                    st.write("You might be experiencing some challenges. Try incorporating relaxation techniques like meditation or yoga.")
                    st.write("It's okay to not be okay. Reach out to friends, family, or a mental health professional for support.")
                with col2:
                    st.image("Images/fair1.png")
            else:
                with col1:
                    st.header("Bad")
                    st.write("Your mental health is a priority. Please reach out to a crisis hotline or mental health professional immediately.")
                    st.write("You're not alone. There are resources available to help you cope. Seek support and don't hesitate to ask for help.")
                with col2:
                    st.image("Images/bad1.png")
