import pandas as pd

def moving_average(dataframe, window):
    """
    Calculate the Moving Average (MA) over a given window.
    """
    return dataframe['close'].rolling(window=window).mean()

def relative_strength_index(dataframe, window):
    """
    Calculate the Relative Strength Index (RSI) over a given window.
    """
    diff = dataframe['close'].diff(1)
    
    up_gain = diff.where(diff > 0, 0)
    down_loss = -diff.where(diff < 0, 0)
    
    up_gain_avg = up_gain.rolling(window=window).mean()
    down_loss_avg = down_loss.rolling(window=window).mean()
    
    rs = up_gain_avg / down_loss_avg
    rsi = 100 - (100 / (1 + rs))
    
    return rsi
