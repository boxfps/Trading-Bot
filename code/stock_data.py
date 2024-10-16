# This file will collect and handle stock data based on the provided list

from stock_list import tsx_stocks # Import the predefined stock list
import yfinance as yf   # Import the yahoo finance API in order to get stock info

def get_stock_data(ticker, period='1y'):
    # Fetch stock data for each ticker
    stock = yf.Ticker(ticker)
    return stock.history(period = period)

def get_all_stock_data(stock_list, period = '1y'):
    stock_data = {}
    for stock in stock_list:
        try:
            print (f"Fetching data for {stock}...")
            data = get_stock_data(stock, period)
            stock_data[stock] = data
        except Exception as e:
            print (f"Error fetching data for {stock}: {e}")

    return stock_data