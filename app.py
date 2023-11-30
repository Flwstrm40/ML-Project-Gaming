from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the ML model
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict(predict_list):
    prediction = np.array(predict_list).reshape(1,3) # Karena inputnya 3
    load = pickle.load(open('model.pkl','rb'))
    result = load.predict(prediction)
    return result
    # # Get input from the form
    # features = [float(x) for x in request.form.values()]

    # # Make predictions using the ML model
    # prediction = model.predict([features])[0]

    # return render_template('index.html', prediction=prediction)

def result():
    if request.method == 'POST':
        name = request.form['name']
        gender = request.form['gender']
        age = request.form['age']
        annual_income = request.form['annual_income']
        spending_score = request.form['spending_score']

        predict_list = list(map(int, [age, annual_income, spending_score]))
        result = predict(predict_list)

        if int(result) == 0:
            prediction = 'Kamu adalah orang yang sangat boros'
        elif int(result) == 1:
            prediction = 'Kamu adalah orang yang boros'
        elif int(result) == 2:
            prediction = 'Kamu adalah orang yang hemat'
        elif int(result) == 3:
            prediction = 'Kamu sederhana'
        elif int(result) == 4:
            prediction = 'Kamu seorang mahasiswa'

        return render_template('index.html', prediction=result)


if __name__ == '__main__':
    app.run(debug=True)
