from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot
import time
from datetime import datetime
from time import gmtime, strftime
from selenium import webdriver
import csv
import re

hotelName = "Hotel Americano";
nights = 1;

csvFileName = hotelName.__str__() + '_' + nights.__str__() + '_nights.csv';
fieldnames = ['Check-In Date', 'Price']

i = 0
with open(csvFileName, mode='a', newline='') as employee_file:
    with open('booking_final.csv', 'r') as file1: # FILE2 (15-30]
        hotelCsv = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        fileLines = [line for line in csv.reader(file1, delimiter=',')]

        # rowsByDateFromFile1 = filter(lambda x: x[0] == currentDate, file1Lines);
        specificHotel = filter(lambda x: x[3] == hotelName, fileLines);

        # Only results with 1 nights
        specificHotel = filter(lambda x: (datetime.strptime(x[2], '%d-%m-%Y') - datetime.strptime(x[1], '%d-%m-%Y')).days == nights, specificHotel);


        for item in specificHotel:
            hotelCsv.writerow([
                item[1],
                item[4]
                #item[1],
                #item[2]
            ]);

            i += 1;


print("done");
