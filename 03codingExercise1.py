import requests
from bs4 import BeautifulSoup

url = 'https://www.marketwatch.com/investing/stock/tsla?mod=search_symbol'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

company_name = soup.h1.text

current_price = soup.find('sup', class_='character').text + " " + soup.find('h2', 
                            class_='intraday__price',).find('bg-quote').text

closing_price = soup.find('td', class_ = 'table__cell u-semi').text;

week_range_52 = '$ ' + soup.find_all('div', class_="range__header")[2].find_all(
    class_='primary')[0].text + ' - $ ' + soup.find_all('div', 
    class_="range__header")[2].find_all(class_='primary')[1].text

analyst_rating = soup.find('li', class_="analyst__option active").text


import pandas as pd

table = pd.DataFrame([[company_name, current_price, closing_price, 
                       week_range_52, analyst_rating],], columns=['Name', 
                       'Current Price', 'Closing Price', '52 Week Range', 'Analyst Rating'])

print(table)