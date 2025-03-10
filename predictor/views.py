import os
import joblib
import numpy as np
import pandas as pd
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import DiabetesPrediction

# Load the trained model and preprocessing tools
model_path = './home/Saved_Model/diabetes_model.pkl'
scaler_path = './home/Saved_Model/scaler.pkl'
label_encoder_path = './home/Saved_Model/label_encoder.pkl'

try:
    classifier = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    label_encoder = joblib.load(label_encoder_path)
    print("✅ Model, scaler, and label encoder loaded successfully.")
except Exception as e:
    print(f"❌ Error loading model or preprocessors: {e}")

@login_required(login_url='/login/')
def predictor_form(request):
    if request.method == 'POST':
           # Get user input from the form
           gender = request.POST.get('gender')
           age = int(request.POST.get('age'))
           hypertension = int(request.POST.get('hypertension'))
           heart_disease = int(request.POST.get('heart_disease'))
           bmi = float(request.POST.get('bmi'))
           HbA1c_level = float(request.POST.get('HbA1c_level'))
           blood_glucose_level = float(request.POST.get('blood_glucose_level'))

           # Encode gender
           gender_encoded = label_encoder.transform([gender])[0]

           # Create a DataFrame for the input
           user_data = pd.DataFrame([[gender_encoded, age, hypertension, heart_disease, bmi, HbA1c_level, blood_glucose_level]],
                                    columns=['gender', 'age', 'hypertension', 'heart_disease', 'bmi', 'HbA1c_level', 'blood_glucose_level'])

           # Make prediction
           prediction = classifier.predict(user_data)
           
           # Save the prediction to the database
           DiabetesPrediction.objects.create(
            user=request.user,
            gender=gender,  # Store original string ("male" or "female")
            age=age,
            hypertension=hypertension,
            heart_disease=heart_disease,
            bmi=bmi,
            HbA1c_level=HbA1c_level,
            blood_glucose_level=blood_glucose_level,
            prediction=prediction[0]
        )
           # Determine result
           result = "The individual is likely to have diabetes in the near future." if prediction[0] == 1 else "The individual is unlikely to have diabetes in the near future."

           return render(request, 'result.html', {'result': result})

    return render(request, 'form.html')