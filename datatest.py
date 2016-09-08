#! /usr/bin/env python
#coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.tsa.stattools import adfuller as ADF
from statsmodels.stats.diagnostic import acorr_ljungbox
from statsmodels.tsa.arima_model import ARIMA

def datatest(dftimeseries):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    #数据检测
    #plot_acf(dftimeseries).show()                       #原始自相关图
    #plot_pacf(dftimeseries).show()                      #原始偏自相关图
    #print(u'adf test result:', ADF(dftimeseries[u'timeseries']))    #原始数据adf值
    timeseries = dftimeseries.diff().dropna()
    timeseries.columns = [u'timeseries']
    timeseries.plot() 
    plt.show()                                   #差分数据图
    plot_acf(timeseries,lags=40)
    plt.show()                       #差分自相关图
    plot_pacf(timeseries,lags=40)
    plt.show()                      #差分偏自相关图
    print(u'diff adf test result:',ADF(timeseries[u'timeseries']))     #差分数据adf值
    print(u'Ljung-Box test result:',acorr_ljungbox(timeseries, lags=1))    #差分序列的白噪声检验结果
