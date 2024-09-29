# Created by Anna at 23.09.2024
Feature: Test login functionality


  Scenario: Login with correct credentials
    Given Open "https://www.profitolizer.com"
    Then Wait 1 seconds
    Then Click element "//a[text()='Login']"
    Then Wait 1 seconds
    Then Type "dudnikovaanna545+1@gmail.com" into "//input[@name='username']"
    Then Type "09172024@Sept" into "//input[@name='password']"
    Then Click element "//button[contains(text(), 'Login')]"
    Then Wait 1 seconds
    Then Verify page by title "Profotolizer - Projects"

  Scenario: Login with incorrect credentials (wrong password)
    Given Open "https://www.profitolizer.com"
    Then Wait 1 seconds
    Then Click element "//a[text()='Login']"
    Then Wait 1 seconds
    Then Type "dudnikovaanna545+1@gmail.com" into "//input[@name='username']"
    Then Type "09172024@Sep" into "//input[@name='password']"
    Then Click element "//button[contains(text(), 'Login')]"
    Then Wait 1 seconds
    Then Verify page by title "Profotolizer - Login"

  Scenario: Login with no password
    Given Open "https://www.profitolizer.com"
    Then Wait 1 seconds
    Then Click element "//a[text()='Login']"
    Then Wait 1 seconds
    Then Type "dudnikovaanna545+1@gmail.com" into "//input[@name='username']"
    Then Click element "//button[contains(text(), 'Login')]"
    Then Wait 1 seconds
    Then Verify presents of element "//div[text()='Password is required']"

  Scenario: Restore password page
    Given Open "https://www.profitolizer.com"
    Then Wait 1 seconds
    Then Click element "//a[text()='Login']"
    Then Wait 1 seconds
    Then Click element "//a[@href='#/restorePassword']"
    Then Wait 1 seconds
    Then Verify presents of element "//h5[text()='Restore Password']"


  Scenario: Restore password - email is sent
    Given Open "https://www.profitolizer.com"
    Then Wait 1 seconds
    Then Click element "//a[text()='Login']"
    Then Wait 1 seconds
    Then Click element "//a[@href='#/restorePassword']"
    Then Wait 1 seconds
    Then Verify presents of element "//h5[text()='Restore Password']"
    Then Type "dudnikovaanna545+1@gmail.com" into "//input[@autocomplete="off"]"
    Then Click element "//button[contains(text(), ' Send')]"
    Then Wait 1 seconds
    Then Verify page by title "Profotolizer - Restore Password"

  Scenario: New Project
    Given Open "https://www.profitolizer.com"
    Then Wait 1 seconds
    Then Click element "//a[text()='Login']"
    Then Wait 1 seconds
    Then Type "dudnikovaanna545+1@gmail.com" into "//input[@name='username']"
    Then Type "09172024@Sept" into "//input[@name='password']"
    Then Click element "//button[contains(text(), 'Login')]"
    Then Wait 1 seconds
    Then Verify page by title "Profotolizer - Projects"
    Then Click element "//span[contains(text(),'Add Project')]"
    Then Click element "//div[@class ='el-input']//input"
    Then Type "One more project" into "//div[@class ='el-input']//input"
    Then Click element "//input[@aria-label="Start date"]"
    Then Wait 1 seconds
    Then Click element "//td[@class="available"]//span[text()='26']"
    Then Click element "//span[text()='Period Dimension']"
    Then Wait 1 seconds
    Then Click element "//span[text()='Month']"
    Then Click element "//span[text()='1 Year']"
    Then Click element "//textarea"
    Then Type "Another project, but this one is second actually, number two" into "//textarea"
    Then Click element "//div[@class="d-flex mt-3 align-items-center"]/button"
    Then Wait 5 seconds
    Then Verify presents of element "//div[@class="el-dropdown"]/button[text()='One more project ']"

  Scenario: Delete project
    Given Open "https://www.profitolizer.com"
    Then Wait 1 seconds
    Then Click element "//a[text()='Login']"
    Then Wait 1 seconds
    Then Type "dudnikovaanna545+1@gmail.com" into "//input[@name='username']"
    Then Type "09172024@Sept" into "//input[@name='password']"
    Then Click element "//button[contains(text(), 'Login')]"
    Then Wait 1 seconds
    Then Verify page by title "Profotolizer - Projects"
    Then Wait 1 seconds
    Then Click element "//button[text()='Accept All']"
    Then Wait 1 seconds
    Then Click element "//div[@class="el-dropdown"]"
    Then Wait 1 seconds
    Then Click element "//li[text()='One more project']"
    Then Wait 1 seconds
    Then Click element "//span[text()='Settings']"
    Then Wait 1 seconds
    Then Click element "//button[text()=' Delete']"
    Then Wait 1 seconds
    Then Verify presents of element "//h1[text()='Warning']"
    Then Click element "//button[@class="btn btn-danger"]"
    Then Wait 3 seconds
    Then Verify presents of element "//a[text()='Second project']"

  Scenario: Logout
    Given Open "https://www.profitolizer.com"
    Then Wait 1 seconds
    Then Click element "//a[text()='Login']"
    Then Wait 1 seconds
    Then Type "dudnikovaanna545+1@gmail.com" into "//input[@name='username']"
    Then Type "09172024@Sept" into "//input[@name='password']"
    Then Click element "//button[contains(text(), 'Login')]"
    Then Wait 1 seconds
    Then Click element "//a[@data-bs-toggle="dropdown"]"
    Then Wait 1 seconds
    Then Click element "//span[text()='Sign Out']"
    Then Wait 1 seconds
    Then Verify page by title "Profotolizer - Login"

  Scenario: Check email
    Given Open "https://www.profitolizer.com"
    Then Wait 1 seconds
    Then Click element "//a[text()='Login']"
    Then Wait 1 seconds
    Then Type "dudnikovaanna545+1@gmail.com" into "//input[@name='username']"
    Then Type "09172024@Sept" into "//input[@name='password']"
    Then Click element "//button[contains(text(), 'Login')]"
    Then Wait 1 seconds
    Then Click element "//a[@data-bs-toggle="dropdown"]"
    Then Wait 1 seconds
    Then Verify presents of element "//span[text()='dudnikovaanna545+1@gmail.com']"

  Scenario: Go to profile
    Given Open "https://www.profitolizer.com"
    Then Wait 1 seconds
    Then Click element "//a[text()='Login']"
    Then Wait 1 seconds
    Then Type "dudnikovaanna545+1@gmail.com" into "//input[@name='username']"
    Then Type "09172024@Sept" into "//input[@name='password']"
    Then Click element "//button[contains(text(), 'Login')]"
    Then Wait 1 seconds
    Then Click element "//a[@data-bs-toggle="dropdown"]"
    Then Wait 1 seconds
    Then Click element "//i[@class="bi bi-person"]"
    Then Wait 1 seconds
    Then Verify page by title "Profotolizer - Profile"

  Scenario: Go to subscription
    Given Open "https://www.profitolizer.com"
    Then Wait 1 seconds
    Then Click element "//a[text()='Login']"
    Then Wait 1 seconds
    Then Type "dudnikovaanna545+1@gmail.com" into "//input[@name='username']"
    Then Type "09172024@Sept" into "//input[@name='password']"
    Then Click element "//button[contains(text(), 'Login')]"
    Then Wait 1 seconds
    Then Click element "//a[@data-bs-toggle="dropdown"]"
    Then Wait 1 seconds
    Then Click element "//ul[@class="dropdown-menu dropdown-menu-end dropdown-menu-arrow profile show"]//a[@href="#/subscription"]"
    Then Wait 1 seconds
    Then Verify page by title "Profotolizer - Subscription"

