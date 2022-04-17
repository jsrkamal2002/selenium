from lib2to3.pgen2 import driver
import selenium
from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="c:\\kamal\selenium\\chromedriver.exe")
#url='google.com'
driver.get('url')
while True:
    time.sleep(2)
    driver.refresh()
