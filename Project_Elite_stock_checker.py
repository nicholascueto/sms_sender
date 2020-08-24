#! /usr/bin/env python
from twilio.rest import Client
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

#This example requires Selenium WebDriver 3.13 or newer
with webdriver.Firefox() as driver:
    wait = WebDriverWait(driver, 10)
    driver.get("https://google.com/ncr")
    driver.find_element(By.NAME, "q").send_keys("cheese" + Keys.RETURN)
    first_result = wait.until(presence_of_element_located(By.CSS_SELECTOR, "h3>div"))
    print(first_result.get_attribute("textContent"))
  

# open browser

# open page

# get text

# get numbers

# check if number is less than i

# text if less

# Send Text

# Download the twilio-python library from twilio.com/docs/libraries/python

# Find these values at https://twilio.com/user/account
account_sid = "ACcb552aa857431ec8fc8648e5febb8f4e"
auth_token = "b680909b83d0aace2519ad7019d6c576"

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+12316851234",
    from_="+15555555555",
    body="Hello there!")