Feature: Test login functionality

  Scenario: Login happy path
    Given Olga open prod environment
    Then Olga login with Admin credentials
#    Then Wait 1 seconds
#    Then Click element "//a[text()='Login']"
#    Then Wait 2 seconds
#    Then Type "ratovbj@htmail.store" into "//input[@name='username']"
#    Then Wait 1 seconds
#    Then Click element "//input[@name='password']"
#    Then Wait 1 seconds
#    Then Type "123321" into "//input[@name='password']"
#    Then Wait 1 seconds
#    Then Click element "//button[contains(text(), 'Login')]"
#    Then Wait 2 seconds
    Then Verify page by title "Profotolizer - Projects"

  Scenario: Login with wrong credentials
    Given Olga open prod environment
    Then Olga login with Wrong credentials
#    Given Open "https://www.profitolizer.com"
#    Then Wait 1 seconds
#    Then Click element "//a[text()='Login']"
#    Then Type "ratovbj@mail.store" into "//input[@name='username']"
#    Then Type "1233" into "//input[@name='password']"
#    Then Click element "//button[contains(text(), 'Login')]"
#    Then Wait 2 seconds
    Then Verify presents of element "//p[text() = 'Invalid username or password']"

  Scenario: Login without username
    Given Olga open prod environment
    Then Olga login with Empty_email credentials
#    Given Open "https://www.profitolizer.com"
#    Then Click element "//a[text()='Login']"
#    Then Click element "//input[@name='password']"
#    Then Type "123321" into "//input[@name='password']"
#    Then Wait 1 seconds
#    Then Click element "//button[contains(text(), 'Login')]"
    Then Verify presents of element "//div[text() = 'Email is required']"

  Scenario: Login without password
    Given Olga open prod environment
    Then Olga login with Empty_psw credentials
#    Given Open "https://www.profitolizer.com"
#    Then Click element "//a[text()='Login']"
#    Then Type "ratovbj@htmail.store" into "//input[@name='username']"
#    Then Wait 1 seconds
#    Then Click element "//button[contains(text(), 'Login')]"
    Then Verify presents of element "//div[text() = 'Password is required']"

  Scenario: Recreate the password
    Given Olga open prod environment
    Then Click element "//a[text()='Login']"
    Then Wait 1 seconds
    Then Click element "//a[text()='Forgot password?']"
    Then Wait 1 seconds
    Then Type "ratovbj@htmail.store" into "//input[@class='el-input__inner']"
    Then Wait 1 seconds
    Then Click element "//button[contains(text(), 'Send')]"
    Then Wait 2 seconds
    Then Verify presents of element "//h5[contains(text(), 'Please check your inbox.')]"

  Scenario: Creating a Project
    Given Olga open prod environment
    Then Olga login with Admin credentials
#    Given Open "https://www.profitolizer.com"
#    Then Wait 1 seconds
#    Then Click element "//a[text()='Login']"
#    Then Wait 1 seconds
#    Then Type "ratovbj@htmail.store" into "//input[@name='username']"
#    Then Wait 1 seconds
#    Then Click element "//input[@name='password']"
#    Then Wait 1 seconds
#    Then Type "123321" into "//input[@name='password']"
#    Then Wait 1 seconds
#    Then Click element "//button[contains(text(), 'Login')]"
#    Then Wait 2 seconds
    Then Verify page by title "Profotolizer - Projects"
    #Then Click element "//label[text()='Project Name']/following-sibling::div//input[@id=//label[text()='Project Name']/@for]/ancestor::div[@class='el-input__wrapper']"
    Then Wait 1 seconds
    Then Type "Example" into "//input[@class='el-input__inner'][not(contains(@placeholder, 'Start date'))]"
    Then Wait 1 seconds
    Then Click element "//input[@placeholder='Start date']"
    Then Wait 1 seconds
    Then Type "2024-10-05" into "//input[@class='el-input__inner'][contains(@placeholder, 'Start date')]"
    Then Wait 1 seconds
    Then Click element "//span[text()='Period Dimension']"
    Then Wait 1 seconds
    Then Click element "//span[text()='Month']"
    Then Wait 1 seconds
    Then Click element "//span[text()='2 Years']"
    Then Wait 1 seconds
    Then Click element "//button[text()=' Save'][not(contains(@class,'me-2'))]"
    Then Wait 2 seconds

  Scenario: Creating/Deleting a Project
    Given Olga open prod environment
    Then Olga login with Admin credentials
#    Given Open "https://www.profitolizer.com"
#    Then Click element "//a[text()='Login']"
#    Then Wait 2 seconds
#    Then Type "ratovbj@htmail.store" into "//input[@name='username']"
#    Then Wait 2 seconds
#    Then Type "123321" into "//input[@name='password']"
#    Then Wait 2 seconds
#    Then Click element "//button[contains(text(), 'Login')]"
    Then Wait 2 seconds
    Then Verify page by title "Profotolizer - Projects"
    Then Olga fill out following information with keys
      | key                 | value      |
      | Project Name        | example    |
      | Start date          | 2024/10/24 |
      | Project description | test       |
      | Period Dimension    | Month      |
      | Project Duration    | 2 Years    |
    Then Wait 7 seconds
    Then Click element "//button[text()=' Save'][not(contains(@class,'me-2'))]"
    Then Wait 7 seconds
    Then Click element "//span[text()='Settings']"
    Then Wait 2 seconds
    Then Click element "//button[contains(text(),'Delete')]"
    Then Wait 2 seconds
    Then Click element "//button[text()='Delete']"