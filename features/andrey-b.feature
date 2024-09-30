Feature: Test login functionality
# This feature file contains login functionality tests
  Background:
    Given Open "https://www.profitolizer.com"
    Then Wait 1 seconds
    Then Click element "//a[text()='Login']"

#  @no_background
  Scenario: Login with correct credentials
    Then Type "pcs.automationclass@gmail.com" into "//input[@name='username']"
    Then Type "Qwerty7" into "//input[@name='password']"
    Then Click element "//button[contains(text(), 'Login')]"
    Then Wait 1 seconds
    Then Verify page by title "Profotolizer - Projects"

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


  Scenario: Login with correct credentials
    Then Type "pcs.automationclass@gmail.com" into "//input[@name='username']"
    Then Type "Qwerty7" into "//input[@name='password']"
    Then Click element "//button[contains(text(), 'Login')]"
    Then Wait 1 seconds
    Then Verify page by title "Profotolizer - Projects"
    Then Fill out following information
      | project     | First project    |
      | start_date  | 09/30/2024       |
      | description | Some description |
      | dimension   | Month            |
      | duration    | 2 Years          |
    Then Fill out following information with keys
      | project       | start_date | description      | dimension | duration |
      | First project | 09/30/2024 | Some description | Month     | 2 Years  |
