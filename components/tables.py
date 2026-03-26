import streamlit as st
import pandas as pd

def display_financials(df, title):
    st.subheader(title)
    st.dataframe(df.style.format("{:.2f}"))

def display_ratios(ratios, pe):
    st.subheader("Key Ratios")
    col1, col2 = st.columns(2)
    with col1:
        pe_display = f"{pe:.2f}" if pe else "N/A"
        st.metric('P/E ratio', pe_display)
        
        profit_margin = ratios.get('Profit Margin') or 0
        st.metric('Profit margin', f"{profit_margin:.2%}")
    with col2:
        roe = ratios.get('ROE') or 0
        st.metric("ROE", f"{roe:.2%}")
        
        debt_equity = ratios.get('Debt to Equity') or 0
        st.metric("Debt/Equity", f"{debt_equity:.2f}")


