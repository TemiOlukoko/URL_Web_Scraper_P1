import requests
from bs4 import BeautifulSoup
import os

url = 'https://www.airbnb.co.uk/s/Ljubljana--Slovenia/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&query=Ljubljana%2C%20Slovenia&place_id=ChIJ0YaYlvUxZUcRIOw_ghz4AAQ&checkin=2020-11-01&checkout=2020-11-08&source=structured_search_input_header&search_type=autocomplete_click'

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
    print(link)
