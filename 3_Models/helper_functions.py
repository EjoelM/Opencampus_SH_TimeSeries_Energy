import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_absolute_percentage_error, r2_score


def create_error_metrics(y: pd.DataFrame, yhat: pd.DataFrame) -> pd.DataFrame:
    error_metrics = dict()

    error_metrics["MAE"] = [round(mean_absolute_error(y, yhat), 2)]
    error_metrics["MSE"] = [round(mean_squared_error(y, yhat), 2)]
    error_metrics["RMSE"] = [round(mean_squared_error(y, yhat, squared=False), 2)]
    error_metrics["MAPE %"] = [round(mean_absolute_percentage_error(y, yhat) * 100, 2)]
    error_metrics["R2 %"] = [round(r2_score(y, yhat) * 100, 2)]
    return pd.DataFrame(error_metrics)
