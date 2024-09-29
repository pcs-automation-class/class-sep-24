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
    Then Wait 5 seconds
    Then Click element "//button/span[text()='Add Project']"

  Scenario: Login with incorrect credentials
    Given Open "https://www.profitolizer.com"
    Then Click element "//a[text()='Login']"
#    Then Wait 6 seconds
    Then Type "pcs.automationclass@gmail.com" into "//input[@name='username']"
#    Then Wait 1 seconds
    Then Type "123456" into "//input[@name='password']"
#    Then Wait 1 seconds
    Then Click element "//button[contains(text(), 'Login')]"
    Then Wait 1 seconds
    Then Verify presents of element "//p[text()='Invalid username or password']"


   Scenario: Login with incorrect credentials
    Given Open "https://www.profitolizer.com"
    Then Click element "//a[text()='Login']"
#    Then Wait 6 seconds
    Then Type "pcs.automationclass@gmail.com" into "//input[@name='username']"
#    Then Wait 1 seconds
    Then Type "123456" into "//input[@name='password']"
#    Then Wait 1 seconds
    Then Click element "//button[contains(text(), 'Login')]"
    Then Wait 1 seconds
    Then Verify presents of element "//p[text()='Invalid username or password']"

