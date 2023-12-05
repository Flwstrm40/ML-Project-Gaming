import pickle
from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load the ML model
model = joblib.load('model_baru.pkl')

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
        # gender = int(request.form['gender'])

        # Make a prediction using the ML model
        prediction = model.predict([[age, annual_income, spending_score]])[0]

        # if prediction == 0:
        #     prediction_text = 'Kamus orang memiliki ekonomi rendah dengan pengeluaran rendah'
        #     image = 'static/cluster0.jpg'
        #     # 
        # elif prediction == 1:
        #     prediction_text = 'Kamu adalah orang yang moderat pengeluarannya'
        #     image = 'static/cluster1.jpg'
        # elif prediction == 2:
        #     prediction_text = 'Kamu sudah pensiun dengan investasi yang bagus'
        #     image = 'static/cluster2.jpg'
        # elif prediction == 3:
        #     prediction_text = 'Kamu muda dan suka berfoya-foya 😞'
        #     image = 'static/cluster3.jpg'
        #     # annual tinggi, spending rendah
        # elif prediction == 4:
        #     prediction_text = 'Kamu orang yang sederhana'
        #     image = 'static/cluster4.jpg'
        #     # Linear, annual tengah, spending tengah
        # elif prediction == 5:
        #     prediction_text = 'Kamu adalah orang yang hemat 👍🏿'
        #     image = 'static/cluster4.jpg'
        if prediction == 0:
            prediction_text = 'Kamu sudah pensiun dengan investasi yang bagus'
            image = 'static/cluster0.jpg'
            # 
        elif prediction == 1:
            prediction_text = 'Kamu adalah orang yang hemat 👍🏿'
            image = 'static/cluster1.jpg'
            # annual tinggi, spending rendah
        elif prediction == 2:
            prediction_text = 'Kamu suka berfoya-foya 😞'
            image = 'static/cluster2.jpg'
        elif prediction == 3:
            prediction_text = 'Kamu orang yang sederhana'
            image = 'static/cluster3.jpg'
            # Linear, annual tengah, spending tengah
        elif prediction == 4:
            prediction_text = 'Kamu adalah orang yang moderat pengeluarannya'
            image = 'static/cluster4.jpg'
        elif prediction == 5:
            prediction_text = 'Kamus orang memiliki ekonomi rendah dengan pengeluaran rendah'
            image = 'static/cluster5.jpg'

        return render_template('index.html', age=age, annual_income=annual_income, spending_score=spending_score, prediction=prediction_text, image=image)

if __name__ == '__main__':
    app.run(debug=True)
