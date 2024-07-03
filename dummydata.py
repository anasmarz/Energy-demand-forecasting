import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Data for yearly household electricity consumption per capita in Malaysia (2000-2016)
yearly_data = {
    2000: 489.10,
    2001: 530.70,
    2002: 557.90,
    2003: 588.00,
    2004: 609.40,
    2005: 632.30,
    2006: 673.70,
    2007: 697.90,
    2008: 715.30,
    2009: 754.80,
    2010: 801.30,
    2011: 800.10,
    2012: 847.60,
    2013: 885.50,
    2014: 902.60,
    2015: 935.40,
    2016: 998.70
}

# Convert the yearly data to a pandas DataFrame
yearly_df = pd.DataFrame(list(yearly_data.items()), columns=['Year', 'Consumption'])

# Create an empty DataFrame for the daily data
daily_df = pd.DataFrame(columns=['Date', 'Daily_Consumption'])

# Function to generate daily data from yearly data
def generate_daily_data(yearly_df):
    for i in range(len(yearly_df) - 1):
        start_year = yearly_df.loc[i, 'Year']
        end_year = yearly_df.loc[i + 1, 'Year']
        start_consumption = yearly_df.loc[i, 'Consumption']
        end_consumption = yearly_df.loc[i + 1, 'Consumption']
        
        start_date = datetime(start_year, 1, 1)
        end_date = datetime(end_year, 1, 1)
        delta_days = (end_date - start_date).days
        
        # Linear interpolation for daily consumption
        daily_consumptions = np.linspace(start_consumption, end_consumption, delta_days, endpoint=False)
        
        for day in range(delta_days):
            date = start_date + timedelta(days=day)
            daily_df.loc[len(daily_df)] = [date, daily_consumptions[day]]

    # Add the last year's data
    last_year = yearly_df.loc[len(yearly_df) - 1, 'Year']
    last_consumption = yearly_df.loc[len(yearly_df) - 1, 'Consumption']
    start_date = datetime(last_year, 1, 1)
    end_date = datetime(last_year + 1, 1, 1)
    delta_days = (end_date - start_date).days
    
    daily_consumptions = np.full(delta_days, last_consumption)
    
    for day in range(delta_days):
        date = start_date + timedelta(days=day)
        daily_df.loc[len(daily_df)] = [date, daily_consumptions[day]]

generate_daily_data(yearly_df)

# Convert 'Date' column to datetime
daily_df['Date'] = pd.to_datetime(daily_df['Date'])

# Display the first few rows of the daily dataset
print(daily_df.head())

# Save the dataset to a CSV file
daily_df.to_csv('daily_electricity_consumption.csv', index=False)
