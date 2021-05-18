# Scrapping elexon reports between 2 dates

##  Requirements
 - Python 3
 - Selenium
 - Geckodriver on path(https://github.com/mozilla/geckodriver/releases)

##  Source
 - https://www.bmreports.com/bmrs/?q=balancing/systemsellbuyprices/historic
 
- https://www.elexon.co.uk/documents/training-guidance/bsc-guidance-notes/beginners-guide-2/

# Code explanation
scraping.py creates the dataset folder where all the reports between start_date and end_date will be storage, then run gen_csv.py to join all the reports in one .csv

## Glosary

**Settlement:** Period of 30 minutes where electricity is traded
**Period:** Number between 1 and 48 that indicates the settlement ( 1 = 00:00 to 00:30, 48 = 23:30 to 00:00
**Offer:** Proposal to increase generation or reduce demand (sell electricity)
**Bid:** proposal to reduce generation or increase demand (buy energy)
**Imbalance:** Difference between electricity produced and used

## Important data
 - Settlement Date: date
 - Period: time
 - System Sell Price (SSB): £/MWh
 - System Buy Price (SBP): £/MWh
 - Net Imbalance Volume (NIV): MWh
 - Offer Volume (OV): MWh
 - Bid Volume (BV): MWh

## What could we make with this?

Using data analytics generate a more detailed report of performance during the last months, know which month you could buy cheaper electricity in average and which month you could sell it in a higher price and compare with the company actions , same with groups of hours, check the imbalance performance during the months or see the behavior of the offer and bid volume.

Also this process could help to feed a predictive model to know the prices that could have the electricity in the future, or the volumes that could be traded