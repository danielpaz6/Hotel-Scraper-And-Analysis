from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot
import time
from datetime import datetime
from time import gmtime, strftime
from selenium import webdriver
import csv
import re
from statsmodels.tsa.arima_model import ARIMA


def parser(x):
	return datetime.strptime(x, '%d-%m-%Y')
	#return datetime.strptime('', '%Y-%m')

#headers = ['Query Date','Check-In Date','Check-Out Date','Hotel Name','Price($)','Rating','Number of Reviews'];
series = read_csv('Hotel Americano_1_nights.csv', header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)

model = ARIMA(series, order=(5,1,0))
model_fit = model.fit(disp = 0)
print(model_fit.summary())

'''print(series.head())
series.plot()
pyplot.show()'''
