from logging import debug
from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

#load a model
model = joblib.load('hiring_model.pkl')

@app.route('/')
def welcome():
    return render_template('base.html')
    
@app.route('/predict', methods=['POST'])
def predict():
    exp = request.form.get('experience')
    tst_scr = request.form.get('test_score')
    int_scr = request.form.get('interview_score')


    prediction = model.predict([[int(exp),int(tst_scr),int(int_scr)]])

    output=round(prediction[0],2)
    return render_template('base.html', prediction_text = f"Employee salary will be ${output}")

    return 'Your form is submitted!'

app.run(debug=True)