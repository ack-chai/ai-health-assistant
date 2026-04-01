from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel
from groq import Groq
import os
from dotenv import load_dotenv

# Load env variables
load_dotenv()

app = FastAPI()

# -----------------------------
# Request model
# -----------------------------
class ChatRequest(BaseModel):
    message: str

# -----------------------------
# Load ML model
# -----------------------------
model = joblib.load("model/diabetes_model.pkl")

# -----------------------------
# Groq client
# -----------------------------
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# -----------------------------
# Home route
# -----------------------------
@app.get("/")
def home():
    return {"message": "AI Health Assistant running"}

# -----------------------------
# Predict route
# -----------------------------
@app.post("/predict")
def predict(data: dict):
    try:
        features = np.array([
            data["Pregnancies"],
            data["Glucose"],
            data["BloodPressure"],
            data["SkinThickness"],
            data["Insulin"],
            data["BMI"],
            data["DiabetesPedigreeFunction"],
            data["Age"]
        ]).reshape(1, -1)

        prediction = model.predict(features)[0]

        return {
            "prediction": int(prediction),
            "risk": "High" if prediction == 1 else "Low"
        }

    except Exception as e:
        return {"error": str(e)}

# -----------------------------
# Chat route (FIXED MODEL)
# -----------------------------
@app.post("/chat")
def chat(user_input: ChatRequest):
    try:
        message = user_input.message.lower()

        # simple symptom mapping
        sample_data = {
            "Pregnancies": 0,
            "Glucose": 140 if "tired" in message or "weak" in message else 100,
            "BloodPressure": 80,
            "SkinThickness": 20,
            "Insulin": 85,
            "BMI": 30,
            "DiabetesPedigreeFunction": 0.5,
            "Age": 25
        }

        # prediction
        features = np.array(list(sample_data.values())).reshape(1, -1)
        prediction = model.predict(features)[0]
        risk = "High" if prediction == 1 else "Low"

        # AI response (WORKING MODEL)
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # ✅ THIS IS THE FIX
            messages=[
                {"role": "system", "content": "You are a helpful medical assistant."},
                {"role": "user", "content": message}
            ]
        )

        return {
            "reply": response.choices[0].message.content,
            "risk": risk
        }

    except Exception as e:
        return {"error": str(e)}