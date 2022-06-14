import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.nfl.com/standings/league/2019/REG'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

table = soup.find('table', class_="d3-o-table d3-o-table--row-striping d3-o-table--detailed d3-o-standings--detailed d3-o-table--sortable {sortlist: [[4,1]], sortinitialorder: 'desc'}")

column_name = []

for i in table.findAll('th'):
    column_name.append(i.text)

df = pd.DataFrame(columns = column_name)

for row in table.findAll('tr')[1:]:
    first_td = row.findAll('td')[0].find('div', class_='d3-o-club-fullname').text.strip()
    data = row.findAll('td')[1:]
    row_data = [td.text.strip() for td in data]
    row_data.insert(0, first_td)
    length = len(df)
    df.loc[length] = row_data
    
df.to_csv('C:/Users/harsh/Documents/Web Scraping/04Project01_NFltable.csv')
