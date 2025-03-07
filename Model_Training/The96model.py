import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import svm
import joblib
import os

# Load your dataset
data = pd.read_csv('./data/Training_data.csv')

# Display the first few rows of the dataset to understand its structure
print(data.head())

# separating the data and labels(outcomes)
x = data.drop(columns='outcome', axis=1)
y = data['outcome']

# Identify numeric and categorical columns
numeric_columns = x.select_dtypes(include=['int64', 'float64']).columns
categorical_columns = x.select_dtypes(include=['object']).columns

# Encode the 'gender' column
label_encoder = LabelEncoder()
x['gender'] = label_encoder.fit_transform(x['gender'])

# Apply StandardScaler to numeric columns
scaler = StandardScaler()
scaled_numeric_data = scaler.fit_transform(x[numeric_columns])

# Convert the scaled data back to a DataFrame
scaled_numeric_df = pd.DataFrame(scaled_numeric_data, columns=numeric_columns, index=x.index)

# Combine scaled numeric data with categorical data
standardized_data = pd.concat([scaled_numeric_df, x[categorical_columns]], axis=1)




# Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Train the classifier
classifier = RandomForestClassifier()
classifier.fit(x_train, y_train)

# Save the model to a file
# Define the path to save the model
save_path = r"./Saved_Model/diabetes_model.pkl"

# Ensure the directory exists
# os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Save the model
joblib.dump(classifier, save_path)
print(f"Model saved at {save_path}")

# Save the scaler
scaler_path = r"./Saved_Model/scaler.pkl"
joblib.dump(scaler, scaler_path)

# Save the label encoder
label_encoder_path = r"./Saved_Model/label_encoder.pkl"
joblib.dump(label_encoder, label_encoder_path)


# Evaluate the model
score = classifier.score(x_test, y_test)
print(f'Model accuracy: {score}')

y_pred = classifier.predict(x_test)
cm = confusion_matrix(y_test, y_pred)
print("confusion metrix", cm)

# following function gets user input and provides result
def get_user_prediction(x, label_encoder):
    # Load the model from the file
    classifier = joblib.load('/diabetes_predictor/Saved_Model/diabetes_model.pkl')
    print('Model loaded..!')

    # Define the user input
    print("Please enter the following details:")
    gender = input("Gender (male/female): ")
    age = int(input("Age: "))
    hypertension = int(input("Hypertension (0/1): "))
    heart_disease = int(input("Heart Disease (0/1): "))
    bmi = float(input("BMI: "))
    HbA1c_level = float(input("HbA1c Level: ")) 
    blood_glucose_level = float(input("Blood Glucose Level: "))
    gender = label_encoder.transform([gender])[0]

    # Create a dataframe for the input
    user_data = pd.DataFrame([[gender, age, hypertension, heart_disease, bmi, HbA1c_level, blood_glucose_level]], columns=x.columns)

    # Make prediction
    prediction = classifier.predict(user_data)

    # Output the result
    if prediction[0] == 1:
        print("The individual is likely to have diabetes in the near future.")
    else:
        print("The individual is unlikely to have diabetes in the near future.")

# Call the function to get user input and provide prediction
get_user_prediction(x, label_encoder)