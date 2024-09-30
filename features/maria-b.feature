# Created by bassm at 9/29/2024

Feature: # Test login functionality
  # This feature file contains login functionality tests

  Scenario: Login with correct credentials
    Given Open "https://www.profitolizer.com"
    Then Click element "//a[text()='Login']"
    Then Type "mariatest252@gmail.com" into "//input[@name='username']"
    Then Type "ABCD1" into "//input[@type='password']"
    Then Click element "//button[@type='submit']"
    Then Wait 1 seconds
    Then Verify page by title "Profotolizer - Projects"

  Scenario: Email textfield is empty
    Given Open "https://www.profitolizer.com"
    Then Click element "//a[text()='Login']"
    Then Type "ABCD1" into "//input[@type='password']"
    Then Click element "//button[@type='submit']"
    Then Wait 1 seconds
    Then Verify presents of element "//div[text()='Email is required']"

    Scenario: Invalid password input
    Given Open "https://www.profitolizer.com"
    Then Click element "//a[text()='Login']"
    Then Type "mariatest252@gmail.com" into "//input[@name='username']"
    Then Type "ABCD4" into "//input[@type='password']"
    Then Click element "//button[@type='submit']"
    Then Wait 1 seconds
    Then Verify presents of element "//p[text()='Invalid username or password']"

    Scenario: Forgotten password
    Given Open "https://www.profitolizer.com"
    Then Click element "//a[text()='Login']"
    Then Click element "//a[text()='Forgot password?']"
    Then Wait 1 seconds
    Then Type "mariatest252@gmail.com" into "//input[@class='el-input__inner']"
    Then Click element "//button[text()=' Send']"
    Then Wait 1 seconds
    Then Verify presents of element "//h5[contains(text(),'Restore Password')]"


