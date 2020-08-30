# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 01:33:03 2020

@author: Eduardo Adachi
"""

import pandas as pd
import pandas_datareader.data as web
import datetime as dt
import matplotlib.pyplot as fig

url ="http://bvmf.bmfbovespa.com.br/indices/ResumoCarteiraTeorica.aspx?Indice=IBOV&idioma=pt-br"
df=pd.read_html(url,decimal=',',thousands='.', index_col='Código')[0][:-1]
print(df)
#======================================================
# ordena pela participacao em ordem descrescente
ibov=df.sort_values('Part. (%)',ascending=False)
print(ibov)
#======================================================
##### usar os dados do site para o datareader #########
inicio=dt.datetime(2019,1,1)
fim=dt.datetime(2020, 8, 28)
num=5 # -----> numero dos primeiros ativos com mais pesos
klist=[]
for i in range(num):
    x=ibov.index[i]+'.SA'
    klist.append(x)
    
for i in range(num):
        y=web.DataReader(klist[i],'yahoo',inicio,fim)
        if i ==0:
            ativo=pd.DataFrame(y['Close'].values)
            ativo=ativo.rename(columns={i:klist[i]})
        else:
            ativo[klist[i]]=pd.DataFrame(y['Close'].values)
ativo.index=y.index
print(ativo)
################################################################

fig.plot(ativo)
fig.legend(klist)
    