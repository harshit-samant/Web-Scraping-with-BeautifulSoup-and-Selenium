from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import time

url = 'https://www.nike.com/w/sale-3yaep'

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(service = Service())

driver.get(url)

last_height = driver.execute_script('return document.body.scrollHeight')

while True:
    
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(2)
    new_height = driver.execute_script('return document.body.scrollHeight')    
    
    if last_height == new_height:
        break
    last_height = new_height
    
soup = BeautifulSoup(driver.page_source, 'lxml')

product_card = soup.find_all('div', class_='product-card css-1v1uza4 css-z5nr6i css-11ziap1 css-14d76vy css-dpr2cn product-grid__card')

df = pd.DataFrame({'Link': [''], 'Name': [''], 'Description': [''], 'Price': [''], 'Sale_Price': ['']})

for product in product_card:
    try:
        link = product.find('a', class_='product-card__link-overlay').get('href')
        name = product.find('div', class_='product-card__title').text
        description = product.find('div', class_='product-card__subtitle').text
        full_price = product.find('div', class_='product-price is--striked-out').text.strip()
        sale_price = product.find('div', class_='product-price is--current-price css-s56yt7').text.strip()
    
        df = df.append({'Link':link, 'Name':name, 'Description':description, 'Price':full_price, 'Sale_Price':sale_price}, ignore_index=True)
    except: 
        pass

df.to_csv('C:/Users/harsh/Documents/Web Scraping/09InfiniteScrolling.csv')
