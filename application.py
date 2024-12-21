import pickle
from flask import Flask, request, render_template
import numpy as np
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app = application

# Load pre-trained models
ridge_model = pickle.load(open('models/ridge.pkl', 'rb'))
standard_scaler = pickle.load(open('models/scaler.pkl', 'rb'))

# Route for home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'POST':
        Temperature = float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))

        new_data_scaled = standard_scaler.transform(
            [[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]]
        )
        result = ridge_model.predict(new_data_scaled)
        fwi_value = result[0]

        if fwi_value < 5.2:
            fire_risk = "Very low danger"
            fire_risk_class = "very-low"
        elif 5.2 <= fwi_value < 11.2:
            fire_risk = "Low danger"
            fire_risk_class = "low"
        elif 11.2 <= fwi_value < 21.3:
            fire_risk = "Moderate danger"
            fire_risk_class = "moderate"
        elif 21.3 <= fwi_value < 38.0:
            fire_risk = "High danger"
            fire_risk_class = "high"
        elif 38.0 <= fwi_value <= 50.0:
            fire_risk = "Very high danger"
            fire_risk_class = "very-high"
        else:
            fire_risk = "Extreme danger"
            fire_risk_class = "extreme"

        return render_template(
            'home.html', result=fwi_value, fire_risk=fire_risk, fire_risk_class=fire_risk_class
        )

    return render_template('home.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0")
