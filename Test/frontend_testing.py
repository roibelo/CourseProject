from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

try:
    driver = webdriver.Chrome(service=Service('C:/Users/Admin/Downloads/chromedriver.exe'))
    driver.get('http://localhost:5001/users/get_user_data/12')
    element = driver.find_element(By.ID, value='user')
    print(element.text)
except Exception as ex:
    print("Error: " + ex.__str__())
finally:
    driver.quit()
