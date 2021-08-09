# Email mező
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
URL = driver.get('https://black-moss-0a0440e03.azurestaticapps.net/mm43.html')
time.sleep(3)

try:
    # Helyes kitöltés
    find_and_clear('email')
    find('email').send_keys('teszt@elek.hu')
    find('submit').click()

    if driver.find_element_by_xpath('/html/body/div/div/form').text == 'has-validation-error':
        print(driver.find_element_by_xpath('//*[@class="validation-error"]').text)
    else:
        print('Nincs validációs hibaüzenet')

    # Helytelen kitöltés
    find_and_clear('email')
    find('email').send_keys('teszt@')
    find('submit').click()

    print(driver.find_element_by_xpath('//*[@class="validation-error"]').text)
    assert driver.find_element_by_xpath(
        '//*[@class="validation-error"]').text == 'Kérjük, adja meg a „@” utáni részt is. A(z) „teszt@” cím nem teljes.'

    # Üres kitöltés
    find_and_clear('email')
    find('email').send_keys('')
    find('submit').click()

    print(driver.find_element_by_xpath('//*[@class="validation-error"]').text)
    assert driver.find_element_by_xpath(
        '//*[@class="validation-error"]').text == 'Kérjük, töltse ki ezt a mezőt.'

finally:
    driver.close()
