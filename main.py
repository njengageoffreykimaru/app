from flask  import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the model
model1 = joblib.load("fertilizerrecommend.pkl")
model =joblib.load("croprecommedation.pkl")
models=joblib.load("cropyieldprediction.pkl")


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
   try:
        # Get the input values from the form and convert them to float
        nitrogen = float(request.form['nitrogen'])
        potassium = float(request.form['potassium'])
        phosphorous = float(request.form['phosphorous'])

        # Make a prediction using the loaded model
        prediction = model1.predict([[nitrogen, potassium, phosphorous]])

        return render_template('index.html', prediction=prediction[0])

   except ValueError:
        error_message = "Invalid input. Please enter numeric values for nitrogen, potassium, and phosphorous."
        return render_template('index.html', error=error_message)
@app.route('/croppredict')
def croprecommendation():
    return render_template('crop.html')


@app.route('/croppredict', methods=['POST'])
def croppredict():
    try:
        # Get the input values from the form and convert them to float
        nitrogen = float(request.form['Nitrogen'])
        phosphorus = float(request.form['Phosphorus'])
        Potassium = float(request.form['Potassium'])
        Temperature = float(request.form['Temperature'])
        Humidity = float(request.form['Humidity'])
        Ph = float(request.form['Ph'])
        Rainfall = float(request.form['Rainfall'])

        # Make a prediction using the loaded model
        prediction = model.predict([[nitrogen,phosphorus,Potassium,Temperature,Humidity,Ph,Rainfall]])

        return render_template('crop.html', prediction=prediction[0])

    except ValueError:
        errors_message = "Invalid input. Please enter numeric values for nitrogen, potassium, and phosphorous."
        return render_template('crop.html', error=errors_message)

@app.route('/yieldpredict')
def yieldprediction():
    return render_template('cropyieldpredction.html')

@app.route('/yieldpredict', methods=['POST'])
def yieldpredict():
    try:
        # Get the input values from the form and convert them to float
        Temperature = float(request.form['Temperature'])
        humidity = float(request.form['humidity'])
        soil_moisture = float(request.form['soil moisture'])
        area = float(request.form['area'])

        # Make a prediction using the loaded model
        prediction = models.predict([[Temperature, humidity, soil_moisture, area]])

        return render_template('cropyieldpredction.html', prediction=prediction[0])

    except ValueError:
        error_message = "Invalid input. Please enter numeric values for the input fields."
        return render_template('cropyieldpredction.html', error=error_message)






if __name__ == '__main__':
    app.run(debug=True)
