import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import openpyxl 

def append_data_to_excel(web_page):
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
        web_driver.get(web_page)
        company=web_driver.find_element(By.XPATH,'//*[@id="header"]/div/div/div/h1/a').text
        website=web_page
        location=web_driver.find_element(By.XPATH,'//*[@id="summary_section"]/div[2]/div[2]/div/div[1]/span').text
        contact=web_driver.find_element(By.XPATH,'//*[@id="quick-menu"]/ul/li[4]/a').text
        rating=web_driver.find_element(By.XPATH,'//*[@id="summary_section"]/div[2]/div[1]/div[2]/div[1]/div/span').text
        total_rating=web_driver.find_element(By.XPATH,'//*[@id="summary_section"]/div[2]/div[1]/div[2]/div[1]/div/a[2]').text
        hourly=web_driver.find_element(By.XPATH,'//*[@id="summary_section"]/div[2]/div[1]/div[3]/div[2]/div/div[2]/span').text
        mini_project=web_driver.find_element(By.XPATH,'//*[@id="summary_section"]/div[2]/div[1]/div[3]/div[2]/div/div[1]/span').text
        employee=web_driver.find_element(By.XPATH,'//*[@id="summary_section"]/div[2]/div[1]/div[3]/div[2]/div/div[3]/span').text
        data=(list([company,website,location,contact,rating,total_rating,hourly,mini_project,employee]))
        time.sleep(0.5)
        web_driver.quit()
        return data
        
