from selenium import webdriver
import chromedriver_autoinstaller 
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


chromedriver_autoinstaller.install()
driver = webdriver.Chrome(service=Service())

driver.get('https://google.com')

box = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
box.send_keys('top 100 movies of all time')

search = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
search.click()

result = driver.find_element(by=By.XPATH, value='//*[@id="rso"]/div[1]/block-component/div/div[1]/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div[1]/a/h3')
result.click()

time.sleep(3)

driver.execute_script('window.scrollTo(0, 10500)')

driver.save_screenshot('C:/Users/harsh/Documents/Web Scraping/screenshotImdb.png')

driver.find_element(by=By.XPATH, value='//*[@id="main"]/div/div[3]/div/div[50]/div[2]/a/img').screenshot('C:/Users/harsh/Documents/Web Scraping/movie.png')


