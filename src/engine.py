import numpy as np

def calculate_volatility(price_series):
   
    # 1. Calculate how much the price changed every day
    returns = np.log(price_series / price_series.shift(1))
    
    # 2. Calculate Volatility (The 'Wiggle' score)
    # 252 is the number of trading days in a year
    volatility = returns.rolling(window=21).std() * np.sqrt(252)
    
    return volatility.dropna()