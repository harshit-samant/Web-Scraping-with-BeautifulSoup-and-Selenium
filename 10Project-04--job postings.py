from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time

url = 'https://in.indeed.com/'
job = 'data analyst'
city = 'noida'

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(service=Service())

driver.get(url)

time.sleep(3)

job_input = driver.find_element(By.XPATH, '//*[@id="text-input-what"]')
job_input.send_keys(job)

city_input = driver.find_element(By.XPATH, '//*[@id="text-input-where"]')
city_input.send_keys(city)

search = driver.find_element(By.XPATH, '//*[@id="jobsearch"]/button')
search.click()

df = pd.DataFrame({'Link': [''], 'Title': [''], 'Company Name': [''], 'Location': [''], 'Date': [''], 'Salary': ['']})

while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')

    time.sleep(3)

    soup = BeautifulSoup(driver.page_source, 'lxml')

    postings = soup.find('ul', class_='jobsearch-ResultsList').find_all('li')

    for post in postings:
        try:
            link = 'https://in.indeed.com/' + post.find('h2', class_='jobTitle').find('a').get('href')
            title = post.find('h2', class_='jobTitle').text
            company = post.find('div', class_='heading6 company_location tapItem-gutter companyInfo')
            company_name = company.find('span').text
            try: 
                company_address = company.find('div', class_='companyLocation').text
            except:
                company_address = 'N/A'
            
            date = post.find('span', class_='date').text.strip()
            try: 
                salary = post.find('div', class_='metadata salary-snippet-container').text
            except:
                salary = 'N/A'
            df = df.append({'Link': link, 'Title': title, 'Company Name': company_name, 'Location': company_address, 'Date': date, 'Salary': salary}, ignore_index=True)
        except:
            pass
    try: 
        next_page = 'https://in.indeed.com/' + soup.find('a', attrs = {'aria-label': 'Next'}).get('href')
        driver.get(next_page)
    except:
        break
    
df.to_csv('C:/Users/harsh/Documents/Web Scraping/10Project-04--job postings.csv')