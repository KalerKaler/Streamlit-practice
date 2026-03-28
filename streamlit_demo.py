import yfinance as yf
import streamlit as st
from datetime import datetime, date

st.title("Stock Value and Volume Visualizer")

tickerSymbol = st.text_input("Enter the stock code (Like AAPL)", "SGML")

tickerData = yf.Ticker(tickerSymbol)

start_date = st.date_input("Enter the start date for the chart",datetime(2000,1,1), datetime(1990,1,1),date.today())
end_date = st.date_input("Enter the end date for the chart",date.today(), datetime(1990,1,1),date.today())

tickerDF = tickerData.history(start=start_date, end='2020-5-31')

st.line_chart(tickerDF.Close)
st.line_chart(tickerDF.Volume)