# low-carbon-london-energy-forecasting
Energy Forecasting Using the Low Carbon London Smart Meter Dataset: A Comparative Study of Preprocessing Techniques and Machine Learning Models

# Low Carbon London Energy Forecasting

## Overview

This project explores how different preprocessing techniques and machine learning models affect the accuracy of energy consumption forecasts using the Low Carbon London Smart Meter dataset. We compare three specific models—Prophet, SARIMA, and LSTM—to determine the best approach for accurate energy forecasting.

## Table of Contents

- [Introduction]
- [Dataset]
- [Preprocessing Techniques]
- [Machine Learning Models]
- [Evaluation]
- [Results and Analysis]
- [Conclusion]
- [Usage]
- [License]
- [Acknowledgements]

## Introduction

Accurate energy forecasting is crucial for efficient energy management, cost reduction, and environmental sustainability. This project aims to evaluate the impact of various preprocessing methods and machine learning models on forecasting accuracy.

## Dataset

The Low Carbon London dataset contains detailed energy consumption data from smart meters across London. Key features include:
- **Timestamp**: Date and time of the reading
- **Energy Usage (kWh)**: Amount of electricity consumed
- **Household Information**: Metadata about the households (if available)
- **Weather Data**: Temperature and other weather conditions (if included)

## Preprocessing Techniques

We explore three preprocessing approaches:
1. **Simple Imputation and Resampling**
2. **Advanced Interpolation**
3. **Feature Engineering**

## Machine Learning Models

Three models are implemented and evaluated:
1. **Prophet**
2. **SARIMA (Seasonal ARIMA)**
3. **LSTM (Long Short-Term Memory) Networks**

## Evaluation

Models are evaluated using:
- **Mean Squared Error (MSE)**
- **Mean Absolute Error (MAE)**

## Results and Analysis

A detailed comparison of model performance across different preprocessing techniques is provided. The results highlight the best combination of preprocessing approach and machine learning model for accurate energy forecasting.

## Conclusion

This project identifies the most effective methods for preprocessing and forecasting energy consumption using the Low Carbon London dataset, contributing to better energy management and sustainability efforts.

## Usage

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/low-carbon-london-energy-forecasting.git
   cd low-carbon-london-energy-forecasting

##Acknowledgements
The Low Carbon London dataset is provided by the London Datastore.
We acknowledge the use of Prophet, SARIMA, and LSTM libraries for model development
