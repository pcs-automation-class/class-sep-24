# Created by nati- at 9/23/2024
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: Login with correct credentials
    Given Open "https://www.profitolizer.com"
    Then Wait 1 seconds
    Then click element "//a[text()='Login']"
    Then Type "namelessgirla@gmail.com" into "//input[@name='username']"
    Then Type "zxcvb7" into "//input[@name='password']"
    Then Click element "//button[contains(text(), 'Login')]"
    Then Wait 2 seconds
    Then Verify page by title "Profotolizer - Projects"


    Scenario: Login without username
    Given Open "https://www.profitolizer.com"
    Then Click element "//a[text()='Login']"
    Then Click element "//input[@name='password']"
    Then Type "123123" into "//input[@name='password']"
    Then Wait 1 seconds
    Then Click element "//button[contains(text(), 'Login')]"
    Then Wait 2 seconds
    Then Verify page by title "Profotolizer - Login"


      Scenario: login with wrong credentials
    Given Open "https://app.profitolizer.com/#/login"
    Then Wait 2 seconds
    Then Type "wrongemail@gmail.com" into "//input[@required][@name='username']"
    Then Type "1999900w" into "//input[@required][@name='password']"
    Then Click element "//button[@type='submit']"
    Then Wait 2 seconds
    Then Verify presents of element "//p[contains(text(),'Invalid username or password')]"