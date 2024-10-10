from time import sleep
from behave import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


@step('Aleks_G_Open "{url}"')
def open_url(context, url):
    print(f"Opening url {url}")
    context.driver.get(url)


@step('Aleks_G_Wait {sec} seconds')
def wait_sec(context, sec):
    sleep(float(sec))


@step('Aleks_G_Click element "{xpath}"')
def click_element(context, xpath):
    element = context.driver.find_element(By.XPATH, xpath)
    element.click()


@step('Aleks_G_Type "{text}" into "{xpath}"')
def type_text(context, text, xpath):
    element = context.driver.find_element(By.XPATH, xpath)
    element.send_keys(text)