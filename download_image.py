from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

image_url='https://free-braindumps.com/images/exam-dumps/DP-100/0acc88f1-bc57-45ad-82ac-98db103411f6.jpg'

driver.get(image_url)

# Wait for the page to load (adjust the wait time as needed)
time.sleep(5)

# Capture the full page as screenshot (modify as needed to capture specific area)
driver.save_screenshot("img2.jpg")

# Close the browser
driver.quit()