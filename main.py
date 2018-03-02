import requests
from lxml import html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scraper import Person
from scraper.objects import Scraper
import time

def is_signed_in(driver):
    try:
        driver.find_element_by_id("profile-nav-item")
        return True
    except:
        pass
    return False

def main():
    url = "https://www.linkedin.com/in/harryliu0/"

    driver = webdriver.Chrome()
    driver.get(url)

if __name__ == '__main__':
    print("Starting...")
    main()

    # url = "https://www.linkedin.com/in/harryliu0/"
    # url2 = "https://www.linkedin.com/in/andre-iguodala-65b48ab5"
    # person = Person(url, driver = driver, scrape=False)
    # time.sleep(15)
    # person.scrape(close_on_complete=False)
    # print(person)
