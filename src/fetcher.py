import yfinance as yf # A tool to talk to the market
import pandas as pd

def get_exchange_data(ticker="USDINR=X"):
   
    data = yf.download(ticker, period="1y", interval="1d")
    return data['Close'].squeeze() # We only care about the price at the end of the day
