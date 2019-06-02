## Hotel `Scraper` And `Analysis`

[![Travis-CI Build Status](https://travis-ci.com/danielpaz6/Hotel-Scraper-And-Analysis.svg?branch=master)](https://travis-ci.com/danielpaz6/Hotel-Scraper-And-Analysis)

### Hotel Scraper for research project structured to analysis data and predict prices.

As part of a research I am doing at the college, I need to go into the various hotel sites, extract data from them and analyze them.
This project is going to be updated regularly during the coming semesters until the end of the research.

## Introduction
The general idea of the study is to estimate the prices of hotels according to different regions and hotel names.

The main advantage of the success of predicting hotel prices is the ability to lower costs to the various search sites that offer hotel search services.

This is because those websites that offer hotel search services use the original hotel's database to provide service to those customers who are looking for hotels, and the cost of such search in the hotel's database costs money.

On the other hand, if those sites had the ability to predict a high percentage of success in hotel prices, they would not have to make immediate use of the databases of those hotels, but rather use forecasting, a kind of "smart database".

And only when the customer is certain that he's interest in purchasing a room reservation, the hotel search services would perform a secondary search, this time in the hotel's database, to get the exact price / availability of the hotel's room.

The idea is not to always use the database of hotel sites, but only if the user really wants to buy, thus saving significant costs of money on the service and use of the same databases provided by hotel sites.

## How it works
So there are two main files: ```expedia.py``` and ```booking.py``` that basically just extract the hotels suggestion from these websites, and saves them in a CSV file that later on will be used for analysis.

An example for data that could be extracted from these website:

| Check-In Date | Check-Out Date | Hotel Name | Price($) | Rating | Number of Reviews |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 07-05-2019 | 08-05-2019 | Hotel Pennsylvania | 200 | 5.6/10 | 40,753 |
| 07-05-2019 | 08-05-2019 | The Mansfield Hotel | 215 | 7.6/10 | 765 |
| 07-05-2019 | 08-05-2019 | Days Hotel by Wyndham on Broadway NYC | 194 | 6.6/10 | 4,984 |
| 07-05-2019 | 08-05-2019 | Holiday Inn Manhattan Financial District | 499 | 8.2/10 | 2,441 |
| 07-05-2019 | 08-05-2019 | Millennium Hilton New York One UN Plaza | 459 | 8.4/10 | 3,957 |
| 07-05-2019 | 08-05-2019 | Hyatt Place New York/Midtown-South | 359 | 8.6/10 | 3,639 |


## Getting Started

In order to fulfill this research needs, I had to learn Python independently, since it is a language that supports functional programming, friendly programming that is suitable for the purposes of research.

The files on this repositoriy

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them:

imports / technologies:

* pip-19.0.3
* selenium
* datetime
* csv
* re
* urlib3
* setuptools

It can be done for example in PyCharm ( as I use this IDE for python in this repository ):

```
File -> Settings -> Project: *Your Project Name* -> Project Interpreter
```

Then search for: pip, selenium, setuptools, urlib3.

## Built With

* [PyCharm](https://www.jetbrains.com/pycharm/) - The Python IDE


## Authors

* **Daniel Paz** - *Part of the research program* - [Profile](https://github.com/DanielPaz6)
* **Aviv Ezer** - *Part of the research program*
* **Hadar Shemesh** - *Part of the research program*
