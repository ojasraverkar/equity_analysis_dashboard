import pandas as pd
import streamlit as st

from scripts.yf_fetcher import get_current_price, get_financials, get_info, get_stock_data
from scripts.news_fetcher import get_news
from scripts.ratios import calculate_ratios, get_pe_ratio
from scripts.technicals import compute_macd, compute_moving_averages, compute_rsi
from components.charts import plot_price_chart, plot_candlesticks, plot_technicals, plot_multiline
from components.tables import display_financials, display_ratios

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
symbol = f"{symbol_in}.NS"
try: 
    df = get_stock_data(symbol)
    cmp = get_current_price(symbol)
    info = get_info(symbol)
    income_stmt, balance_sheet, cashflow = get_financials(symbol)
    news = get_news(symbol)
except Exception as e:
    st.error(f"Error occured while fetching data")
    st.stop()

#header with cmp
cmp = get_current_price(symbol)
st.header(f"{symbol_in} - Current Market Price {cmp:.2f}" if cmp else symbol_in)

#tabs
tab1, tab2, tab3, tab4 = st.tabs(["Chart", "Fundamentals", "Ratios", "News"])

#tab1 - charts
with tab1:
    st.subheader("Price chart")
    period = st.selectbox("Duration", ["1mo", "3mo", "6mo", "1y", "2y", "5y"], index = 4)
    df_period = get_stock_data(symbol, period=period)
    fig = plot_price_chart(df_period, f"{symbol_in} Price ({period})")
    st.plotly_chart(fig, use_container_width=True)

#tab2 - fundamentals
with tab2:
    st.subheader("Income Statement")
    display_financials(income_stmt, "Income Statement")
    st.subheader("Balance Sheet")
    display_financials(balance_sheet, "Balance Sheet")
    st.subheader("Cash Flow statement")
    display_financials(cashflow, "Cash Flow")

#tab3 - ratios & technical
with tab3:

    #ratios
    ratios = calculate_ratios(income_stmt, balance_sheet)
    pe = get_pe_ratio(info)
    display_ratios(ratios, pe)

    #technicals
    st.subheader("Technical Indicators")
    tech_period = st.selectbox('Duration:', ["1mo", "3mo", "6mo", "1y", "2y", "5y"], index=3)
    df_technical = get_stock_data(symbol, period=tech_period)
    if df_technical.empty or len(df_technical) < 26:
        st.warning("Not enough data for technical indicators (need at least 26 days).")
    else:
        df_technical['RSI'] = compute_rsi(df_technical['Close'])
        df_technical = compute_moving_averages(df_technical)
        df_technical = compute_macd(df_technical)
        latest_rsi = df_technical['RSI'].iloc[-1]
        st.metric("RSI(14) ", f"{latest_rsi:.2f}")

        fig_tech = plot_technicals(df_technical, f"{symbol_in}")
        st.plotly_chart(fig_tech, use_container_width=True)

        st.subheader("MACD")
        fig_macd = plot_multiline(df_technical[['MACD', 'Signal']].dropna(), "MACD and Signal", ['MACD', 'Signal'])
        st.plotly_chart(fig_macd, use_container_width=True)

with tab4:
    st.subheader("News")
    for article in news:
        st.markdown(f"**{article['title']}** \n{article['published']} \n[read more]({article['link']})")
        st.markdown("---")
    


    
