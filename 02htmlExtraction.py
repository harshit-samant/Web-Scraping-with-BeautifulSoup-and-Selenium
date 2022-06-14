import requests
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/allinone/phones/touch'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')


#Find

soup.find('h4', {'class': 'pull-right price'}).string
soup.find('h4', class_ = 'pull-right price')

#Find All

soup.find_all('h4', {'class': 'pull-right price'})

soup.find_all('a', class_='title')
 #all list items after index 5
soup.find_all('p', class_='pull-right')[5:]

#Find All Part-2

soup.find_all(['h1','h2','h3', 'h5'])
soup.find_all(id = True)
soup.find_all(string = 'Iphone')
soup.find_all(string = ['Iphone', 'Nokia X'])

import re 

soup.find_all(string = re.compile('Nokia'))
soup.find_all(class_ = re.compile('pull'))
soup.find_all('p', class_ = re.compile('pull'))
soup.find_all('p', class_ = re.compile('pull'), limit = 4)

#Find All Part-3
product_name = soup.find_all('a', class_='title')
price = soup.find_all('h4', class_='pull-right price')
reviews = soup.find_all('p', class_='pull-right')
descriptions = soup.find_all('p', class_='description')

product_name_list = []
for i in product_name:
    name = i.text
    product_name_list.append(name)
    
    
product_price_list = []
for i in price:
    price = i.text
    product_price_list.append(price)


product_review_list = []
for i in reviews:
    review = i.text
    product_review_list.append(review)


product_description_list = []
for i in descriptions:
    description = i.text
    product_description_list.append(description)

import pandas as pd

table = pd.DataFrame({'Product Name' : product_name_list, 
                      'Description': product_description_list,
                      'Price': product_price_list,
                      'Reviews': product_review_list})

#Extracting Data from nested Html tags

boxes = soup.find_all('div', class_='col-sm-4 col-lg-4 col-md-4')[6]
print(boxes.find('a').text)






