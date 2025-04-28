from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import joblib
import numpy as np

# Load scaler dan model
scaler = joblib.load("scaler.pkl")
model = joblib.load("kmeans_model.pkl")

# FastAPI instance
app = FastAPI(debug=True)

@app.get('/')
def home():
    return {'Message: Clustering the Countries by using Unsupervised Learning for HELP International'}

# Definisikan inputan API
class InputData(BaseModel):
    child_mort: float = Field(..., example=111)
    health: float = Field(..., example=2)
    income: float = Field(..., example=1000)
    life_expec: float = Field(..., example=33)
    gdpp_log: float = Field(..., example=6.907)

@app.post("/predict_cluster")
def predict_cluster(data: InputData):
    try:
        # Mengambil data input dan mengonversi kategori 'continent' menjadi nilai numerik
        input_data = [
            [data.child_mort, data.health, data.income, 
            data.life_expec, data.gdpp_log]
        ]

        # Normalisasi data
        input_data_norm = scaler.transform(input_data)

        # Prediksi cluster menggunakan model KMeans
        prediction = model.predict(input_data_norm)

        # Menentukan nama cluster berdasarkan hasil prediksi
        cluster = prediction[0]
        cluster_label = f"Cluster {cluster + 1}"  # Cluster diberi label 1, 2, atau 3

        return {
            "input": data.dict(),
            "prediksi_cluster": cluster_label
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))