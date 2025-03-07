from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.predictor_form, name='predictor_form'),
]
