# Városok kigyűjtése
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)

# Load page
driver.get('https://black-moss-0a0440e03.azurestaticapps.net/rv4.html')
time.sleep(3)
cities_elements = driver.find_elements_by_id('cities')

with open('cities.txt', 'w') as citiesfile:
    for cities in cities_elements:
        citiesfile.write(cities.get_attribute(id).replace('/n'))

