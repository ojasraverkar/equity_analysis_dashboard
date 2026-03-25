import yfinance as yf

def get_info(symbol):
    stock = yf.Ticker(symbol)
    return stock.info

def get_stock_data(symbol, period = "1y"):
    stock = yf.Ticker(symbol)
    hist = stock.history(period = period)
    return hist

def get_current_price(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period = "1d")
    return data['Close'].iloc[-1]

def get_financials(symbol):
    stock = yf.Ticker(symbol)
    income = stock.income_stmt
    balance = stock.balance_sheet
    cashflow = stock.cashflow
    return income, balance, cashflow


