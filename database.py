import psycopg2

def save_trade(trade):
    """
    Save a trade to the database.
    """
    conn = psycopg2.connect('postgresql://user:password@localhost/trading_bot')
    cur = conn.cursor()
    
    cur.execute('INSERT INTO trades (symbol, side, price, quantity, time) VALUES (%s, %s, %s, %s, %s)', (trade['symbol'], trade['side
