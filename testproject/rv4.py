# Kakukktojás - városok
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)


# Driver find
def find(id):
    find = driver.find_element_by_id(id)
    return find


# Load page
URL = driver.get('https://black-moss-0a0440e03.azurestaticapps.net/rv4.html')
time.sleep(3)

# kigyűjteni a cities.py segítségével a cities.txt-be a városokat
# majd keresni a hiányzót a randomCities -ben


def all_random():
    return driver.find_elements_by_xpath('//*[@id="randomCities"]/li')

# random_list = all_random()
# hiany_list = []
# for hiany in random_list:
#     if hiany.text != 'cities.txt'......:  # a cities.txt fájlból a városokkal
#         hiany_list.append(hiany.text)
#
# print(hiany)

# find('missingCiti').send_keys('hiany')
ellenorzes_btn = find('submit')
ellenorzes_btn.click()

assert find('reslult').text == 'Eltalátad.'