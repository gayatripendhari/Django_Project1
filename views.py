from django.shortcuts import render
import pandas as pd
import joblib
import numpy as np

# Create your views here.
def index(request):
    if request.method == "POST":
        yrs = request.POST['yrs']
        yrs = float(yrs)
        print(yrs,type(yrs))
        #load the saved model
        loaded_model = joblib.load('model/salary_prediction_model.pkl')
        #Predict the salary based on user input
        predicted_salary = loaded_model.predict(np.array([[yrs]]))
        print(predicted_salary[0])
    return render(request,'index.html',{"predicted_salary":predicted_salary })

def log_in(request):
    return render(request,'login.html')

