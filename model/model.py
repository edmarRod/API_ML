from typing import Dict
import joblib
import numpy as np
from sklearn.base import BaseEstimator

def load_model() -> BaseEstimator:
    model = joblib.load('model/rf_model.joblib')
    return model

def predict(dict: Dict) -> float:
    model = load_model()
    arr = np.array(list(dict.values())).reshape(1,-1)
    return model.predict(arr)
