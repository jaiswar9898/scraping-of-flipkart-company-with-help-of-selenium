from selenium import webdriver
from  bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import requests
from openpyxl import Workbook
import time
import pandas as pd 


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("https://www.flipkart.com/")
time.sleep(2)
driver.find_element(By.XPATH,'//button[@class="_2KpZ6l _2doB4z"]').click() # automaticaly click the key 
driver.find_element(By.XPATH,'//input[@class="_3704LK"]').send_keys("vivo phones") # automatically display the key in search box 
driver.find_element(By.XPATH,'//button[@class="L0Z3Pu"]').click() 
time.sleep(6)
titles=driver.find_elements(By.XPATH,'//div[@class="_4rR01T"]') # find the title of only first page of vivo phone 
for index,title in enumerate(titles): # this will print the title with index 
    print(index,title.text)
time.sleep(6)

# i want all rating of vivo phone 
rating=driver.find_elements(By.XPATH,'//span[@class="_1lRcqv"]')
for index,rate in enumerate(rating): 
    print(index,rate.text)

prices=driver.find_elements(By.XPATH,'//div[@class="_30jeq3 _1_WHN1"]')
for index,price in enumerate(prices): 
    print(index,price.text)

crossprices=driver.find_elements(By.XPATH,'//div[@class="_3I9_wc _27UcVY"]')
for index,cross in enumerate(crossprices): 
    print(index,cross.text)

