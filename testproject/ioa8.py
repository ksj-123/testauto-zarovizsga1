# Összeadó
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
URL = driver.get('https://black-moss-0a0440e03.azurestaticapps.net/ioa8.html')
time.sleep(3)

try:
    # Num
    num1 = int(find('num1').text)
    num2 = int(find('num2').text)


    def algebra():
        if find('op').text == '+':
            summary = num1 + num2
            return summary
        elif find('op').text == '-':
            deduc = num1 - num2
            return deduc
        elif find('op').text == '*':
            multi = num1 * num2
            return multi
        elif find('op').text == '/':
            division = num1 / num2
            return division


    button = find('submit')
    button.click()

    result = algebra()
    print(result)
    print(find('result').text)
    assert int(result) == int(find('result').text)

finally:
    driver.close()
