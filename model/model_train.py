from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_diabetes

import joblib


x, y = load_diabetes(return_X_y=True)
rf = RandomForestClassifier(n_estimators=10, max_depth=20)
rf.fit(x,y)

joblib.dump(rf, 'rf_model.joblib')