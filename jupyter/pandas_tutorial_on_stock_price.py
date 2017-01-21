# Pandas Tutorial On Stock Price Analysis

# This tutorial will cover how to retrieve stock price from google finance using pandas data reader. The analysis of stock is done by plotting its high, low, close, volumne values in table and a chart. Charts are of two types,
# 
# 1. Line Chart
# 2. Bar Chart
# 
# If you don't know what is stock then first **watch this video to gain understanding on fundamentals of stocks and investing**,
# https://www.youtube.com/embed/XRO6lEu9-5w

import pandas.io.data as web
df = web.DataReader('AAPL', 'google', '2016/1/1', '2017/1/1')
df.head()
df.plot(y='Close', color="Green")
df.plot.bar(y='Volume')

