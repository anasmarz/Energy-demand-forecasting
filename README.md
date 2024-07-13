# Energy Demand Forecasting API

## Overview

The **Energy Demand Forecasting API** is a robust tool designed to predict future energy consumption patterns for households and businesses using historical data. Powered by a trained ARIMA (AutoRegressive Integrated Moving Average) model, this Flask-based application provides accurate forecasts to help users make data-driven decisions about their energy needs.

## Features

- **Time Series Forecasting**: Predicts future energy consumption based on historical data.
- **ARIMA Model**: Utilizes the ARIMA model for precise time series analysis.
- **RESTful API**: Simple interface for requesting forecasts via HTTP requests.
- **Flexible Forecast Periods**: Allows users to specify the number of future periods to forecast.

## Endpoints

### `POST /predict`

Generates energy consumption forecasts for the specified number of future periods.

- **URL**: `http://127.0.0.1:5000/predict`
- **Method**: `POST`
- **Headers**:
  - `Content-Type: application/json`
- **Request Body**:
  ```json
  {
    "periods": 10
  }
  ```
  - `periods`: Number of future periods (e.g., days) for which to forecast energy consumption.

- **Response**:
  - **Content-Type**: `application/json`
  - **Body**:
    ```json
    [102.5, 104.3, 103.8, 105.0, 106.2, 107.1, 108.5, 109.0, 110.2, 111.3]
    ```
    - A JSON array of forecasted energy consumption values for the specified number of periods.

## Installation

To set up and run the Energy Demand Forecasting API locally:

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/yourusername/energy-demand-forecasting.git
   cd energy-demand-forecasting
   ```

2. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```sh
   python app.py
   ```

4. **Train the Model (if needed)**:
   ```sh
   python model.py
   ```

## Deployment

To deploy the application to a platform like Heroku, follow these steps:

1. **Create a `requirements.txt` File**:
   ```txt
   flask
   pandas
   statsmodels
   gunicorn
   ```

2. **Create a `Procfile`**:
   ```txt
   web: gunicorn app:app
   ```

3. **Deploy to Heroku**:
   ```sh
   git init
   git add .
   git commit -m "Initial commit"
   heroku create your-app-name
   git push heroku master
   ```

4. **Open Your Deployed App**:
   ```sh
   heroku open
   ```

## Usage

To request a forecast, use the following `curl` command:

```sh
curl -X POST -H "Content-Type: application/json" -d '{"periods": 10}' http://127.0.0.1:5000/predict
```

Or in PowerShell:

```powershell
$headers = @{
    "Content-Type" = "application/json"
}

$body = @{
    periods = 10
} | ConvertTo-Json

$response = Invoke-RestMethod -Uri http://127.0.0.1:5000/predict -Method Post -Headers $headers -Body $body
$response
```
