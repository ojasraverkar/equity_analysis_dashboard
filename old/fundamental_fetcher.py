import os

import requests
import yfinance as yf

import feedparser

stock = yf.Ticker('RELIANCE.NS')
#print(stock.financials)
#print(stock.balance_sheet)
#print(stock.cashflow)
#print(stock.actions)           #dividends and stocksplits
#print(stock.analyst_price_targets)
#print(stock.earnings_estimate)
#print(stock.eps_trend)

url = "https://news.google.com/rss/search?q=Reliance+Industries"
feed = feedparser.parse(url)

for entry in feed.entries[:5]:
    print(entry.title, entry.link)

response = requests.get(url)
print(response.status_code)
print(response.text)