# Commented because made some steps changes in my computer, so now it makes no sense I believe
# Reason: when I try change first name and last name the necessary text fields are empty,but when it`s done by driver firstly I had to make them blank

#  Scenario: Add first name and last name
#    Given Open "https://www.profitolizer.com"
#    Then Wait 1 seconds
#    Then Click element "//a[text()='Login']"
#    Then Wait 1 seconds
#    Then Type "dudnikovaanna545+1@gmail.com" into "//input[@name='username']"
#    Then Type "09172024@Sept" into "//input[@name='password']"
#    Then Click element "//button[contains(text(), 'Login')]"
#    Then Wait 1 seconds
#    Then Click element "//a[@data-bs-toggle="dropdown"]"
#    Then Wait 1 seconds
#    Then Click element "//i[@class="bi bi-person"]"
#    Then Wait 1 seconds
#    Then Verify page by title "Profotolizer - Profile"
#    Then Wait 1 seconds
#    Then Click element "//label[text()='First name']/../div[@class='el-form-item__content']//input"
#    Then Clear "//label[text()='First name']/../div[@class='el-form-item__content']//input"
#    Then Wait 1 seconds
#    Then Type "Jason" into "//label[text()='First name']/../div[@class='el-form-item__content']//input"
#    Then Wait 1 seconds
#    Then Click element "//label[text()='Last name']/../div[@class='el-form-item__content']//input"
#    Then Clear "//label[text()='Last name']/../div[@class='el-form-item__content']//input"
#    Then Wait 1 seconds
#    Then Type "Dean" into "//label[text()='Last name']/../div[@class='el-form-item__content']//input"
#    Then Wait 1 seconds
#    Then Click element "//button[text()=' Save']"
#    Then Wait 1 seconds
#    Then Verify presents of element "//a[@data-bs-toggle="dropdown"]//span[text()='Jason Dean']"

