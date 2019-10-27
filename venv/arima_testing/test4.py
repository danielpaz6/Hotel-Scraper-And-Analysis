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
series.index = pd.DatetimeIndex(series.index).to_period('D')
fixedNan = np.nan_to_num(series.values)

X = fixedNan
size = int(len(X) * 0.66)
train, test = X[0:size], X[size:len(X)]
#train_dates, test_dates = series.index[0: size], series.index[size:len(X)]

history = [x for x in train]
predictions = list()

#df = pd.DataFrame({"val": pd.Series(fixedNan, index=series.index)})
#df_train = pd.DataFrame({"val": pd.Series(train, index=train_dates)})
#df_test = pd.DataFrame({"val": pd.Series(test, index=test_dates)})


for t in range(len(test)):
	model = ARIMA(history, order=(5,1,0))
	model_fit = model.fit(disp=0)
	output = model_fit.forecast()
	yhat = output[0]
	predictions.append(yhat)
	obs = test[t]
	history.append(obs)
	print('predicted=%f, expected=%f' % (yhat, obs))

error = mean_squared_error(test, predictions)
print('Test MSE: %.3f' % error)
# plot
pyplot.plot(test)
pyplot.plot(predictions, color='red')
pyplot.show()


print("Done!")