 #reddit

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time 


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH) 
driver.get("https://duckduckgo.com/")

search = driver.find_element_by_id("search_form_input_homepage")
search.send_keys("reddit")
search.send_keys(Keys.RETURN)

driver.implicitly_wait(5)


element = WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.CLASS_NAME, "result__title")))
element.click()

    driver.implicitly_wait(5)

login = driver.find_element_by_link_text("Log In").click()

driver.implicitly_wait(5)

username = driver.find_element_by_id("loginUsername")
username.click()
username.send_keys("O André Ventura é Sexy")

