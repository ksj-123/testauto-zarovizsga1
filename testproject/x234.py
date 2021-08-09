# Téglalap kerülete
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


def find_and_clear(id):
    find_clear = driver.find_element_by_id(id)
    find_clear.clear()
    return find_clear


# Load page
URL = driver.get("https://black-moss-0a0440e03.azurestaticapps.net/x234.html")
time.sleep(3)

try:
    # Helyes kitöltés
    def right_text():
        find_and_clear('a')
        find('a').send_keys(99)
        find_and_clear('b')
        find('b').send_keys(12)
        kalkulacio = find('submit')
        kalkulacio.click()


    right_text()

    eredmeny_right = int(find('result').text)
    print(eredmeny_right)
    assert eredmeny_right == 222


    # Nem számokkal történő kitöltés
    def abc_text():
        find_and_clear('a')
        find('a').send_keys('kiskutya')
        find_and_clear('b')
        find('b').send_keys(12)
        kalkulacio = find('submit')
        kalkulacio.click()


    abc_text()

    eredmeny_abc = find('result').text
    print(eredmeny_abc)
    assert eredmeny_abc == 'NaN'


    # Üres kitöltés
    def null_text():
        find_and_clear('a')
        find('a').send_keys('')
        find_and_clear('b')
        find('b').send_keys('')
        kalkulacio = find('submit')
        kalkulacio.click()


    null_text()

    eredmeny_null = find('result').text
    print(eredmeny_null)
    assert eredmeny_null == 'NaN'

finally:
    driver.close()
