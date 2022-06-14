import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.carpages.ca/used-cars/search/?fueltype_id%5B0%5D=3&fueltype_id%5B1%5D=7'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

df = pd.DataFrame({'links':[''], 'Name':[''], 'Edition':[''], 'Distance':[''], 'Color': [''], 'Price':['']})

while True:
    postings = soup.findAll('div', class_='media soft push-none rule')

    for post in postings:   
        try:
            link = post.find('a', class_='media__img media__img--thumb').get('href')
            full_link = 'https://www.carpages.ca' + link
            name = post.find('h4', class_='hN').text.strip()
            edition = post.find('h5', class_='hN grey').text
            distance = post.find('div', class_='grey l-column l-column--small-6 l-column--medium-4').text.strip()
            color = post.findAll('div', class_='grey l-column l-column--small-6 l-column--medium-4')[1].text.strip()
            price = post.find('strong', class_='delta').text.strip()
        
            df = df.append({'links':full_link, 'Name':name, 'Edition':edition, 
                            'Distance':distance, 'Color': color, 'Price':price}, ignore_index=True)
        except: 
            pass
        
    
    try:
        next_page = 'https://www.carpages.ca' + soup.find('a', {'title': 'Next Page'}).get('href')
    
        url = next_page
    
        page = requests.get(url)

        soup = BeautifulSoup(page.text, 'lxml')
    except:
        break
    
df.to_csv('C:/Users/harsh/Documents/Web Scraping/05Project02-carPage.csv')
print("Scraping finished and saved into file named: 05Project02-carPage.csv")
