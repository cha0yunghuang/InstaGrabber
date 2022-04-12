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


# Explicit-Wait for username and password
username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)
password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "password"))
)

