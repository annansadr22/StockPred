from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from model_utils import StockPredictor

app = FastAPI(title="Stock Predictor API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or ["http://localhost:5173"] for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
predictor = StockPredictor()

@app.get("/")
def root():
    return {"message": "Welcome to the Stock Prediction API!"}

@app.get("/predict")
def predict(date: str = Query(..., example="2018-02-15"), top_n: int = Query(5)):
    return predictor.predict_top_stocks(date, top_n)
