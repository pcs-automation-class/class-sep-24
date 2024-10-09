from time import sleep

from behave import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


@step('Anna Open "{url}"')
def open_url(context, url):
    print(f"Opening url {url}")
    context.driver.get(url)


@step('Anna Open {env} environment')
def open_env(context, env):
    envs = {
        'prod': 'https://www.profitolizer.com',
        'dev': 'https://www.dev.profitolizer.com',
        'test': 'https://www.test.profitolizer.com',
        'uat': 'https://www.uat.profitolizer.com',
        'qa': 'https://www.qa.profitolizer.com',
    }
    open_url(context, envs[env])
    sleep(1)


@step('Anna Wait {sec} seconds')
def wait_sec(context, sec):
    sleep(int(sec))


@step('Anna Click element "{xpath}"')
def click_element(context, xpath):
    element = context.driver.find_element(By.XPATH, xpath)

    # element = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()


@step('Anna Type "{text}" into "{xpath}"')
def type_text(context, text, xpath):
    # element = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
    element = context.driver.find_element(By.XPATH, xpath)
    element.send_keys(text)
    # element.send_keys(Keys.COMMAND, 'a')

@step('Anna Clear "{xpath}"')
def clear_nope(context, xpath):
    element = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
    # element = context.driver.find_element(By.XPATH, xpath)
    element.send_keys(Keys.BACKSPACE*10)


@step('Anna Verify page by title "{text}"')
def verify_title(context, text):
    title = context.driver.title
    assert title == text, f"Expected title: {text}, actual title: {title}. "


@step('Anna Verify presents of element "{xpath}"')
def verify_presents_of_element(context, xpath):
    elements = context.driver.find_elements(By.XPATH, xpath)
    assert len(elements) == 1


@step("Anna Fill out following information")
def create_project(context):
    elements = {
        'project': "//div[./label[text()='Project Name']]//input",
        'start_date': "//input[@placeholder='Start date']",
        'description': "//div[./label[text()='Project description']]//textarea",
        'dimension': "//span[text()='Period Dimension']",
        'duration': "//span[text()='",
    }
    for row in context.table:
        type_text(context, row[0], elements['project'])
        type_text(context, row[1], elements['start_date'])
        type_text(context, row[2], elements['description'])
        click_element(context, elements['dimension'])
        sleep(1)
        click_element(context, f"//li/span[text()='{row[3]}']")
        click_element(context, f"{elements['duration']}{row[4]}']")


@step("Anna Fill out following information with keys")
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
            type_text(context, row.cells[1], elements[row.cells[0]])
        elif row.cells[0] == 'Period Dimension':
            click_element(context, elements[row.cells[0]])
            sleep(0.5)
            click_element(context, f"//li/span[text()='{row.cells[1]}']")
        else:
            click_element(context, f"{elements[row.cells[0]]}{row.cells[1]}']")


@step("Anna Login with {user} credentials")
def login(context, user):
    users = {
        'Admin': ('dudnikovaanna545+2@gmail.com', '09172024@Sept'),
        'Sale': ('dudnikovaanna545+3@gmail.com', '09172024@Septe'),
        'Wrong': ('dudnikovaanna545+2@gmail.com', '09172024@S'),
    }
    click_element(context, "//a[text()='Login']")
    type_text(context, users[user][0], "//input[@name='username']")
    type_text(context, users[user][1], "//input[@name='password']")
    click_element(context, "//button[contains(text(), 'Login')]")
    sleep(1)

@step("Anna Choose {item} in sidenav")
def choose_side(context, item):

    items = {
        'sales': "//span[text()='Sales']",
        'team': "//span[text()='Team']",
        'invest': "//span[text()='Investments']",
        'rent': "//span[text()='Rent']",
        'expenses': "//span[text()='Expenses']",
        'pl': "//span[text()='P&L']",
        'plgraphs': "//span[text()='P&L Graphs']"
    }
    click_element(context, items[item])
    sleep(1)


@step("Anna Choose {smth} in Sales")
def choose_sale(context, smth):
    items = {
        'serv_and_prod': "//span[text()='Services/Products']",
        'compos': "//span[text()='Compositions']",
        'cost_fore': "//span[text()='Cost Forecast']",
        'price_sced': "//span[text()='Pricing Schedule']",
        'sales_plan': "//span[text()='Sales plan']"
    }
    click_element(context, items[smth])
    sleep(1)

@step("Anna Add {one} Service or Product")
def add_servs(context, one):
    click_element(context, "//div[@class='el-table__body-wrapper']//i[@class='bi bi-plus']")
    click_element(context, "//input[@placeholder='Service name']")
    servs = {
        'service': "fff",
        'product': "aaa"
    }
    type_text(context, servs[one], "//input[@placeholder='Service name']")
    click_element(context, "//div[@class='el-select__selected-item el-select__placeholder is-transparent']")
    click_element(context, "//li[@class='el-select-dropdown__item is-hovering']")
    click_element(context, "//button[@class='el-button el-button--success el-button--small is-circle']")
    sleep(1)

