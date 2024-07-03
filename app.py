from flask import Flask, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

# Load the trained model
with open('energydemand_model.pkl', 'rb') as pkl_file:
    model_fit = pickle.load(pkl_file)

@app.route('/')
def home():
    return "Energy Consumption Forecasting API"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    periods = data.get('periods', 10)  # Number of periods to forecast, default to 10

    # Make predictions
    forecast = model_fit.forecast(steps=periods)
    forecast = forecast.tolist()  # Convert forecast to list

    return jsonify(forecast)

if __name__ == '__main__':
    app.run(debug=True)
