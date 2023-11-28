from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the ML model
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input from the form
    features = [float(x) for x in request.form.values()]

    # Make predictions using the ML model
    prediction = model.predict([features])[0]

    return render_template('index.html', prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)
