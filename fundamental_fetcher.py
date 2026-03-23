import os
from dotenv import load_dotenv

import requests
import yfinance as yf

load_dotenv()

stock = yf.Ticker('RELIANCE.NS')
#print(stock.financials)
#print(stock.balance_sheet)
#print(stock.cashflow)
#print(stock.actions)           #dividends and stocksplits
#print(stock.analyst_price_targets)
#print(stock.earnings_estimate)
#print(stock.eps_trend)

apikey = os.getenv("FMP_API_KEY")

#to search for symbols 
#url = f"https://financialmodelingprep.com/stable/search-name?query=reliance&apikey={apikey}"

#This API provides key financial and operational information for a specific stock symbol, including the company's market capitalization, stock price, industry, and much more.
#url = f"https://financialmodelingprep.com/stable/profile?symbol=RELIANCE.NS&apikey={apikey}"

#Identify and compare companies within the same sector and market capitalization range
#url = f"https://financialmodelingprep.com/stable/stock-peers?symbol=RELIANCE.NS&apikey={apikey}"

#market cap
url = f"https://financialmodelingprep.com/stable/market-capitalization?symbol=RELIANCE.NS&apikey={apikey}"


respose = requests.get(url)
data = respose.json()
print(data)

