# Sales Forecasting Project

## Overview
This project forecasts future sales using historical time-series data from retail/e-commerce. It includes trends, seasonality (e.g., yearly patterns), and promotional effects. Models used: Prophet (primary) and ARIMA (comparison).

## Features
- Synthetic data generation with promotions.
- Data preprocessing and decomposition.
- Model training and evaluation (MAE, RMSE).
- Visualization of forecasts vs. actuals.
- 30-day future forecast.

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Generate data: `python data_generator.py`
3. Run the notebook: `jupyter notebook sales_forecasting.ipynb`

## Results
- Prophet typically outperforms ARIMA on seasonal data.
- Visualizations show forecast accuracy and components.

## Extensions
- Add LSTM for deep learning.
- Integrate real data (e.g., from Kaggle).
- Deploy as a web app with Streamlit.
