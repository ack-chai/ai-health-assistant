🧠 AI Health Assistant with Predictive Insights


🚀 Overview

This project is an AI-powered healthcare assistant that analyzes user symptoms and provides predictive insights using a combination of Machine Learning and Generative AI.

It allows users to interact through a chat interface, receive medical explanations, and view disease risk predictions based on structured health parameters.

✨ Features
💬 Chat-based interface for symptom input
🧠 AI-powered explanation using LLM (Groq API)
📊 Diabetes risk prediction using Machine Learning
📈 Visual risk trend graph
🌐 Full-stack application (React + FastAPI)
☁️ Deployable backend and frontend
🏗️ Tech Stack
Frontend
React.js
Axios
Chart.js
Backend
FastAPI
Python
Machine Learning
Random Forest Classifier (scikit-learn)
PIMA Indians Diabetes Dataset
AI Integration
Groq API (LLM)
🧠 How It Works
User enters symptoms in natural language
LLM interprets symptoms and converts them into structured medical parameters
ML model predicts disease risk (diabetes)
System returns:
AI-generated explanation
Risk level (High / Low)
Graph visualization
📂 Project Structure
ai-health-assistant/
│
├── backend/
│   ├── main.py
│   ├── model/
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   └── App.js
│
└── README.md
⚙️ Installation & Setup
🔧 Backend
cd backend
pip install -r requirements.txt
python -m uvicorn main:app --reload
💻 Frontend
cd frontend
npm install
npm start
🌐 API Endpoints
/chat
Input: User symptoms
Output: AI explanation + risk prediction
/predict
Input: Health parameters
Output: Risk level
📊 Example Input
{
  "message": "I feel tired and weak"
}
📈 Example Output
{
  "reply": "You may be experiencing fatigue due to...",
  "risk": "High"
}
⚠️ Disclaimer

This project is a prototype for educational purposes only.
It is not intended for real medical diagnosis or treatment.

🚀 Future Improvements
Multi-disease prediction
Better dataset & model accuracy
Real-time health monitoring
Voice-based interaction
Improved explainability
👨‍💻 Author

Built as part of an AI/ML project to demonstrate full-stack integration of Machine Learning and Generative AI.
