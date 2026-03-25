import pandas as pd
import streamlit as st

from scripts.yf_fetcher import get_current_price, get_financials, get_info, get_stock_data
from scripts.news_fetcher import get_news
from scripts.ratios import calculate_ratios, get_pe_ratio
from scripts.technicals import compute_macd, compute_moving_averages, compute_rsi
from components.charts import plot_price_chart, plot_candlesticks, plot_technicals

st.set_page_config(page_title="Equity Dashboard", layout='centered')
st.title("Equity Dash", )

#sidebar 
st.sidebar.header("Stock selection")
symbol_in = st.sidebar.text_input("Symbol: ").upper().strip()
if symbol_in:
    symbol = f"{symbol_in}.NS"
else:
    st.warning("symbol missing")
    st.stop()

#fetching
try: 
    df = get_stock_data(symbol)
    cmp = get_current_price(symbol)
    info = get_info(symbol)
    income_Stmt, balance_sheet, cashflow = get_financials(symbol)
    news = get_news(symbol)
except Exception as e:
    st.error(f"Error occured while fetching data")
    st.stop()

#header with cmp
st.header(f"{symbol_in} - Current Market Price {cmp:.2f}" if cmp else symbol_in)

#tabs
tab1, tab2, tab3, tab4 = st.tabs(["Chart", "Fundamentals", "Ratios", "News"])

#tab1 - charts
with tab1:
    st.subheader("Price chart")
    period = st.selectbox("Duration", ["1d", "1m", "3m", "6m", "1y", "2y", "5y"], index = 4)
    df_period = get_stock_data(symbol, period=period)
    fig = plot_price_chart(df_period, f"{symbol_in} Price ({period})")
    st.plotly_chart(fig, use_container_width=True)

