from prophet import Prophet
import pandas as pd

class EngagementPredictor:
    def __init__(self):
        self.model = Prophet()

    def predict_engagement(self, historical_data: pd.DataFrame, periods: int = 7) -> pd.DataFrame:
        self.model.fit(historical_data)
        future = self.model.make_future_dataframe(periods=periods)
        forecast = self.model.predict(future)
        return forecast[["ds", "yhat"]]
