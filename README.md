London Low Carbon Energy Forecasting
This project aims to forecast daily low-carbon energy consumption in London using various machine learning models, including Random Forest, SARIMA, and LSTM. Accurate forecasting of energy demand is essential for better grid management and supporting the transition towards sustainable energy practices.

Table of Contents
Project Overview
Dataset
Technologies Used
Modeling Approach
Results
Installation
Usage
Contributing
License
Project Overview
The main objective of this project is to predict the daily energy consumption in London to help manage the energy grid's demand and supply more efficiently. We apply machine learning models that take into account both historical energy usage data and external factors like time-based variables and weather influences.

Three models are implemented and compared:

Random Forest Regressor
SARIMA (Seasonal Autoregressive Integrated Moving Average)
LSTM (Long Short-Term Memory) Neural Network
Dataset
The dataset used in this project contains historical energy consumption data from the London Low Carbon Energy initiative. The main feature is the energy consumption recorded in kilowatt-hours (kWh) per half-hour intervals.

The dataset was resampled to daily frequencies for this analysis. The key features of the data include:

KWH/hh (per half hour): The target variable representing energy consumption.
Time-based features: Day of the Week, Month, and lagged consumption values.
Technologies Used
Python: Core language for data analysis and model development.
Jupyter Notebook: For interactive coding and visualization.
Pandas & NumPy: For data manipulation and numerical computations.
Scikit-learn: For implementing traditional machine learning models (Random Forest).
TensorFlow/Keras: For implementing LSTM neural networks.
Statsmodels & pmdarima: For time series modeling using SARIMA.
Matplotlib & Seaborn: For data visualization and plotting model results.
Modeling Approach
Three different approaches are used to forecast daily energy consumption:

1. Random Forest Regressor
A Random Forest model is trained using lagged values, rolling averages, and time-based features to predict daily energy consumption. It captures non-linear relationships in the data.

2. SARIMA (Seasonal ARIMA)
The SARIMA model, optimized using auto_arima, is used for time series forecasting. It captures seasonality and temporal patterns in the data to make predictions.

3. LSTM (Long Short-Term Memory)
An LSTM neural network is used to capture long-term dependencies in the time series data. The data is scaled and reshaped into sequences before being fed into the model for training.

Results
Evaluation Metrics
The models were evaluated using Mean Squared Error (MSE) and Mean Absolute Error (MAE). The results are as follows:

Random Forest:

MSE: 61.34
MAE: 5.76
SARIMA:

MSE: 93,187.70
MAE: 291.14
LSTM:

MSE: 1,037.29
MAE: 23.22
Insights:
Random Forest performed significantly better than SARIMA and LSTM, with much lower MSE and MAE values.
SARIMA struggled to capture the variability in the data, possibly due to complexity in seasonal patterns.
LSTM, while not outperforming Random Forest, captured long-term dependencies and seasonal patterns better than SARIMA.
Visual Results:
Several plots are generated to compare the predictions of each model against the actual data. Below is an overview:

Random Forest closely follows the actual data trend with the smallest error margins.
SARIMA shows significant deviations due to its inability to fully capture the complexity of the energy consumption patterns.
LSTM, though better than SARIMA, has higher prediction errors compared to Random Forest.
Installation
To run this project locally, follow these steps:

Clone the repository:
bash
Copy code
git clone https://github.com/Nikhilsxni/low-carbon-london-energy-forecasting.git
Navigate to the project directory:
bash
Copy code
cd low-carbon-london-energy-forecasting
Install the required Python libraries:
bash
Copy code
pip install -r requirements.txt
Usage
To run the forecasting models and visualize the results:

Open the main.ipynb Jupyter notebook.
Execute the cells sequentially to load the data, preprocess it, train the models, and evaluate their performance.
Modify the notebook to experiment with different models, hyperparameters, or datasets if needed.
Contributing
Contributions are welcome! If you would like to contribute to this project, please fork the repository, create a feature branch, and submit a pull request with your enhancements.

License
This project is licensed under the MIT License. See the LICENSE file for more details