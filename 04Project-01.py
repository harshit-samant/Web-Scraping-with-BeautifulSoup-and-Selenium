import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.worldometers.info/world-population/'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

table = soup.find('table', class_='table table-striped table-bordered table-hover table-condensed table-list')

headers = []

for i in table.findAll('th'):
    headers.append(i.text)

df = pd.DataFrame(columns = headers)

for j in table.findAll('tr')[1:]:
    row_data = j.findAll('td')
    
    row = [tr.text for tr in row_data]
    length = len(df)
    df.loc[length] = row

df.to_csv('C:/Users/harsh/Documents/Web Scraping/04Project01_table.csv')
