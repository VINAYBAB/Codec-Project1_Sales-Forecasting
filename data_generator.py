import pandas as pd
import numpy as np
import os

# Create data directory if it doesn't exist
os.makedirs('data', exist_ok=True)

# Generate synthetic data
np.random.seed(42)  # For reproducibility
dates = pd.date_range(start='2020-01-01', end='2023-12-31', freq='D')
n_days = len(dates)

# Base sales with trend (increasing over time)
trend = np.linspace(100, 200, n_days)

# Seasonal component (yearly, e.g., higher in Q4 for holidays)
seasonal = 50 * np.sin(2 * np.pi * dates.dayofyear / 365)

# Promotional effects (random binary: 1 if promotion, boosts sales by 20%)
promotions = np.random.choice([0, 1], n_days, p=[0.85, 0.15])
promo_effect = promotions * 20

# Noise and overall sales
noise = np.random.normal(0, 10, n_days)
sales = trend + seasonal + promo_effect + noise

# Create DataFrame
df = pd.DataFrame({
    'date': dates,
    'sales': sales.astype(int),
    'promotions': promotions
})

# Save to CSV
df.to_csv('data/sales_data.csv', index=False)
print("Synthetic sales data generated and saved to data/sales_data.csv")
