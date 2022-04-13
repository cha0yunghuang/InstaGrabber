import config
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

# To authenticate the SSL certificate issue
def main():
    ssl._create_default_https_context = ssl._create_unverified_context
    r = urllib.request.urlopen('https://google.com')
    print(r.status)
    print(r)
if __name__ == '__main__':
    main()


driver = webdriver.Chrome(config.chromeDriver)

driver.get('https://www.instagram.com')


# Explicit-Wait, for username and password text field
username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)
password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "password"))
)


username.clear()
password.clear()

username.send_keys(config.username)
password.send_keys(config.password)

login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
login.click()


# Explicit-Wait, for the searchbar to appear
search = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'))
)


# Fill in the keyword, then click Enter 2 times
keyword = config.searchKeyword
search.send_keys(keyword)
time.sleep(1)
search.send_keys(Keys.RETURN)
time.sleep(1)
search.send_keys(Keys.RETURN)


# Explicit-Wait, for the image tiles appear
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/article/div[1]'))
)

# Create a folder
path = os.path.join(keyword)
os.mkdir(path)


imgs = driver.find_elements_by_class_name('FFVAD')

count = 0

# After images are downloaded, scroll, then execute download again.
for i in range(3):

    for img in imgs:
        save_as = os.path.join(path, keyword + '_' + str(count) + '.jpg')
        #print(img.get_attribute('src'))
        wget.download(img.get_attribute('src'), save_as)
        count += 1

    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(5)


time.sleep(4)
driver.close()