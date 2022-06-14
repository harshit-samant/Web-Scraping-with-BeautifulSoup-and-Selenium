
import requests
from bs4 import BeautifulSoup

#Getting html from website
url = 'https://webscraper.io/test-sites/e-commerce/allinone'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')


#Tags

soup.header
soup.div

#Navigable Strings

soup.header.p.string

#Attributes (attrs keyword is used to extract attributes from any html tags)
soup.header.a.attrs['new-attribute'] = 'This is a new attribute'
soup.header.a.attrs

#Comments
print