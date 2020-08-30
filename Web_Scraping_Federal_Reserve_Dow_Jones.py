# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 13:49:16 2020

@author: Eduardo Adachi
"""

import matplotlib.pyplot as fig
import datetime as dt
import pandas_datareader.data as web

inicio=dt.datetime(1970,1,1)
fim=dt.datetime(2019,11,24)
df1=web.DataReader('DGS10','fred',inicio,fim)
df2=web.DataReader('^DJI','yahoo',inicio,fim)
df1['med_mov']=df1['DGS10'].rolling(window=500,min_periods=0).mean()

ax=fig.subplot(111)
ax.plot(df1.index,df1['DGS10'],color='black',alpha=0.5)
ax.plot(df1.index,df1['med_mov'],color='black')
ax.set_title('Tesouro EUA - venc. 10 (10-year Treasury)',fontsize=18,weight='bold')
ax.text(x=df1.index[1000],y=14,s='Título de 10 anos',fontsize=14,weight='bold')

ax2=ax.twinx()
ax2.plot(df2.index,df2['Close'],color='black')
ax2.set_ylabel('DOW JONES',fontsize=18,weight='bold')
ax2.text(x=df1.index[11000],s='DOW JONES',fontsize=14,weight='bold')
fig.grid()