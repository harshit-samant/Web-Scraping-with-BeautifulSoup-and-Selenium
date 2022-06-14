import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.airbnb.ca/s/honolulu/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&date_picker_type=calendar&checkin=2022-06-08&checkout=2022-06-10&source=structured_search_input_header&search_type=user_map_move&query=Honolulu%2C%20HI%2C%20United%20States&ne_lat=22.011284845115938&ne_lng=-156.17162000338112&sw_lat=20.6204253108008&sw_lng=-158.33372941190873&zoom=10&search_by_map=true'
page = requests.get(url, headers = {'User-agent': 'Super Bot Power Level Over 9000'})
soup = BeautifulSoup(page.text, 'lxml')

df = pd.DataFrame({'links':[''], 'Title':[''], 'Details':[''], 'Price': [''], 'Rating':['']})

while True:
    posting_container = soup.find('div', class_='_11ry7lz');
    postings = posting_container.findAll('div', class_='c4mnd7m dir dir-ltr')
    for post in postings:
        try:
            link = post.find('a', class_='lwm61be dir dir-ltr')
            full_link = 'https://www.airbnb.ca' + link.get('href')
            title = post.find('div', {'id' : link.get('aria-labelledby')}).text
            price = post.find('span', class_='_tyxjp1').text
            rating = post.find('span', class_='ru0q88m dir dir-ltr').text
            details = post.find('span', class_='dir dir-ltr').text
        
            df = df.append({'links':full_link, 'Title':title, 'Details':details, 
                        'Price': price, 'Rating': rating}, ignore_index = True)
        except:
            pass

    next_page = soup.find('a', {'aria-label': 'Next'}).get('href');
    full_next_page = 'https://www.airbnb.ca' + next_page

    url = full_next_page
    page = requests.get(url, headers = {'User-agent': 'Super Bot Power Level Over 9000'})
    soup = BeautifulSoup(page.text, 'lxml')

df.to_csv('C:/Users/harsh/Documents/Web Scraping/05Project02-airbnb.csv');
