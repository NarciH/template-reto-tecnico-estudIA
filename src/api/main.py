from fastapi import FastAPI
from pydantic import BaseModel
import tensorflow as tf
import numpy as np

app = FastAPI()

class SalesData(BaseModel):
    date: str
    sales: float

model = tf.keras.models.load_model('models/best_model.h5')

def preprocess_data(data):
    # Add your preprocessing steps here
    return np.array([data.sales])

@app.post("/predict")
def predict_sales(data: SalesData):
    preprocessed_data = preprocess_data(data)
    prediction = model.predict(np.array([preprocessed_data]))
    return {"prediction": prediction[0][0]}
