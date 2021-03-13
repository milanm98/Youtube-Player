from selenium import webdriver
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time

options = webdriver.ChromeOptions()
options.add_argument('--disable-gpu')

Song = str(input())

driver = webdriver.Chrome(executable_path="chromedriver", chrome_options=options)
driver.get("http://www.youtube.com")
delay = 2

search = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, "search")))
search.click()
search.send_keys(Song)
searchButton = driver.find_element_by_id("search-icon-legacy")
searchButton.click()

playSong = WebDriverWait(driver, delay*5).until(EC.presence_of_element_located((By.XPATH, "/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]")))
playSong.click()

try:
    WebDriverWait(driver, delay*10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[17]/div/div[3]/div/div[2]/span/button"))).click()
except:
    pass