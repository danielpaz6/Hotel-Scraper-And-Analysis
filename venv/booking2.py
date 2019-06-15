import time
from datetime import datetime
from time import gmtime, strftime
from selenium import webdriver
import csv
import re

chrome_path = r"D:/chromedriver.exe"
driver = webdriver.Chrome(chrome_path)  # Optional argument, if not specified will search path.

newAddedRows = 0;
RIGHTnow = time.localtime(time.time());
RIGHTtodaysDate = strftime("%d-%m-%Y", RIGHTnow);

for z in range(15, 30):
    for l in range(1, 6): # walk through days ( for example hotels from 1 day to 3 days )
        now = time.localtime(time.time() + (24 * 3600 * z));
        tomorrow = time.localtime(time.time() + (24*3600 * l) + (24 * 3600 * z))

        todaysDate = strftime("%d-%m-%Y", now)
        tomorrowsDate = strftime("%d-%m-%Y", tomorrow)

        checkin_monthday = strftime("%d", now)
        checkin_month = strftime("%m", now)
        checkin_year = strftime("%Y", now)

        checkout_monthday = strftime("%d", tomorrow)
        checkout_month = strftime("%m", tomorrow)
        checkout_year = strftime("%Y", tomorrow)


        for j in range(0, 1): # walk through pages
            try:
                with open('booking2.csv', 'r') as file1:
                    existingLines = [line for line in csv.reader(file1, delimiter=',')]
            except:
                existingLines = []

            flagcount = 0
            while flagcount <= 3:
                index = (j*50).__str__();
                driver.get("https://www.booking.com/searchresults.html?label=gen173nr-1FCAEoggI46AdIM1gEaGqIAQGYARW4ARfIAQzYAQHoAQH4AQuIAgGoAgO4ApS14uUFwAIB&sid=68eafc3a3cd51d49961a273449b15458&sb=1&src=searchresults&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Fsearchresults.html%3Flabel%3Dgen173nr-1FCAEoggI46AdIM1gEaGqIAQGYARW4ARfIAQzYAQHoAQH4AQuIAgGoAgO4ApS14uUFwAIB%3Bsid%3D68eafc3a3cd51d49961a273449b15458%3Btmpl%3Dsearchresults%3Bac_click_type%3Db%3Bac_position%3D0%3Bclass_interval%3D1%3Bdest_id%3D20088325%3Bdest_type%3Dcity%3Bdtdisc%3D0%3Bfrom_sf%3D1%3Bgroup_adults%3D2%3Bgroup_children%3D0%3Biata%3DNYC%3Binac%3D0%3Bindex_postcard%3D0%3Blabel_click%3Dundef%3Bno_rooms%3D1%3Boffset%3D0%3Bpostcard%3D0%3Braw_dest_type%3Dcity%3Broom1%3DA%252CA%3Bsb_price_type%3Dtotal%3Bsearch_selected%3D1%3Bshw_aparth%3D1%3Bslp_r_match%3D0%3Bsrc%3Dindex%3Bsrc_elem%3Dsb%3Bsrpvid%3Dca06887c279e0264%3Bss%3DNew%2520York%252C%2520New%2520York%2520State%252C%2520USA%3Bss_all%3D0%3Bss_raw%3Dnew%3Bssb%3Dempty%3Bsshis%3D0%26%3B&ss=New+York&is_ski_area=0&ssne=New+York&ssne_untouched=New+York&city=20088325&checkin_year="+checkin_year+"&checkin_month="+checkin_month+"&checkin_monthday="+checkin_monthday+"&checkout_year="+checkout_year+"&checkout_month="+checkout_month+"&checkout_monthday="+checkout_monthday+"&group_adults=1&group_children=0&no_rooms=1&from_sf=1&selected_currency=USD&rows=50&offset=" + index)
                time.sleep(4) #  sleep before all data is set up.
                blocks = driver.find_elements_by_class_name("sr_item")
                num_of_blocks = len(blocks)
                with open('booking2.csv', mode='a', newline='') as employee_file:
                    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    for i in range(num_of_blocks):
                        try:
                            hotelName = blocks[i].find_element_by_class_name("sr-hotel__name")
                            hotelPrice = blocks[i].find_element_by_class_name("bui-price-display__value")
                            hotelRating = blocks[i].find_element_by_class_name("bui-review-score__badge")
                            hotelReviews = blocks[i].find_element_by_class_name("bui-review-score__text")

                            #hotelReviews = hotelReviews.re
                            # hotelRating = hotelRating + "/10";
                            #hotelRating += '/10';
                        except:
                            flagcount += 1
                            continue;

                        if(hotelName.size == 0 or hotelPrice.size == 0 or hotelRating.size == 0 or hotelReviews.size == 0):
                            flagcount += 1
                            continue;

                        # date, hotelName, hotelPrice ( shekels ), hotelRating, hotelCountReviews
                        try:
                            if[RIGHTtodaysDate,todaysDate,tomorrowsDate,hotelName.text,re.sub('([^0-9,])+', '', hotelPrice.text),hotelRating.text + "/10",re.sub('([^0-9,])+', '',hotelReviews.text)] not in existingLines:
                                employee_writer.writerow([
                                    RIGHTtodaysDate,
                                    todaysDate,
                                    tomorrowsDate,
                                    hotelName.text,
                                    re.sub('([^0-9,])+', '', hotelPrice.text),
                                    hotelRating.text + "/10",
                                    re.sub('([^0-9,])+', '',hotelReviews.text)
                                ]);
                                newAddedRows += 1
                            else:
                                print("the item is already exists!");

                            print(hotelName.text)
                            print(re.sub('([^0-9,])+', '', hotelPrice.text))
                            print(hotelRating.text + '/10')
                            print(re.sub('([^0-9,])+', '', hotelReviews.text))
                            #print(re.sub('reviews', '', hotelReviews.text))
                        except:
                            flagcount += 1
                            continue;

                if(num_of_blocks > 0):
                    break;

                flagcount += 1

driver.quit()
print("New rows added: " + newAddedRows.__str__());
print("done.");