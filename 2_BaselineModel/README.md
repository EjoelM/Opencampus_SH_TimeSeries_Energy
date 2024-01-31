# Baseline Model

Seasonal ARIMA with Exogenous ( hourly `Air temperature`, `hour` of day, and if day of week `is_weekend` ) with prediction evaluation metrics of `len(test_set)`, `A week`, and `A day`. 

**A Week**

![image](https://github.com/EjoelM/Opencampus_SH_TimeSeries_Energy/assets/12827390/e3000407-76f1-4076-9a34-e0055d7cbe57)

**A day**

![image](https://github.com/EjoelM/Opencampus_SH_TimeSeries_Energy/assets/12827390/8f2d2e63-ffba-4c84-98cb-94ac025261e1)


**Evaluation**

| timeframe | MAE | MSE  | RMSE | MAPE % | R2 % |
|--| --    |    -- | -- | -- | -- |
|len(test_set)| 29082.02 | 1.262166e+09 | 35526.97 | 13.2  | 19.51 |
|A Week| 23709.73 | 8.466005e+08 | 29096.4 | 11.28 | 37.78 |
|A Day | 18270.07 | 5.842364e+08 | 24170.98 | 9.23 | 47.25 |  


**Possible Improvements**

- With `is_holiday` and events as exogenous
- Inclusion of other relevant external features

**[[Notebook @](baseline_model.ipynb)]**

