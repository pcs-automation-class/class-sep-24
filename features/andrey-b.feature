Feature: Test login functionality
# This feature file contains login functionality tests
#  Background:
##    Given Open "https://www.profitolizer.com/"
#    Given Open prod environment
#    Then Wait 1 seconds
#    Then Click element "//a[text()='Login']"

#  @no_background
  Scenario: Login with correct credentials
    Given Open prod environment
    Then Wait 1 seconds
    Then Click element "//a[text()='Login']"
    Then Type "pcs.automationclass@gmail.com" into "//input[@name='username']"
    Then Type "Qwerty7" into "//input[@name='password']"
    Then Click element "//button[contains(text(), 'Login')]"
    Then Wait 1 seconds
    Then Verify page by title "Profotolizer - Projects"


  Scenario: Correct credentials
    Given Open prod environment
    Then Login with Sale credentials
    Then Verify page by title "Profotolizer - Projects"
    Then Andrey Open url


#  @regression
  Scenario Outline: Test with valid credentials
    Then Type "<login>" into "//input[@name='username']"
    Then Type "<password>" into "//input[@name='password']"
    Then Click element "//button[contains(text(), 'Login')]"
    Then Wait 1 seconds
    Then Verify page by title "Profotolizer - Projects"
    Examples:
      | login                           | password |
      | pcs.automationclass@gmail.com   | Qwerty7  |
      | pcs.automationclass+3@gmail.com | Qwerty7  |

#  @regression
  Scenario: Login with incorrect credentials
    Then Type "pcs.automationclass@gmail.com" into "//input[@name='username']"
    Then Wait 1 seconds
    Then Type "123456" into "//input[@name='password']"
    Then Wait 1 seconds
    Then Click element "//button[contains(text(), 'Login')]"
    Then Wait 1 seconds
    Then Verify presents of element "//p[text()='Invalid username or password']"


  Scenario: Fill out data with table
    Then Type "pcs.automationclass@gmail.com" into "//input[@name='username']"
    Then Type "Qwerty7" into "//input[@name='password']"
    Then Click element "//button[contains(text(), 'Login')]"
    Then Wait 1 seconds
    Then Verify page by title "Profotolizer - Projects"
    Then Fill out following information with keys
      | key                 | value            |
      | Project Name        | First project    |
      | Start date          | 09/30/2024       |
      | Project description | Some description |
      | Period Dimension    | Month            |
      | Project Duration    | 2 Years          |
#    Then  Fill out following information
#      | project       | start_date | description      | dimension | duration |
#      | First project | 09/30/2024 | Some description | Month     | 2 Years  |
    Then Wait 5 seconds

  @smoke
  Scenario: First scenario
    Given Open "https://www.profitolizer.com"
    Then Wait 1 seconds

  @regression
  Scenario: Second scenario
    Given Open "https://www.profitolizer.com"
    Then Wait 1 seconds

  @smoke @regression
  Scenario: Third scenario
    Given Open "https://www.profitolizer.com"
    Then Wait 1 seconds

  @api
  Scenario: API weather
    Given Get weather in "Chicago"

#  Scenario: Terms and Conditions verification
#    Given Open prod environment
#    Then Login with Sale credentials
#    Then Verify page by title "Profotolizer - Projects"
#    Then Click element "//a[text()='Privacy Policy']"
#    Then Wait 2 seconds
#    Then Switch to new window
#    Then Verify page by title "Terms and Conditions - Profitolizer"
#    Then Wait 2 seconds
#    Then Close current window
#    Then Wait 2 seconds
#    Then Switch to home window
#    Then Verify page by title "Profotolizer - Projects"