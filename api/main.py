from fastapi import FastAPI
from pydantic import BaseModel
import tensorflow as tf

app = FastAPI()

class PredictionRequest(BaseModel):
    data: list

@app.on_event("startup")
def load_model():
    global model
    model = tf.keras.models.load_model('models/best_model.h5')

@app.post("/predict")
def predict(request: PredictionRequest):
    data = request.data
    # Preprocess the data if necessary
    predictions = model.predict(data)
    return {"predictions": predictions.tolist()}
