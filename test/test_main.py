from fastapi.testclient import TestClient

from .main import app


client = TestClient(app)


fake_pred = {"age": 0.0380759064, "sex": 0.0506801187, "bmi": 0.0616962065, "bp": 0.021872355, "s1": -0.0442234984,
           "s2": -0.0348207628, "s3": -0.0434008457, "s4": -0.002592262, "s5": 0.0199084209, "s6": -0.0176461252}

def test_predict():
    response = client.post('/prediction', json=fake_pred)
    assert response.status_code == 200
    assert type(response['prediction']) == float
