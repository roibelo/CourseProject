import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def do_post_request(user_id):
    try:
        url = "http://127.0.0.1:5000/users/" + str(user_id)
        res = requests.post(url, json={"user_name": "John"})
        if res.ok:
            data = res.json()
            print("user " + data["user_added"] + " has been added")
        else:
            raise Exception("test failed  " + str(res))
    except Exception as ex:
        raise Exception("test failed:" + ex.__str__())


def do_get_request(user_id):
    try:
        url = "http://127.0.0.1:5000/users/" + str(user_id)
        res = requests.get(url)
        if res.ok and res.status_code == 200:
            data = res.json()
            if data["user_name"][0] == "John":
                print("data is equals")
            else:
                raise Exception("test failed")
        else:
            raise Exception("test failed")
    except Exception as ex:
        raise Exception("test failed")


def do_selenium_request(user_id):
    try:
        url = "http://127.0.0.1:5001/users/get_user_data/" + str(user_id)
        driver = webdriver.Chrome(service=Service('C:/Users/Admin/Downloads/chromedriver.exe'))
        driver.get(url)
        element = driver.find_element(By.ID, value='user')
        if element.text == "John":
            print("user name is correct")
        else:
            raise Exception("test failed")
    except Exception as ex:
        raise Exception("test failed")
    finally:
        driver.quit()


do_post_request(6)
do_get_request(6)
do_selenium_request(6)