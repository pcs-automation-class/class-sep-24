#Feature: Test login functionality
## Some login functionality tests
#
#
#  Scenario: Play with login functionality
#    Given Open "https://www.profitolizer.com/"
#    Then Wait 5 seconds
#    Then Click element "//a[@class='header-link _btn__link']"
#    Then Wait 1 seconds
#    Then Click element "//button[@class='btn btn-primary w-100']"
#    Then Wait 1 seconds
#    Then Verify presents of element "//div[text()='Email is required']"
#    Then Wait 1 seconds
#    Then Verify presents of element "//div[text()='Password is required']"
#    Then Wait 1 seconds
#    Then Click element "//a[text()='Forgot password?']"
#    Then Wait 1 seconds
#    Then Verify presents of element "//h5[text()='Restore Password']"
#    Then Wait 1 seconds
#    Then Type "test@mail.com" into "//input[@class='el-input__inner']"
#    Then Wait 1 seconds
#    Then Click element "//button[text()=' Send']"
#    Then Wait 1 seconds
#    Then Verify presents of element "//h5[contains(text(), 'Please check your inbox')]"
#    Then Wait 1 seconds
#    Then Click element "//a[@href='https://profitolizer.com/']"
#    Then Wait 1 seconds

Feature: Test login functionality
# This feature file contains login functionality tests


  Scenario: Login with correct credentials
    Given Open "https://www.profitolizer.com"
#    Then Wait 1 seconds
    Then Click element "//a[text()='Login']"
#    Then Wait 1 seconds
    Then Type "pcs.automationclass@gmail.com" into "//input[@name='username']"
    Then Type "Qwerty7" into "//input[@name='password']"
    Then Click element "//button[contains(text(), 'Login')]"
    Then Wait 1 seconds
    Then Verify page by title "Profotolizer - Projects"

  Scenario: Login with incorrect credentials
    Given Open "https://www.profitolizer.com"
    Then Click element "//a[text()='Login']"
#    Then Wait 5 seconds
    Then Type "pcs.automationclass@gmail.com" into "//input[@name='username']"
#    Then Wait 1 seconds
    Then Type "123456" into "//input[@name='password']"
#    Then Wait 1 seconds
    Then Click element "//button[contains(text(), 'Login')]"
    Then Wait 1 seconds
    Then Verify presents of element "//p[text()='Invalid username or password']"
