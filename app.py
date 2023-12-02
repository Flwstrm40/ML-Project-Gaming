import pickle
from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load the ML model
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get input from the form
        age = int(request.form['age'])
        annual_income = int(request.form['annual_income'])
        spending_score = int(request.form['spending_score'])

        # Make a prediction using the ML model
        prediction = model.predict([[age, annual_income, spending_score]])[0]

        if prediction == 0:
            prediction_text = 'Kamu adalah orang yang sangat boros'
        elif prediction == 1:
            prediction_text = 'Kamu adalah orang yang boros'
        elif prediction == 2:
            prediction_text = 'Kamu adalah orang yang hemat'
        elif prediction == 3:
            prediction_text = 'Kamu sederhana'
        elif prediction == 4:
            prediction_text = 'Kamu seorang mahasiswa'

        return render_template('index.html', age=age, annual_income=annual_income, spending_score=spending_score, prediction=prediction_text)

if __name__ == '__main__':
    app.run(debug=True)
