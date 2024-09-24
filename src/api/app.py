from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np

# Load the saved RandomForest model
model = joblib.load('../notebooks/model.pkl')

app = Flask(__name__)

@app.route('/')
def home():
    return "RandomForest Model API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    input_features = np.array(data['features']).reshape(1, -1)
    feature_names = [
        'Id', 
        'CompetitionDistance', 
        'CompetitionOpenSinceMonth', 
        'CompetitionOpenSinceYear', 
        'Promo2', 
        'Promo2SinceWeek', 
        'Promo2SinceYear', 
        'DayOfWeek', 
        'Customers', 
        'Open', 
        'Promo', 
        'SchoolHoliday', 
        'Year', 
        'Month', 
        'Day', 
        'WeekOfYear', 
        'DayOfMonth', 
        'IsMonthStart', 
        'IsMonthEnd', 
        'StoreType_b', 
        'StoreType_c', 
        'StoreType_d', 
        'Assortment_c', 
        'StateHoliday_a', 
        'StateHoliday_b', 
        'StateHoliday_c', 
        'PromoMonths'
    ]
    print('after')
    print(input_features)
    # Make a prediction
    input_df = pd.DataFrame(input_features, columns=feature_names)
    prediction = model.predict(input_df)
    
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)