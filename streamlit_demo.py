import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
         # STONKS
         ## SICK
         """)

tickerSymbol = 'SGML'

tickerData = yf.Ticker(tickerSymbol)

tickerDF = tickerData.history(start='2010-5-31', end='2020-5-31')

st.line_chart(tickerDF.Close)
st.line_chart(tickerDF.Volume)