# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 13:34:48 2020

@author: Eduardo Adachi
"""

import matplotlib.pyplot as fig
import datetime as dt
import pandas_datareader.data as web

inicio=dt.datetime(1970,1,1)
fim=dt.datetime(2019,11,24)
df1=web.DataReader('DGS10','fred',inicio,fim)
df1['med_mov']=df1['DGS10'].rolling(window=500,min_periods=0).mean()

ax=fig.subplot(111)
ax.plot(df1.index,df1['DGS10'],color='black',alpha=0.5)
ax.plot(df1.index,df1['med_mov'],color='black')
ax.set_title('Tesouro EUA - venc. 10 (10-year Treasury)',fontsize=18,weight='bold')

