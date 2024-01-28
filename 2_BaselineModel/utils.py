import math
import itertools
from typing import Union

import pandas as pd
import statsmodels.api as sm


def search_optimal_params(param_combinations: list, train_set: pd.DataFrame) -> tuple:
    """
    Search for the optimal parameters to minimize AIC in SARIMA model.
    Parameters:
        param_combinations: List of parameter combinations to try
        train_set: Training set
    Returns:
        Tuple of best AIC and the corresponding best parameters
    """
    best_aic = float("inf")
    best_params = None

    for params in param_combinations:
        order = params[:3]
        seasonal_order = params[3:]
        endog=train_set["Load"]
        exog=train_set[['hour', 'day_of_week', 'day', 'month', 'day_of_year', 'is_weekend']]

        try:
            model = sm.tsa.SARIMAX(endog=endog, exog=exog, order=order, seasonal_order=seasonal_order)
            result = model.fit(disp=False)
            aic = result.aic
            if not math.isinf(result.zvalues.mean()):
                print("order: {}, seasonal_order: {}, AIC: {}".format(order, seasonal_order, aic))
                if aic < best_aic:
                    best_aic = aic
                    best_params = params
            else:
                print(order, seasonal_order, 'not converged')
        except:
            continue

    return (best_aic, best_params)