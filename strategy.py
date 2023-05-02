import pandas as pd

def simple_moving_average(dataframe, window):
    """
    Calculate the Simple Moving Average (SMA) over a given window.
    """
    return dataframe['close'].rolling(window=window).mean()

def generate_signals(dataframe):
    """
    Generate trading signals based on a Simple Moving Average (SMA) crossover strategy.
    """
    # Calculate the 50-day and 200-day Simple Moving Average (SMA)
    sma_50 = simple_moving_average(dataframe, 50)
    sma_200 = simple_moving_average(dataframe, 200)
    
    # Generate buy and sell signals
    buy_signal = (sma_50 > sma_200) & (sma_50.shift(1) <= sma_200.shift(1))
    sell_signal = (sma_50 < sma_200) & (sma_50.shift(1) >= sma_200.shift(1))
    
    # Combine signals into a single dataframe
    signals = pd.DataFrame({'buy': buy_signal, 'sell': sell_signal})
    
    return signals
