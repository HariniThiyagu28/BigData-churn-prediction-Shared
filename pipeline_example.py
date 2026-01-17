
# Churn Prediction Pipeline - Usage Example

import joblib
import pandas as pd
from datetime import datetime

class ChurnPredictor:
    def __init__(self):
        self.model = joblib.load('best_churn_model.pkl')
        self.scaler = joblib.load('scaler.pkl')

    def predict(self, customer_data):
        # Preprocess and predict
        processed = self.scaler.transform([customer_data])
        prediction = self.model.predict(processed)[0]
        probability = self.model.predict_proba(processed)[0][1]
        return prediction, probability

# Usage:
# predictor = ChurnPredictor()
# result = predictor.predict([feature1, feature2, ...])
