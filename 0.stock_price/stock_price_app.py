# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75

import pandas as pd
import yfinance as yf
import streamlit as st


st.write("""
## Basic Web App for Stock Price Visualization

Below are shown both stock **Closing price** and **Volume** of _IBM_!

""")

# define the ticker symbol
tickerSymbol = 'IBM'

# get data for this ticker
tickerData = yf.Ticker(tickerSymbol)

# pass the arguments to get historical prices for the ticker
tickerDf = tickerData.history(period = '1d',
                              start = '2020-4-30',
                              end = '2021-4-30')

# Write the arguments for closing and volume price
st.write("""
## Closing Price (USD)
""")
st.line_chart(tickerDf.Close,
              color = "#ffaa00") 

st.write("""
## Volume Price (USD)
""")
st.line_chart(tickerDf.Volume,
              color = "#ffaa00")

