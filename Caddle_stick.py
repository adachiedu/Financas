# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 01:33:03 2020

@author: Eduardo Adachi
"""

import matplotlib.pyplot as fig
import datetime as dt
import mpl_finance as mpf
import matplotlib.dates as mdates
import pandas_datareader.data as web

# 1 Amostrar os dados do site ######################
inicio=dt.datetime(2019,1,1)
fim=dt.datetime(2020,8,28)
df=web.DataReader('ITUB4.SA','yahoo',inicio,fim)
####################################################
df['med_mov']=df['Close'].rolling(window=20,min_periods=0).mean()
df_ohlc=df['Close'].resample('7D').ohlc()
df_ohlc['Volume']=df['Volume'].resample('7D').sum()

df_ohlc.reset_index(inplace=True)
df_ohlc['Date']=df_ohlc['Date'].map(mdates.date2num)

ax1=fig.subplot(311)
ax1.xaxis_date()
mpf.candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')
ax1.plot(df.index, df['med_mov'])

#####################################################
ax2=fig.subplot(312)
ax2.xaxis_date()
ax2.bar(df_ohlc['Date'],df_ohlc['Volume'],color='blue')

#####################################################
ax3=fig.subplot(313)
ax3.xaxis_date()
df['ret']=df['Close'].pct_change()
ax3.plot(df.index,df['ret'],color='red')
