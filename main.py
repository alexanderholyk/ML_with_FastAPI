# main.py
# Alex Holyk

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import joblib
import random

app = FastAPI(title="Sentiment Analysis API")

# Load the trained model
file_name = 'sentiment_model.pkl'
try:
    model = joblib.load(file_name)
    print("Model loaded successfully.")
except FileNotFoundError:
    print(f"Error: Model file {file_name} not found.")
    model = None

# Define the input data model
class PredictionInput(BaseModel):
    text: str

# Health check endpoint
@app.get("/health")
def health_check():
    """ 
    This endpoint is used to verify that the API server is running and responsive.
    """
    return {"status": "ok"}

# Predict sentiment endpoint
@app.post("/predict")
def predict(input_data: PredictionInput):
    """
    Takes a text input and returns a sentiment prediction.
    """
    if model is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Model is not loaded. Cannot make predictions."
        )
    
    prediction = model.predict([input_data.text])
    return {"sentiment": prediction[0]}

# Predict with probability endpoint
@app.post("/predict_proba")
def predict_proba(input_data: PredictionInput):
    """
    Takes a text input and returns the predicted sentiment along with its confidence score.
    """
    if model is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Model is not loaded. Cannot make predictions."
        )
    
    prediction = model.predict([input_data.text])
    probabilities = model.predict_proba([input_data.text])

    if prediction == "positive":
        probability = probabilities[0][1]
    else:
        probability = probabilities[0][0]

    return {
        "sentiment": prediction[0],
        "probability": probability
    }

# Get training example endpoint
@app.get("/example")
def example():
    """
    Returns a random review from the original IMDB training dataset. This is useful for testing the prediction endpoints. 
    """
    
    file_name = 'IMDB Dataset.csv'
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
        print(f"{file_name} loaded successfully.")
    except FileNotFoundError:
        print(f"Error: Reviews file {file_name} not found.")
        lines = []

    if not lines:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No reviews available."
        )
    
    random_line = random.choice(lines)
    return {"review": random_line.strip()}

# Can now run in terminal: uvicorn main:app --reload