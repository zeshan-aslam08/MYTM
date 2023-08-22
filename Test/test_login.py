import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")
driver.get("https://mytmtravels.com/")
# Maximize window
driver.maximize_window()
time.sleep(5)
# Minimize Window
driver.minimize_window()
# Getting Current Url
url = driver.current_url
print(url)
# Getting Title
title = driver.title
print(title)
# Waits in selenium
# implicit wait
# explicit wait
# Close Driver
driver.close()
# Quit Driver
driver.quit
# Locaters are use to identify web element of web page
# By ID ,By Name ,By Class ,By Xpath ,By Css Selector ,By Link Text
