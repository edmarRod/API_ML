from fastapi import FastAPI
from pydantic import BaseModel
from model.model import predict

class ModelValues(BaseModel):
    age : float
    sex : float
    bmi : float
    bp : float
    s1 : float
    s2 : float
    s3 : float
    s4 : float
    s5 : float
    s6 : float

class Prediction(BaseModel):
    prediction : float

app = FastAPI()

@app.get("/")
async def root():
    return {'Hello':'API'}

@app.post("/prediction", response_model=Prediction)
async def predict_api(model_values: ModelValues):
    return {'prediction' : predict(model_values.dict())}

