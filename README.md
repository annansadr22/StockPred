# 📈 StockPred — AI-Powered Stock Prediction Dashboard

Welcome to **StockPred**, a futuristic stock prediction system that uses machine learning to forecast the most promising stocks for the next trading day. Built with FastAPI + React + Tailwind + 🔮 RandomForest + 📊 Financial Data.

---

## 🚀 How to Run It Locally

### 1. Clone the Repository

```bash
git clone https://github.com/annansadr22/StockPred.git
cd StockPred
```

---

### 2. Train the ML Model

> Run this once to prepare your trained model and preprocessed dataset.

```bash
cd stock_api
python train_model.py
```

This will generate:

- `rf_model.joblib`
- `scaler.joblib`
- `label_encoder.joblib`
- `cleaned_stock_data.csv`

These files are used by the FastAPI backend for AI predictions.

---

### 3. Start the Backend API (FastAPI)

```bash
uvicorn main:app --reload
```

- 🔗 API runs at: [http://127.0.0.1:8000](http://127.0.0.1:8000)  
- 📚 Swagger Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

### 4. Start the Frontend (React + Vite)

In a new terminal window:

```bash
cd ../frontend
npm install
npm run dev
```

Open in browser: [http://localhost:5173](http://localhost:5173)

You can:

- Select a historical date 📅
- Choose how many stocks to predict (Top N) 🔢
- View AI-driven stock predictions and probabilities 💹

---

## ✨ Features

- 🔮 Predicts stock movement using a trained ML model
- 📊 Beautiful interactive dashboard (React + Tailwind CSS)
- ⚡ AI-powered confidence ratings per stock
- 📅 Simulates real market predictions on historical dates
- 💡 FastAPI backend with Swagger documentation
- 🔁 Real-time data pipeline with clean architecture

---

## 🧠 Tech Stack

| Layer     | Technology                            |
|-----------|----------------------------------------|
| Backend   | Python, FastAPI                        |
| ML Model  | scikit-learn (RandomForestClassifier)  |
| Frontend  | React + TypeScript + Tailwind CSS      |
| Styling   | Glassmorphism, Lucide Icons            |
| Dev Tools | Vite, Git, VS Code, Uvicorn            |

---

## 🧼 .gitignore Notes

These files are intentionally ignored to reduce repo size and avoid leaking large artifacts:

```gitignore
# Model artifacts & data
stock_api/*.joblib
stock_api/*.csv

# Node & build
frontend/node_modules/
frontend/dist/
frontend/build/

# Secrets
.env

# OS junk
.DS_Store
Thumbs.db
```

---

## 🛠 To Do

- [ ] Connect to real-time stock APIs
- [ ] Deploy backend on Render
- [ ] Deploy frontend on Vercel
- [ ] Add stock performance chart over time
- [ ] Enable historical prediction archive

---

## 👨‍💻 Author

**Anurag Fulare**  
📍 [GitHub](https://github.com/annansadr22) • 💼 [LinkedIn](https://www.linkedin.com/in/anuragfulare)

> _"Predict tomorrow's market. Today."_ 🚀
