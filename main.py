from fastapi import FastAPI, HTTPException
import random
import time

app = FastAPI()

# Simulated AI Model Storage
model_status = {"trained": False, "last_trained": None}


@app.get("/status")
async def get_status():
    """Returns system and model status"""
    return {
        "server": "Running",
        "model_trained": model_status["trained"],
        "last_trained": model_status["last_trained"]
    }


@app.post("/train")
async def train_model():
    """Simulates training an AI model"""
    time.sleep(2)  # Simulating training time
    model_status["trained"] = True
    model_status["last_trained"] = time.ctime()
    return {"message": "Model trained successfully", "last_trained": model_status["last_trained"]}


@app.get("/predict")
async def predict():
    """Generates a mock prediction from the trained model"""
    if not model_status["trained"]:
        raise HTTPException(status_code=400, detail="Model is not trained yet")

    prediction = random.choice(["cat", "dog", "bird"])
    return {"prediction": prediction, "confidence": round(random.uniform(0.7, 1.0), 2)}
