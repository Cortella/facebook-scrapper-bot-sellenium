# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 19:03:28 2022

@author: bnmac
"""

#imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.get("http://www.facebook.com")
driver.find_element_by_xpath("//*[@id='email']").send_keys("bnmachado10@gmail.com")
driver.find_element_by_xpath("//*[@id='pass']").send_keys("th4pr29eyu")

#target the login button and click it
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

driver.get("https://www.facebook.com/117437320954615/posts/137734662258214")
buttonComment= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Comentar")]'))).click()

