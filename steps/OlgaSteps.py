from time import sleep

from behave import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@step('Olga open "{url}"')
def olga_open_url(context, url):
    context.driver.get(url)

@step('Olga open {env} environment')
def olga_open_env(context, env):
    envs = {
        'prod': 'https://www.profitolizer.com/',
        'dev': 'https://www.dev.profitolizer.com/',
        'test': 'https://www.test.profitolizer.com/',
        'uat': 'https://www.uat.profitolizer.com/',
        'qa': 'https://www.qa.profitolizer.com/',
    }
    olga_open_url(context, envs[env])


@step('Olga click element "{xpath}"')
def olga_click_element(context, xpath):
    # element = context.driver.find_element(By.XPATH, xpath)

    element = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()

@step('Olga type "{text}" into "{xpath}"')
def olga_type_text(context, text, xpath):
    element = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
    # element = context.driver.find_element(By.XPATH, xpath)
    element.send_keys(text)

@step("Olga login with {user} credentials")
def olga_login(context, user):
    users = {
        'Admin': ('ratovbj@htmail.store', '123321'),
        'Wrong': ('ratovbj@mail.store', '1221'),
        'Empty_email': ('', '123321'),
        'Empty_psw': ('ratovbj@htmail.store', '')
    }
    olga_click_element(context, "//a[text()='Login']")
    olga_type_text(context, users[user][0], "//input[@name='username']")
    olga_type_text(context, users[user][1], "//input[@name='password']")
    olga_click_element(context, "//button[contains(text(), 'Login')]")
    sleep(1)


@step('Olga verify presents of element "{xpath}"')
def olga_verify_presents_of_element(context, xpath):
    elements = context.driver.find_elements(By.XPATH, xpath)
    assert len(elements) == 1


@step("Olga fill out following information with keys")
def create_project_keys(context):
    elements = {
        'Project Name': "//div[./label[text()='Project Name']]//input",
        'Start date': "//input[@placeholder='Start date']",
        'Project description': "//div[./label[text()='Project description']]//textarea",
        'Period Dimension': "//span[text()='Period Dimension']",
        'Project Duration': "//div[./label[text()='Project Duration']]//span[text()='",
    }
    for row in context.table:
        if row.cells[0] in ['Project Name', 'Start date', 'Project description']:
            olga_type_text(context, row.cells[1], elements[row.cells[0]])
        elif row.cells[0] == 'Period Dimension':
            olga_click_element(context, elements[row.cells[0]])
            sleep(0.5)
            olga_click_element(context, f"//li/span[text()='{row.cells[1]}']")
        else:
            olga_click_element(context, f"{elements[row.cells[0]]}{row.cells[1]}']")