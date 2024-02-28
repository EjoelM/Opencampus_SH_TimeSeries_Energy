# Literature Review

Approaches or solutions that have been tried before on similar projects.

**Summary of Each Work**:

- **Source 1**: Short-term office building elevator energy consumption forecast using SARIMA (Bláquez-García et al., 2019)

  - **[Link](https://www.tandfonline.com/doi/full/10.1080/19401493.2019.1698657)**
  - **Objective**:Forecast of energy consumption of a green-elevator
  - **Methods**: Use of three variations of SARIMA model (daily, hourly and 15-min data)  
  - **Outcomes**: The model with the highest accruacy (measured mainly with the MAPE indicator) was the SARIMA model using hourly data. 
  - **Relation to the Project**: Energy consumption is the main focus of our project. Furthermore, we wanted evaluate which SARIMA model could be the "best" baseline model. Other literatures also indicate that the 1h SARIMA model is the most used SARIMA model when it comes to forecasting energy consumption. 

- **Source 2**: A hybrid forecasting model using LSTM and Prophet for energy consumption with decomposition of time series data (Arslan, 2022)

  - **[Link](https://peerj.com/articles/cs-1001/)**
  - **Objective**: Proposition of an efficient forecasting framework for energy consumption using both the Prohet and LSTM model
  - **Methods**: Use of the Prophet and LSTM model to create an hybrid form of the two model. The hybrid form is challanged against other models on several countries.
  - **Outcomes**: The hybrid model exhibits mitigated results: it outperforms other models for some countries. For other countries, it shows "competitive" performance, i.e. it ranks among the best performing models
  - **Relation to the Project**: We are using both the Prophet and the LSTM model to test against the baseline model. We wanted to know whether a hybrid model could provide competitive advantage. Since the results were mitigated, we decided to remain with the "pure" form of the models.

- **Source 3**: Multivariate time series prediction by RNN architectures for energy consumption forecasting (Amalou et al., 2022)

  - **[Link](https://www.sciencedirect.com/science/article/pii/S2352484722013932?via%3Dihub)**
  - **Objective**: Comparative analysis of some deep learning models for the forecast of energy consumption
  - **Methods**: The models of interest used were the Recurrent Neural Network (RNN), the Long Short-term Memory (LSTM) and the Gated Recurrent Unit (GTU) models.
  - **Outcomes**: In terms of accuracy (several indicators were considered such as RMSE, MAE, R^2 etc.), the GRU outperformed the other two models. The RNN model exhibits the most "modest" results. 
  - **Relation to the Project**: It firstly shows that deep learning models are more and more common in forecasting energy consumption. Secondly, we wanted to learn more about how such models can be used in forecasting energy consumption.
 
  - **Source 4**: Predicting Energy Consumption Using LSTM, Multi-Layer GRU and Drop-GRU Neural Networks (Mahjoub et al., 2022)
 
  - **[Link](https://www.mdpi.com/1424-8220/22/11/4062)
  - **Objective**: Predicting energy consumption using a number of Neural Network models (NNM)
  - **Methods**: Three NNMs were used: LSTM, Multi-layer GRU and Drop-GRU.
  - **Outcomes**: In the setting used in this paper (i.e. power consumption in some French cities), the LSTM outperformed the other two models. 
  - **Relation to the Project**: This outcomes is not in line with Amalou et al. (2022) which shows that the research in power conumption prediction using NNM is still under development and that the context matters.
