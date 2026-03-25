import streamlit as st
import pandas as pd

def display_financials(df, title):
    st.subheader(title)
    st.dataframe(df.style.format("{:.2f}"))

def display_ratios(ratios, pe):
    st.subheader("Key Ratios")
    col1, col2 = st.columns(2)
    with col1:
        st.metric('P/E ratio', f"{pe:.2f}")
        st.metric('Profit margin', f"{ratios.get('Profit Margin', 0):.2%}")
    with col2:
        st.metric("ROE", f"{ratios.get('ROE', 0):.2%}")
        st.metric("Debt/Equity", f"{ratios.get('Debt to Equity', 0):.2f}")