#  Scenario: Empty first name
#    Given Open "https://www.profitolizer.com"
#    Then Wait 1 seconds
#    Then Click element "//a[text()='Login']"
#    Then Wait 1 seconds
#    Then Type "dudnikovaanna545+1@gmail.com" into "//input[@name='username']"
#    Then Type "09172024@Sept" into "//input[@name='password']"
#    Then Click element "//button[contains(text(), 'Login')]"
#    Then Wait 1 seconds
#    Then Click element "//a[@data-bs-toggle="dropdown"]"
#    Then Wait 1 seconds
#    Then Click element "//i[@class="bi bi-person"]"
#    Then Wait 1 seconds
#    Then Verify page by title "Profotolizer - Profile"
#    Then Wait 1 seconds
#    Then Clear "//label[text()='First name']/../div[@class='el-form-item__content']//input"
#    Then Click element "//label[text()='First name']/../div[@class='el-form-item__content']//input"
#    Then Wait 1 seconds
#    Then Click element "//button[text()=' Save']"
#    Then Wait 1 seconds
#    Then Verify presents of element "//div[text()='Please input first name']"
#    Then Verify presents of element "//a[@data-bs-toggle="dropdown"]//span[text()='Jason Dean']"
#
#  Scenario: Empty last name
#    Given Open "https://www.profitolizer.com"
#    Then Wait 1 seconds
#    Then Click element "//a[text()='Login']"
#    Then Wait 1 seconds
#    Then Type "dudnikovaanna545+1@gmail.com" into "//input[@name='username']"
#    Then Type "09172024@Sept" into "//input[@name='password']"
#    Then Click element "//button[contains(text(), 'Login')]"
#    Then Wait 1 seconds
#    Then Click element "//a[@data-bs-toggle="dropdown"]"
#    Then Wait 1 seconds
#    Then Click element "//i[@class="bi bi-person"]"
#    Then Wait 1 seconds
#    Then Verify page by title "Profotolizer - Profile"
#    Then Wait 1 seconds
#    Then Clear "//label[text()='Last name']/../div[@class='el-form-item__content']//input"
#    Then Wait 1 seconds
#    Then Click element "//button[text()=' Save']"
#    Then Wait 1 seconds
#    Then Verify presents of element "//div[text()='Please select last name']"
#    Then Verify presents of element "//a[@data-bs-toggle="dropdown"]//span[text()='Jason Dean']"

  Scenario: Check Bronze Plan
    Given Open "https://www.profitolizer.com"
    Then Wait 1 seconds
    Then Click element "//a[text()='Login']"
    Then Wait 1 seconds
    Then Type "dudnikovaanna545+1@gmail.com" into "//input[@name='username']"
    Then Type "09172024@Sept" into "//input[@name='password']"
    Then Click element "//button[contains(text(), 'Login')]"
    Then Wait 1 seconds
    Then Click element "//a[@data-bs-toggle="dropdown"]"
    Then Wait 1 seconds
    Then Click element "//i[@class="bi bi-person"]"
    Then Wait 1 seconds
    Then Verify page by title "Profotolizer - Profile"
    Then Wait 1 seconds
    Then Click element "//button[text()='Current subscription']"
    Then Wait 1 seconds
    Then Verify presents of element "//h5[text()='Trial Bronze plan']"

    Scenario: Add Service
    Given Open "https://www.profitolizer.com"
    Then Wait 1 seconds
    Then Click element "//a[text()='Login']"
    Then Wait 1 seconds
    Then Type "dudnikovaanna545+1@gmail.com" into "//input[@name='username']"
    Then Type "09172024@Sept" into "//input[@name='password']"
    Then Click element "//button[contains(text(), 'Login')]"
    Then Wait 1 seconds
    Then Click element "//span[text()='Sales']"
    Then Wait 1 seconds
    Then Click element "//span[text()='Services/Products']"
    Then Wait 1 seconds
    Then Click element "//div[@class="el-table__body-wrapper"]//i[@class='bi bi-plus']"
    Then Wait 1 seconds
    Then Click element "//input[@placeholder="Service name"]"
    Then Wait 1 seconds
    Then Type "New One" into "//input[@placeholder="Service name"]"
    Then Wait 1 seconds
    Then Click element "//div[@class="el-select__selected-item el-select__placeholder is-transparent"]"
    Then Wait 1 seconds
    Then Click element "//li[@class="el-select-dropdown__item is-hovering"]"
    Then Wait 1 seconds
    Then Click element "//button[@class="el-button el-button--success el-button--small is-circle"]"
    Then Verify presents of element "//div[@class="cell"]//span[@class="el-text el-text--success"]"

  Scenario: Add Compositions
    Given Open "https://www.profitolizer.com"
    Then Wait 1 seconds
    Then Click element "//a[text()='Login']"
    Then Wait 1 seconds
    Then Type "dudnikovaanna545+1@gmail.com" into "//input[@name='username']"
    Then Type "09172024@Sept" into "//input[@name='password']"
    Then Click element "//button[contains(text(), 'Login')]"
    Then Wait 1 seconds
    Then Click element "//span[text()='Sales']"
    Then Wait 1 seconds
    Then Click element "//span[text()='Compositions']"
    Then Wait 1 seconds
    Then Click element "//button[text()=' Generate Components']"
    Then Wait 3 seconds
    Then Verify presents of element "//h4[text()='Suggestion preview']"
    Then Click element "//div[@class="d-flex justify-content-between my-2"][3]/button[2]"
    Then Wait 1 seconds
    Then Click element "//h4[text()='Suggestion preview']/../button"
    Then Wait 1 seconds
    Then Verify presents of element "//div[@class="cell"][text()='New_consumable_1']"

  Scenario: Check daily limit of "Daily requests to AI"
    Given Open "https://www.profitolizer.com"
    Then Wait 1 seconds
    Then Click element "//a[text()='Login']"
    Then Wait 1 seconds
    Then Type "dudnikovaanna545+1@gmail.com" into "//input[@name='username']"
    Then Type "09172024@Sept" into "//input[@name='password']"
    Then Click element "//button[contains(text(), 'Login')]"
    Then Wait 1 seconds
    Then Click element "//span[text()='Sales']"
    Then Wait 1 seconds
    Then Click element "//span[text()='Compositions']"
    Then Wait 1 seconds
    Then Verify presents of element "//button[text()=' I want more']"

    #TODO
  Scenario: Add component for cost forecast
    Given Open "https://www.profitolizer.com"
    Then Wait 1 seconds
    Then Click element "//a[text()='Login']"
    Then Wait 1 seconds
    Then Type "dudnikovaanna545+1@gmail.com" into "//input[@name='username']"
    Then Type "09172024@Sept" into "//input[@name='password']"
    Then Click element "//button[contains(text(), 'Login')]"
    Then Wait 1 seconds
    Then Click element "//button[text()='Accept All']"
    Then Wait 1 seconds
    Then Click element "//span[text()='Sales']"
    Then Wait 1 seconds
    Then Click element "//span[text()='Cost Forecast']"
    Then Wait 1 seconds
    Then Click element "//button[@class="btn btn-primary"]"
    Then Wait 1 seconds
    Then Verify presents of element "//div[@class="modal-header"]"
    Then Wait 1 seconds
    Then Click element "//label[text()='Component Name']/../div//input"
    Then Wait 1 seconds
    Then Type "Another" into "//label[text()='Component Name']/../div//input"
    Then Wait 1 seconds
    Then Click element "//label[text()='Unit']/../div"
    Then Wait 1 seconds
    #clickable and not at the same time
    Then Click element "//div[@id="el-popper-container-700"]/div[6]/div/div/div/ul/li[1]"
    Then Wait 1 seconds
    Then Click element "//div[@class="modal-footer"]/button[@class="btn btn-success"]"
    Then Wait 1 seconds
    Then Verify presents of element "//div[@class="text-wrap text-start"][text()='Another, gal']"

  Scenario: Check investment group help
    Given Open "https://www.profitolizer.com"
    Then Wait 1 seconds
    Then Click element "//a[text()='Login']"
    Then Wait 1 seconds
    Then Type "dudnikovaanna545+1@gmail.com" into "//input[@name='username']"
    Then Type "09172024@Sept" into "//input[@name='password']"
    Then Click element "//button[contains(text(), 'Login')]"
    Then Wait 1 seconds
    Then Click element "//a[@data-bs-target="#Investments-nav"]"
    Then Wait 1 seconds
    Then Click element "//ul[@id="Investments-nav"]//span[text()='Groups']"
    Then Wait 1 seconds
    Then Click element "//h1[text()='Investment Groups']/../button[@title='Help']"
    Then Wait 1 seconds
    Then Verify presents of element "//h4[text()='Investment Groups Help']"












