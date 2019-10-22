import time
from datetime import datetime
from time import gmtime, strftime
from selenium import webdriver
import csv
import re

previousData = "aa";
currentDate = "";

with open('booking_final.csv', mode='a', newline='') as employee_file:
    with open('booking2.csv', 'r') as file2: # FILE2 (15-30]
        with open('booking.csv', 'r') as file1: # FILE1 [0-15)
            finalCsv = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            file1Lines = [line for line in csv.reader(file1, delimiter=',')]
            file2Lines = [line for line in csv.reader(file2, delimiter=',')]

            for row in file1Lines:
                currentDate = row[0];  # e.g. 09-10-2019

                if(currentDate == previousData):
                    continue;

                rowsByDateFromFile1 = filter(lambda x: x[0] == currentDate, file1Lines);
                rowsByDateFromFile2 = filter(lambda x: x[0] == currentDate, file2Lines);

                finalCsv.writerows(rowsByDateFromFile1);
                finalCsv.writerows(rowsByDateFromFile2);

                previousData = currentDate;


print("done!");