from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

PATH = "chromedriver.exe"

driver = webdriver.Chrome()

driver.get('https://za.indeed.com/?r=us')
time.sleep(10)

search  = driver.find_element(By.ID,"text-input-what")
search.send_keys("Data Analyst")
search  = driver.find_element(By.ID,"text-input-where")
search.send_keys("KwaZulu-Natal")
search.send_keys(Keys.RETURN)

def search_page():
  time.sleep(10)
  cards = driver.find_elements(By.CLASS_NAME,"job_seen_beacon")

  for card in cards:
    # Find all anchor tags (a) within the card element
    anchor_tags = card.find_elements(By.TAG_NAME, "a")

    for anchor in anchor_tags:
      # Get the ID (if it exists)
      element_id = anchor.get_attribute("id")

      # Get the href attribute
      href = anchor.get_attribute("href")
      if element_id!="":

      # Print the results
        anchor.click()
        
        time.sleep(10)
        side = driver.find_element(By.XPATH, "//h2[@data-testid='jobsearch-JobInfoHeader-title']")
        header = side.find_element(By.TAG_NAME, "span")
        try:
          company=driver.find_element(By.XPATH,"//div[@data-testid='inlineHeader-companyName']")
          company_bol = company.get_attribute("data-company-name")
          
          company_name = company.text if company_bol=="true" else ""
        except:
          pass
        descrip = driver.find_element(By.ID,"jobDescriptionText")
        descrip_text = descrip.get_attribute("innerText")

        print(f"ID: {element_id}, Job name:{header.text.replace('- job post','').strip()}, company name: {company_name}, job description: {descrip_text}")

while True:
  time.sleep(10)
  try:
    
    nx_pg = driver.find_element(By.XPATH, "//a[@data-testid='pagination-page-next']")
    nx_pg.click()
    try:
      #press the pop up
      pop_x = driver.find_element(By.XPATH, "//button[@aria-label='close']")
      pop_x.click()
    except:
      #the pop-up aint there

      print("Guess no pop-up")
    finally:
      #continue with this esh either way
      print("continue either way")

      
    print('On to the next page')
    
    
  except:
    print("I GUESS THAT IT!!!!")
    break
# for card in cards:
#     header = card.find_element(By.TAG_NAME, "span")
#     if "data analyst" in header.text.lower():  
#         print(header.text)


# time.sleep(10000)