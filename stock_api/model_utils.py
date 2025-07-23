import pandas as pd
from joblib import load

class StockPredictor:
    def __init__(self):
        print("🔁 Loading model artifacts...")
        self.model = load("rf_model.joblib")
        self.scaler = load("scaler.joblib")
        self.le = load("label_encoder.joblib")
        self.df = pd.read_csv("cleaned_stock_data.csv", parse_dates=["date"])
        self.features = ['Name_encoded', 'daily_return', '5day_ma', '10day_ma']
        print("✅ Model ready.")

    def predict_top_stocks(self, user_date, top_n=5):
        user_date = pd.to_datetime(user_date)
        available_dates = self.df['date'].unique()

        try:
            closest_date = max(d for d in available_dates if d <= user_date)
        except:
            return {"error": "No available trading data before or on this date."}

        day_data = self.df[self.df['date'] == closest_date].copy()
        if day_data.empty:
            return {"error": "No data for this date."}

        X_day = self.scaler.transform(day_data[self.features])
        preds = self.model.predict_proba(X_day)[:, 1]
        day_data['Up_Prob'] = preds

        top_stocks = day_data.sort_values('Up_Prob', ascending=False).head(top_n)
        return {
            "date_used": str(closest_date.date()),
            "top_stocks": top_stocks[['Name', 'Up_Prob']].to_dict(orient='records')
        }
