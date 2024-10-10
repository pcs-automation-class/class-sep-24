from time import sleep

from behave import step
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

@step('Maria Open "{url}"')
def maria_open_url(context, url):
    context.driver.get(url)

@step('Maria Click Element "{xpath}"')
def maria_click_element(context, xpath):
    element = context.driver.find_element(By.XPATH, xpath)
    element.click()

@step('Maria Type "{text}" Into "{xpath}"')
def maria_type_text(context, text, xpath):
    element = context.driver.find_element(By.XPATH, xpath)
    element.send_keys(text)

@step('Maria Wait {sec} seconds')
def maria_wait_sec(context, sec):
    sleep(int(sec))

@step('Maria Verify page by Title "{text}"')
def maria_verify_page_by_title(context, text):
    title = context.driver.title
    assert title == text

@step('Maria Verify Presents of Element "{xpath}"')
def maria_verify_presents_of_element(context, xpath):
    elements = context.driver.find_elements(By.XPATH, xpath)
    assert len(elements) == 1

@step('Maria Press a key "{key}"')
def maria_press_key(context, key):
    key_to_press = getattr(Keys, key.upper())
    element = context.driver.switch_to.active_element
    element.send_keys(key_to_press)

@step('Maria Type a "{text}"')
def maria_type_text(context, text):
    element = context.driver.switch_to.active_element
    element.send_keys(text)




