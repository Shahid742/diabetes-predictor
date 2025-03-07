from django.db import models
from django.contrib.auth.models import User

class DiabetesPrediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)  # Stores "male" or "female"
    age = models.IntegerField()
    hypertension = models.IntegerField()  # 0 or 1
    heart_disease = models.IntegerField()  # 0 or 1
    bmi = models.FloatField()
    HbA1c_level = models.FloatField()
    blood_glucose_level = models.FloatField()
    prediction = models.IntegerField()  # 0 or 1 (0: Unlikely, 1: Likely)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prediction for {self.user.username} on {self.created_at}"