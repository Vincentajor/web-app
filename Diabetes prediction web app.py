# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 10:50:36 2023

@author: RICKY
"""

import numpy as np 
import streamlit as st
import pickle
loaded_model=pickle.load(open("C:/Users/RICKY/Desktop/code plateu 6.0/trained_model.sav","rb"))
# creating a function for prediction
def diabetes_prediction (input_data):
    
# change the input to Numpy Array
    data = np.array(input_data)

#reshape the numpy array because we are predicting for
    input_data_reshaped = data.reshape (1, -1)

    prediction = loaded_model.predict (input_data_reshaped)
    print (prediction)
    if (prediction) [0]==0:
        return "This person is not diabetic"
    else:
        return "This person is diabetic. See a Doctor"
def main ():
    
    #Giving a Title 
    st.title ("Diabetes prediction Web App")
    
    #Getting Inputs From The User
    Pregnancies = st.text_input("Number of pregnancies")
    Glucose = st.text_input("Glucose Level")
    BloodPressure = st.text_input("Blood Pressure Value")
    SkinThickness = st.text_input("Skin Thickness Value")
    Insulin = st.text_input("Insulin Level")
    BMI = st.text_input ("Body Mass Index Level")
    DiabetesPedigreeFunction = st.text_input ("Diabetes Pedigree Function Value")
    Age = st.text_input("Age of The Person")
    
    #code for prediction
    diagnosis =""
    
    # Creating a button for prediction
    if st.button ("Diabetes Test Result"):
        diagnosis= diabetes_prediction ([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome])
    st.success(diagnosis)
       
    if__name__=="__main__"
    main()