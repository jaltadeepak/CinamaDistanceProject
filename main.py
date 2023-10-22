from bms_scraper import Scraper
from geocoder import Geocoder
from distance_calc import Distance
from jsontocsv import JSONtoCSV

scraper = Scraper()
geocoder = Geocoder()
dist_calc = Distance()
tocsv = JSONtoCSV()

scraper.scrape()
geocoder.geocodeCinemas()
geocoder.geocodeCurrentAddress()
dist_calc.CalcDistance()
tocsv.converter()