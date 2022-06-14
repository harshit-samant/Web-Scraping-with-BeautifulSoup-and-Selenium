from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(service=Service())

driver.get('https://google.com')

box = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')

box.send_keys('girrafe')


# Search button
button = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
button.click()


# Click first result of web search
# link = driver.find_element(by=By.XPATH, value='//*[@id="rso"]/div[1]/div/div/div[1]/div/a/h3')
# link.click()


# Screenshot

# driver.save_screenshot('C:/Users/harsh/Documents/Web Scraping/screenshot.png')


# Scrolling

time.sleep(5)

link = driver.find_element(by=By.XPATH, value='//*[@id="hdtb-msb"]/div[1]/div/div[2]/a')
link.click()

while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')

