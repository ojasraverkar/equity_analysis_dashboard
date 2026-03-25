import numpy as np
import pandas as pd

def compute_rsi(series, period = 14):
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window = period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window = period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def compute_moving_averages(df, windows = [50, 200]):
    for w in windows:
        df[f"SMA_{w}"] = df['Close'].rolling(window = w).mean()
    return df

def compute_macd(df, fast = 12, slow = 26, signal = 9):
    e1 = df['Close'].ewm(span = fast, adjust = False).mean()
    e2 = df['Close'].ewm(span = fast, adjust = False).mean()
    df['MACD'] = e1 - e2
    df['Signal'] = df['MACD'].ewm(span = signal, adjust = False).mean()
    return df

