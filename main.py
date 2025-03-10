from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load the trained models
kmeans_model = joblib.load("kmeans.joblib")
kmodes_model = joblib.load("kmodes_model.joblib")

# Load the scalers
scaler_kmeans = joblib.load("Models/scaler.joblib")  # For K-Means
scaler_kmodes = joblib.load("Models/scaler2.joblib")  # For K-Modes

# Define cluster mappings for each model
cluster_mapping_kmeans = {
    0: "The Reliable Basics",
    1: "The Hidden Gems",
    2: "The Crowd Favorites"
}

cluster_mapping_kmodes = {
    0: "Quick Learning",
    1: "Career Growth",
    2: "Specialized Skills",
    3: "Comprehensive Programs"
}

# Initialize FastAPI app
app = FastAPI()

# Define request model for input data
class InputData(BaseModel):
    model_type: str  # "kmeans" or "kmodes"
    features: list  # Feature values for prediction

@app.post("/predict")
async def predict_cluster(data: InputData):
    input_array = np.array([data.features]).reshape(1, -1)

    # Choose the appropriate model and scaler
    if data.model_type.lower() == "kmeans":
        scaled_input = scaler_kmeans.transform(input_array)
        cluster_label = kmeans_model.predict(scaled_input)[0]
        cluster_name = cluster_mapping_kmeans.get(cluster_label, "Unknown Cluster")

    elif data.model_type.lower() == "kmodes":
        scaled_input = scaler_kmodes.transform(input_array)
        cluster_label = kmodes_model.predict(scaled_input)[0]
        cluster_name = cluster_mapping_kmodes.get(cluster_label, "Unknown Cluster")

    else:
        return {"error": "Invalid model type. Choose 'kmeans' or 'kmodes'."}

    return {"cluster": cluster_label, "cluster_name": cluster_name}
