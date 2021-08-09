# Pénzfeldobás
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


def all_result():
    return driver.find_elements_by_xpath('//*[@id="results"]/li')


# Load page
URL = driver.get("https://black-moss-0a0440e03.azurestaticapps.net/tts4.html")
time.sleep(3)

# 100 gombnyomás
for i in range(100):
    money_btn = find('submit')
    money_btn.click()

all_reasult_s = all_result()
print(len(all_reasult_s))
assert len(all_reasult_s) == 100

# min 30 fej
result_list = all_result()
fej_list = []
for fej in result_list:
    if fej.text == "fej":
        fej_list.append(fej.text)

print(len(fej_list))
assert len(fej_list) >= 30

driver.close()
