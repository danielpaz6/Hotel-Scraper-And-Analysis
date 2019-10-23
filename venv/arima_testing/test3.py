from pandas import read_csv
from pandas import datetime
import pandas as pd
from matplotlib import pyplot
import time
from datetime import datetime
from time import gmtime, strftime
from selenium import webdriver
import csv
import re
from statsmodels.tsa.arima_model import ARIMA
import statsmodels.api as sm
import numpy as np
from pandas import DataFrame


def parser(x):
	return datetime.strptime(x, '%d-%m-%Y')
	#return datetime.strptime('', '%Y-%m')

#headers = ['Query Date','Check-In Date','Check-Out Date','Hotel Name','Price($)','Rating','Number of Reviews'];
series = read_csv('hotels_output/Hotel Pennsylvania_1_nights.csv', header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)

#series = list(series)
#print(series);
#tmp = [row[0] for row in series]

#series.index = pd.DatetimeIndex(series.index.values, freq = series.index.inferred_freq)
series.index = pd.DatetimeIndex(series.index).to_period('D')

#print(series[1])
#df = pd.DataFrame({"val": pd.Series([1.1,1.7,8.4 ], index=['2015-01-15 12:10:23','2015-02-15 12:10:23','2015-03-15 12:10:23'])})

# Some values may be Nulls, this step will conver them to 0,
# More information can be found here: https://stackoverflow.com/questions/33447808/sklearns-plsregression-valueerror-array-must-not-contain-infs-or-nans
fixedNan = np.nan_to_num(series.values)

df = pd.DataFrame({"val": pd.Series(fixedNan, index=series.index)})



#print(np.isnan(series.values).any())
#print(np.isnan(series.index).any())


#Info
model = ARIMA(df, order=(5,1,0))
model_fit = model.fit(disp = 0);
print(model_fit.summary())

#Plot

# plot residual errors
residuals = DataFrame(model_fit.resid)
residuals.plot()
pyplot.show()
residuals.plot(kind='kde')
pyplot.show()
print(residuals.describe())


#model_fit = model.fit(disp = 0)
#print(model_fit.summary())

'''model = ARIMA(series, order=(5,1,0))
model_fit = model.fit(disp = 0)
print(model_fit.summary())'''

'''print(series.head())
series.plot()
pyplot.show()'''

'''fit1 = sm.tsa.statespace.SARIMAX(series, order=(1, 0, 0),
                            enforce_stationarity=False,
                            enforce_invertibility=False).fit()'''