import requests
from bs4 import BeautifulSoup
import os

url = 'https://www.airbnb.co.uk/s/Bath/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=november&flexible_trip_dates%5B%5D=october&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&place_id=ChIJLeE-dKZ4cUgRCZpt1tAnixM&checkin=2021-09-30&checkout=2021-10-01&adults=1&source=search_blocks_selector_p1_flow&search_type=search_query'

#reach out to server with requests and get information back
r = requests.get(url)

#create soup
#in this case BeautifulSoup is the html parser
soup = BeautifulSoup(r.text, 'html.parser')

#find all images tages
images = soup.find_all('img',{"src":True})

for image in images:
    #alt tag usually contains name of image
    name = image['alt']
    link = image['src']
    print(name, link)
    #save image - open file
