from time import sleep

from behave import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


@step('Andrey Open url')
def andrey_open_url(context):
    context.browser.get('https://profitolizer.com')
