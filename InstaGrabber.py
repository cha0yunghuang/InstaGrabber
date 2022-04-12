import urllib.request
import ssl

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import os
import wget

# Explicit Waits
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# for authenticate the ssl certificate issue
def main():
    ssl._create_default_https_context = ssl._create_unverified_context
    r = urllib.request.urlopen('https://google.com')
    print(r.status)
    print(r)
if __name__ == '__main__':
    main()


# chromedriver path
driver = webdriver.Chrome('/Users/erichuang/Dev/chromedriver')

driver.get('https://www.instagram.com')


# Explicit-Wait for username and password textfield
username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)
password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "password"))
)


username.clear()
password.clear()

username.send_keys('YOUR_USERNAME')
password.send_keys('YOUR_PASSWORD')

login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
login.click()


# Explicit-Wait for the searchbar appear
search = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'))
)


# keyword -> enter 2 times
keyword = '#meme'
search.send_keys(keyword)
time.sleep(1)
search.send_keys(Keys.RETURN)
time.sleep(1)
search.send_keys(Keys.RETURN)


# Explicit-Wait for the imageTiles appear
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/article/div[1]'))
)

# create a folder
path = os.path.join(keyword)
os.mkdir(path)

imgs = driver.find_elements_by_class_name('FFVAD')

count = 0
for img in imgs:
    save_as = os.path.join(path, keyword + '_' + str(count) + '.jpg')
    #print(img.get_attribute('src'))
    wget.download(img.get_attribute('src'), save_as)
    count += 1

driver.close()