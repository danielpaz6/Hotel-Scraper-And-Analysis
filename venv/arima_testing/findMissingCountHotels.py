from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot
import time
from datetime import datetime
from time import gmtime, strftime
from selenium import webdriver
import csv
import re
from operator import itemgetter

def sorting(L):
    splitup = L.split('-')
    return int(splitup[2]), int(splitup[1]), int(splitup[0])


# Top rated hotels ( excluding "Hotel Americano" )
hotelList = ["Hotel Americano", "Hotel Pennsylvania", "Pod Times Square", "The Watson Hotel", "Hotel Edison Times Square", "Martinique New York on Broadway, Curio Collection by Hilton", "Pod 39"]

for hotelName in hotelList:
    #hotelName = "Hotel Americano";
    nights = 1;

    csvFileName = hotelName.__str__() + '_' + nights.__str__() + '_nights.csv';
    fieldnames = ['Check-In Date', 'Price']

    rowsCount = 0
    with open("hotels_output/" + csvFileName, mode='w', newline='') as employee_file:
        with open('booking_final.csv', 'r') as file1: # FILE2 (15-30]
            hotelCsv = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            fileLines = [line for line in csv.reader(file1, delimiter=',')]

            # rowsByDateFromFile1 = filter(lambda x: x[0] == currentDate, file1Lines);
            specificHotel = filter(lambda x: x[3] == hotelName, fileLines);

            # Only results with 1 nights
            specificHotel = list(filter(lambda x: (datetime.strptime(x[2], '%d-%m-%Y') - datetime.strptime(x[1], '%d-%m-%Y')).days == nights, specificHotel));

            # Slice the list
            getter = itemgetter(1, 4)
            specificHotel = list(map(list, map(getter, specificHotel)))

            # Sorting the rows according by date
            specificHotel.sort(key = lambda row: sorting(row[0]))
            #specificHotel.sort(key = lambda row: (datetime.strptime(row[0], '%d-%m-%Y')))
            #sorted(specificHotel, key=lambda x: datetime.strptime(x[1], '%d-%m-%Y'))
            #sorted(specificHotel, key=lambda x: sorting(x[0]))

            # Add the headers of the CSV
            hotelCsv.writerow([fieldnames[0], fieldnames[1]]);

            # Add only the two first columns of specificHotel list
            for item in specificHotel:
                hotelCsv.writerow(item);
                rowsCount += 1;

            missingCount = 0
            for i in range(0, len(specificHotel) - 1):
                if((datetime.strptime(specificHotel[i+1][0], '%d-%m-%Y') - datetime.strptime(specificHotel[i][0], '%d-%m-%Y')).days > 1):
                    missingCount += 1;

            missingRate = missingCount / rowsCount;

            print("---------------------------");
            print("HoteName: " + hotelName);
            print("Total rows count: " + rowsCount.__str__());
            print("Total missing count: " + missingCount.__str__());
            print("MissingRate: " + missingRate.__str__());
            print("---------------------------");


#print("done, added " + i.__str__() + " rows.");
print("done.");
