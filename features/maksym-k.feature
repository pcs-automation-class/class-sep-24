Feature: Test login functionality
# This feature file contains login functionality tests
  Background:
    Given Open "https://www.profitolizer.com"
    Then Wait 1 seconds
    Then Click element "//a[text()='Login']"

#  @no_background
  Scenario: Login with correct credentials
    Then Type "makstester77@gmail.com" into "//input[@name='username']"
    Then Type "12345678" into "//input[@name='password']"
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
      | login                    | password |
      | makstester77@gmail.com   | 12345678 |
      | makstester77+1@gmail.com | 12345678 |

#  @regression
  Scenario: Login with incorrect credentials
    Then Type "makstester7@gmail.com" into "//input[@name='username']"
    Then Wait 1 seconds
    Then Type "123456" into "//input[@name='password']"
    Then Wait 1 seconds
    Then Click element "//button[contains(text(), 'Login')]"
    Then Wait 1 seconds
    Then Verify presents of element "//p[text()='Invalid username or password']"


  Scenario: Fill out data with table
    Then Type "makstester77@gmail.com" into "//input[@name='username']"
    Then Type "12345678" into "//input[@name='password']"
    Then Click element "//button[contains(text(), 'Login')]"
    Then Wait 1 seconds
    Then Verify page by title "Profotolizer - Projects"
    Then Fill out following information with keys
      | key                 | value            |
      | Project Name        | First project    |
      | Start date          | 10/01/2024       |
      | Project description | Some description |
      | Period Dimension    | Month            |
      | Project Duration    | 2 Years          |
#    Then  Fill out following information
#      | project       | start_date | description      | dimension | duration |
#      | First project | 09/30/2024 | Some description | Month     | 2 Years  |
    Then Wait 5 seconds
