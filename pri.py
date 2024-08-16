import streamlit as st
import pickle
import pandas
import sklearn
import numpy as np
fn = lambda x: {0: 'Australia', 1: 'Belgium', 2: 'Bosnia and Herzegovina', 3: 'Brazil', 4: 'Canada', 5: 'Colombia', 6: 'Costa Rica', 7: 'Croatia', 8: 'Czech Republic', 9: 'Denmark', 10: 'Finland', 11: 'France', 12: 'Georgia', 13: 'Germany', 14: 'Greece', 15: 'India', 16: 'Ireland', 17: 'Israel', 18: 'Italy', 19: 'Mexico', 20: 'Moldova', 21: 'Netherlands', 22: 'New Zealand', 23: 'Nigeria', 24: 'Philippines', 25: 'Poland', 26: 'Portugal', 27: 'Russia', 28: 'Singapore', 29: 'South Africa', 30: 'Sweden', 31: 'Switzerland', 32: 'Thailand', 33: 'United Kingdom', 34: 'United States'}[x]
fn1 = lambda x1: {0: 'Business', 1: 'Corporate', 2: 'Housewife', 3: 'Others', 4: 'Student'}[x1]
fn2 = lambda x2: {0: '1-14 days', 1: '15-30 days', 2: '31-60 days', 3: 'Go out Every day', 4: 'More than 2 months'}[x2]
fn3 = lambda x3: {0: 'Maybe', 1: 'No', 2: 'Yes'}[x3]
fn4 = lambda x4: {0: 'No', 1: 'Not sure', 2: 'Yes'}[x4]


st.set_page_config("Diagnosis",layout='wide')
st.title("Welcome to Health Diagnosis web app 🩺")
st.subheader("A application where you can check Medical Health🫀 or Mental Health🧠")
col1, col2 = st.columns(2)
with st.sidebar:
    smoker = st.radio('Choose any one diagnosis option', [0, 1], format_func=lambda x: 'Medical Health🫀' if x == 1 else 'Mental Health🧠')
    if smoker == 1:
        gender = st.selectbox("Select your Gender",[0,1],format_func=lambda x: 'Male' if x == 1 else 'Female')
        age = st.number_input("Enter your age ",min_value=18,max_value=80)
        sys_bp = st.number_input("Enter systolic BP ",min_value=105,max_value=150)
        dia_bp = st.number_input("Enter diastolic BP ",max_value=95,min_value=65)
        cholesterol = st.number_input("Enter your Cholesterol", max_value=240, min_value=140)
        BMI = st.number_input("Enter your  BMI in Kg/m²",max_value=40,min_value=25)
        smoke = st.selectbox("Do you smoke?", [0, 1], format_func=lambda x: 'YES' if x == 1 else 'NO')
        diabetes = st.selectbox("Do you have diabetes?",[0,1],format_func=lambda x: 'YES' if x == 1 else 'NO')
        if st.button("Predict"):
            values1 = np.array([gender,age,sys_bp,dia_bp,cholesterol,BMI,smoke,diabetes]).reshape(1, -1)
            model1 = pickle.load(open("LR_model.pkl", "rb"))
            pred = model1.predict(values1)[0]
            if pred == 1:
                with col1:
                    st.header("Good")
                    st.write("You're in great shape! Keep up the good work by eating healthy, exercising regularly, and getting enough sleep.")
                    st.write("Your overall health is excellent. Consider scheduling a routine check-up to maintain your well-being.")
                with col2:
                    st.image("Image/good.png")
            elif pred == 2:
                with col1:
                    st.header("Fair")
                    st.write("Your health is fair. It's important to focus on improving your diet and increasing physical activity.")
                    st.write("You might be experiencing some minor health issues. Consult a doctor to get a proper diagnosis and treatment.")
                with col2:
                    st.image("Image/fair.png")
            else:
                with col1:
                    st.header("Fair")
                    st.write("Your health is currently at risk. Seek immediate medical attention and follow the doctor's advice.")
                    st.write("You need to prioritize your health. Make lifestyle changes and follow a treatment plan as recommended.")
                with col2:
                    st.image("Image/bad.png")



    if smoker == 0:
        gender1 = st.selectbox("Select your Gender", [0, 1], format_func=lambda x: 'Male' if x == 1 else 'Female')
        country = st.selectbox("Which country do you belong?", [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33],format_func=fn)
        occupation = st.selectbox("Whats your Occupation?", [0, 1], format_func=fn1)
        self_emp = st.selectbox("Are you self employed?", [0, 1], format_func=lambda x: 'YES' if x == 1 else 'NO')
        treat = st.selectbox("Have you done before any kind of treatment?",[0,1],format_func=lambda x: 'YES' if x == 1 else 'NO')
        Indoor = st.selectbox("How much time you spent Indoor?", [0,1,2,3,4], format_func=fn2)
        grow_stress = st.selectbox("Does your stress Grow?", [0,1,2], format_func=fn3)
        habit = st.selectbox("Have you ever tried to change your habit?", [0, 1, 2], format_func=fn3)
        mental_his = st.selectbox("Does you have any kind of mental disease history?", [0, 1, 2], format_func=fn3)
        struggle = st.selectbox("Have you face issues in coping struggle?", [0, 1],format_func=lambda x: 'YES' if x == 1 else 'NO')
        interest = st.selectbox("Do have any kind of work interest?", [0, 1, 2], format_func=fn3)
        weak = st.selectbox("Do you have any kind of social weakness?", [0, 1, 2], format_func=fn3)
        interview = st.selectbox("Have you gone through any kind of mental health Interview?", [0, 1, 2], format_func=fn3)
        care = st.selectbox("Have ever care yourself regarding this?", [0, 1, 2], format_func=fn4)
        if st.button("Predict"):
            values2 = np.array([gender1,country,occupation,self_emp,treat,Indoor,grow_stress,habit,mental_his,struggle,interest,weak,interview,care]).reshape(1, -1)
            model2 = pickle.load(open("DT_model.pkl", "rb"))
            pred = model2.predict(values2)[0]
            st.write(pred)
            if pred == 0:
                with col1:
                    st.header("Good")
                    st.write("You're doing great! Keep practicing self-care, and explore new ways to nurture your well-being.")
                    st.write("Your mental health is strong. Consider engaging in activities that bring you joy and fulfillment.")
                with col2:
                    st.image("Image/good1.png")
            elif pred == 1:
                with col1:
                    st.header("Fair")
                    st.write("You might be experiencing some challenges. Try incorporating relaxation techniques like meditation or yoga.")
                    st.write("It's okay to not be okay. Reach out to friends, family, or a mental health professional for support.")
                with col2:
                    st.image("Image/fair1.png")
            else:
                with col1:
                    st.header("Bad")
                    st.write("Your mental health is a priority. Please reach out to a crisis hotline or mental health professional immediately.")
                    st.write("You're not alone. There are resources available to help you cope. Seek professional help as soon as possible.")
                with col2:
                    st.image("Image/bad1.png")

