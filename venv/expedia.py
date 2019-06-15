import time
from datetime import datetime
from time import gmtime, strftime
from selenium import webdriver
import csv
import re

counter = 0
RIGHTnow = time.localtime(time.time());
RIGHTtodaysDate = strftime("%d-%m-%Y", RIGHTnow);

for z in range(0,30):
    for k in range(1, 6): # walk through dates ( 1 to 5 )
        now = time.localtime(time.time() + (24 * 3600 * z));
        tomorrow = time.localtime(time.time() + (24 * 3600 * k) + (24 * 3600 * z))

        todaysDate = strftime("%m/%d/%Y", now)
        todaysDate2 = strftime("%d-%m-%Y", now)

        tomorrowsDate = strftime("%m/%d/%Y", tomorrow)
        tomorrowsDate2 = strftime("%d-%m-%Y", tomorrow)

        checkin_monthday = strftime("%d", now)
        checkin_month = strftime("%m", now)
        checkin_year = strftime("%Y", now)

        checkout_monthday = strftime("%d", tomorrow)
        checkout_month = strftime("%m", tomorrow)
        checkout_year = strftime("%Y", tomorrow)

        endDate = tomorrowsDate

        chrome_path = r"D:/chromedriver.exe"
        driver = webdriver.Chrome(chrome_path)  # Optional argument, if not specified will search path.
        # driver.get('https://www.expedia.com/Hotel-Search?destination=New+York%2C+New+York&latLong=40.75668%2C-73.98647&regionId=178293&startDate=" + _startDate + "&endDate=" + _endDate + "&rooms=1&adults=1');
        driver.get(
            'https://www.expedia.com/Hotel-Search?destination=New+York%2C+NY+%28LGA-LaGuardia%29&latLong=40.77429%2C-73.872035&regionId=4278092&startDate='+todaysDate+'&endDate='+endDate+'&rooms=1&adults=1');


        time.sleep(7)

        blocks = driver.find_elements_by_class_name("listing")
        num_of_blocks = len(blocks)

        try:
            with open('expedia.csv', 'r') as file1:
                existingLines = [line for line in csv.reader(file1, delimiter=',')]
        except:
            existingLines = []

        with open('expedia.csv', mode='a', newline='') as employee_file:
            employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for i in range(num_of_blocks):
                try:
                    hotelName = blocks[i].find_element_by_tag_name("h3");
                    hotelPrice = blocks[i].find_element_by_class_name("content-hotel-lead-price--a11y");
                    hotelRank = blocks[i].find_element_by_class_name("listing__reviews");
                    hotelRank = hotelRank.find_elements_by_tag_name('span')
                    hotelRating = hotelRank[0].text;

                    if ("reviews" in hotelRank[1].text):
                        hotelReviews = hotelRank[1].text;
                    else:
                        hotelReviews = hotelRank[2].text;

                    hotelReviews = re.sub(' reviews\)', '', hotelReviews);
                    hotelReviews = re.sub('\(', '', hotelReviews);

                    hotelName = hotelName.text;

                    if ("reviews" in hotelReviews):
                        continue;

                    # Checks if the data already exists !!
                    if [
                        RIGHTtodaysDate,
                        todaysDate2,
                        tomorrowsDate2,
                        hotelName,
                        hotelPrice.text,
                        hotelRating,
                        hotelReviews
                    ] not in existingLines:
                        employee_writer.writerow([
                            RIGHTtodaysDate,
                            todaysDate2,
                            tomorrowsDate2,
                            hotelName,
                            hotelPrice.text,
                            hotelRating,
                            hotelReviews
                        ])
                        counter = counter + 1

                    print(hotelName)
                    print(hotelPrice.text)
                    print(hotelRating)
                    print(hotelReviews)

                except:
                    print("not found")

        driver.quit()

print("rows added: " + counter.__str__())
print("done")