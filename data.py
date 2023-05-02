import requests

def get_historical_prices(symbol, start_date, end_date):
    """
    Retrieve historical price data for a given symbol and date range.
    """
    url = f'https://api.binance.com/api/v3/klines?symbol={symbol}&interval=1d&startTime={start_date}&endTime={end_date}'
    response = requests.get(url)
    
    data = response.json()
    
    prices = []
    for item in data:
        price = {
            'date': item[0],
            'open': float(item[1]),
            'high': float(item[2]),
            'low': float(item[3]),
            'close': float(item[4]),
            'volume': float(item[5])
        }
        prices.append(price)
    
    return prices
