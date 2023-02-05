#!/usr/bin/env python
# coding: utf-8

# In[1]:


import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
#simple Stock Price App
Shown are the stock closing price and volume in Google""")

tickerSymbol='GOOGL'

tickerData=yf.Ticker(tickerSymbol)

tickerDF=tickerData.history(period='id',start='2010-5-31')

st.line_chart(tickerDF.Close)
st.line_chart(tickerDF.Volume)


# In[ ]:




