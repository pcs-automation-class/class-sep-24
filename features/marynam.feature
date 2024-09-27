# Created by mary at 9/23/24
Feature: Test Login functionality 
  # This feature file contains login functionality tests

  Scenario: # Login with correct credentials
  Given Open "https://profitolizer.com"
    Then Click element "//a[text()='Login']"
    Then Wait 5 seconds
    Then Type "mmarchuk81@gmail.com" into "//input[@name='username']"
    Then Wait 4 seconds
    Then Type "o45oHoihj^&$#" into "//input[@name='password']"
    Then Wait 4 seconds
    Then Click element "//button[contains(text(),'Login')]"
    Then Wait 4 seconds
    Then Verify page by title "Profotolizer - Projects"

  Scenario: #Login with no password
  Given Open "https://app.profitolizer.com/#/login"
    Then Type "mmarchuk81@gmail.com" into "//input[@name='username']"
    Then Wait 4 seconds
    Then Click element "//button[contains(text(),'Login')]"
    Then Verify presents of element "//div[@class='invalid-feedback' and text()='Password is required']"

  Scenario: #Forgotten password
  Given Open "https://profitolizer.com"
    Then Click element "//a[text()='Login']"
    Then Wait 4 seconds
    Then Type "mmarchuk81@gmail.com" into "//input[@name='username']"
    Then Wait 4 seconds
    Then Click element "//a[text()='Forgot password?']"
    Then Wait 4 seconds
    Then Verify presents of element "//h5[contains(text(),'Restore Password')]"


