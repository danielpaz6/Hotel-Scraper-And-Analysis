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
from sklearn.metrics import mean_squared_error


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

#predictions = list()

#df = pd.DataFrame({"val": pd.Series(fixedNan, index=series.index)})
#df_train = pd.DataFrame({"val": pd.Series(train, index=train_dates)})
#df_test = pd.DataFrame({"val": pd.Series(test, index=test_dates)})

minError = 999999
tmpn1 = -1
tmpn2 = -1
tmpn3 = -1

print("Running...")
for n1 in range (1, 5):
    for n2 in range(0, 5):
        for n3 in range(0, 3):
            if (n1,n2,n3) in [(1,0,0), (1,0,1), (1,0,2), (1,0,3), (1,0,4), (1,1,0), (1,1,1), (1,1,2), (1,2,0)]:
                continue;

            history = [x for x in train]
            predictions = list()
            for t in range(len(test)):
                tmpOrder = (n1,n2,n3)
                model = ARIMA(history, order=tmpOrder)

                try:
                    model_fit = model.fit(disp=0)
                except:
                    continue;

                output = model_fit.forecast()
                yhat = output[0]
                predictions.append(yhat)
                obs = test[t]
                history.append(obs)
                #print('predicted=%f, expected=%f' % (yhat, obs))

            error = mean_squared_error(test, predictions)

            if(error < minError):
                minError = error
                tmpn1 = n1
                tmpn2 = n2
                tmpn3 = n3

            print("-----------------------------")
            print('Test MSE: %.3f' % error)
            print('p =  ' + n1.__str__())
            print('d =  ' + n2.__str__())
            print('q =  ' + n3.__str__())
            print("-----------------------------")

            # plot
            #pyplot.plot(test)
            #pyplot.plot(predictions, color='red')
            #pyplot.show()


print("MinError: " + minError.__str__())
print("p: " + tmpn1.__str__())
print("d: " + tmpn2.__str__())
print("q: " + tmpn3.__str__())

print("Done!")