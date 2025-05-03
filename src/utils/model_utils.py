import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib

def load_model(model_path):
    model = joblib.load(model_path)
    return model

def predict_ridership(model, features):
    prediction = model.predict(features)
    return prediction

def evaluate_model(y_true, y_pred):
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    return rmse, mae, r2

def get_model_performance(model, X_test, y_test):
    y_pred = predict_ridership(model, X_test)
    return evaluate_model(y_test, y_pred)