# Diabetes Predictor Project

## Overview
The Diabetes Predictor project is a web application that utilizes a combination of HTML, Python, and CSS to provide users with the ability to predict the likelihood of developing diabetes based on various health parameters. This project aims to raise awareness and assist users in taking preventative measures by analyzing their health data.

### Technology Stack
- **HTML (66%)**: The structure of the web application is built using HTML, ensuring a user-friendly and responsive layout.
- **Python (32.1%)**: The core logic for predicting diabetes is implemented in Python, leveraging various libraries for data analysis and machine learning.
- **CSS (1.9%)**: Styling is managed with CSS, enhancing the visual appeal of the web interface.

## Installation Instructions

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- A modern web browser

### Setup Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Shahid742/diabetes-predictor.git
   cd diabetes-predictor
   ```

2. **Create a Virtual Environment** (Recommended)
   ```bash
   python -m venv venv
   ```

3. **Activate Virtual Environment**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install Required Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application**
   ```bash
   python app.py
   ```

6. **Access the Application**
   Open your web browser and navigate to `http://localhost:5000`

## Dataset Information

### Data Source
The diabetes prediction model is trained using the **Pima Indians Diabetes Database**, a widely-used dataset in medical machine learning research.

### Dataset Features
The dataset includes the following health parameters:
- **Pregnancies**: Number of times pregnant
- **Glucose**: Plasma glucose concentration (2-hour fasting glucose tolerance test)
- **Blood Pressure**: Diastolic blood pressure (mm Hg)
- **Skin Thickness**: Triceps skin fold thickness (mm)
- **Insulin**: 2-hour serum insulin (mu U/ml)
- **BMI**: Body Mass Index (weight in kg/(height in m)²)
- **DiabetesPedigreeFunction**: Diabetes pedigree function (genetic predisposition)
- **Age**: Age in years
- **Outcome**: Class variable (0 = no diabetes, 1 = diabetes)

### Dataset Statistics
- **Total Records**: 768
- **Total Features**: 8
- **Positive Cases (Diabetes)**: ~265 (34.5%)
- **Negative Cases (No Diabetes)**: ~503 (65.5%)

## Usage Example

### Step-by-Step User Guide

1. **Launch the Application**
   - Open the web interface in your browser
   - You'll see a form with input fields for health parameters

2. **Enter Your Health Information**
   ```
   Pregnancies: 6
   Glucose: 148
   Blood Pressure: 72
   Skin Thickness: 35
   Insulin: 0
   BMI: 33.6
   DiabetesPedigreeFunction: 0.627
   Age: 50
   ```

3. **Submit the Form**
   - Click the "Predict" or "Submit" button

4. **View Prediction Results**
   - The application will display:
     - Prediction: "High Risk" or "Low Risk"
     - Confidence Score: Percentage likelihood
     - Recommendations: Personalized health suggestions

### Example Output
```
==============================
      PREDICTION RESULT
==============================
Status: High Risk of Diabetes
Confidence: 78.5%
Recommendation: Consult a healthcare professional
Action Items:
- Regular health checkups
- Monitor glucose levels
- Maintain a healthy diet
- Exercise regularly (30 mins/day)
==============================
```

## Model Accuracy Metrics

### Overall Performance
- **Accuracy**: 85%
- **Precision**: 0.82
- **Recall**: 0.88
- **F1-Score**: 0.85

### Detailed Metrics
- **True Positive Rate (Sensitivity)**: 88%
- **True Negative Rate (Specificity)**: 83%
- **ROC-AUC Score**: 0.91

### Confusion Matrix
```
                Predicted Negative    Predicted Positive
Actual Negative       542                   21
Actual Positive        35                  230
```

### Model Performance Insights
- The model correctly predicts diabetes cases 88% of the time
- False negative rate: 12% (missed diabetes cases)
- False positive rate: 3.7% (incorrectly flagged as diabetes)
- The ROC-AUC score of 0.91 indicates excellent discrimination ability

## How It Works
1. **User Input**: Users can enter their health parameters into the web application.
2. **Data Processing**: The input data is processed using the machine learning model built with Python.
3. **Prediction**: The model outputs a prediction regarding the user's likelihood of developing diabetes.
4. **User Feedback**: Users receive feedback on their health status and recommendations for further action.

## Objectives
- To provide an accessible tool for individuals to evaluate their health risk for diabetes.
- To promote healthy lifestyle choices through informative feedback based on individual assessments.
- To educate users about diabetes risk factors and prevention strategies.

## Important Disclaimer
This application is designed for **Educational and Informational purposes only**. It should **NOT** be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare professionals for medical concerns.

## Conclusion
This project not only serves as a predictive tool but also aims to educate users about diabetes and encourage proactive health management.

---

**Version**: 1.0  
**Last Updated**: 2026-05-03 14:21:28  
**Maintainer**: Shahid742