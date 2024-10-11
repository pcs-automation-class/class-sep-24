Feature: # Test login functionality
  # This feature file contains login functionality tests

  Scenario: Login with correct credentials
    Given Maria Open "https://www.profitolizer.com"
    Then Maria Click Element "//a[text()='Login']"
    Then Maria Type "mariatest252@gmail.com" Into "//input[@name='username']"
    Then Maria Type "ABCD1" Into "//input[@type='password']"
    Then Maria Click Element "//button[@type='submit']"
    Then Maria Wait 1 seconds
    Then Maria Verify page by Title "Profotolizer - P&L charts"

  Scenario: Email textfield is empty
    Given Maria Open "https://www.profitolizer.com"
    Then Maria Click Element "//a[text()='Login']"
    Then Maria Type "<ABCD1>" Into "//input[@type='password']"
    Then Maria Click Element "//button[@type='submit']"
    Then Maria Wait 1 seconds
    Then Maria Verify Presents of Element "//div[text()='Email is required']"

  Scenario: Sign in using TAB and ENTER keys
    Given Maria Open "https://www.profitolizer.com"
    Then Maria Click Element "//a[text()='Login']"
    Then Maria Press a key "TAB"
    Then Maria Press a key "TAB"
    Then Maria Type a "mariatest252@gmail.com"
    Then Maria Press a key "TAB"
    Then Maria Type a "ABCD1"
    Then Maria Press a key "TAB"
    Then Maria Press a key "Enter"
    Then Maria Wait 1 seconds
    Then Maria Verify page by Title "Profotolizer - P&L charts"


    Scenario: Forgotten password using TAB and ENTER keys
    Given Open "https://www.profitolizer.com"
    Then Click element "//a[text()='Login']"
    Then Maria Press a key "TAB"
    Then Maria Press a key "TAB"
    Then Maria Type a "mariatest252@gmail.com"
    Then Maria Press a key "TAB"
    Then Maria Press a key "TAB"
    Then Maria Press a key "TAB"
    Then Maria Press a key "Enter"
    Then Maria Wait 1 seconds
    Then Maria Press a key "TAB"
    Then Maria Press a key "TAB"
    Then Maria Type a "mariatest252@gmail.com"
    Then Maria Press a key "TAB"
    Then Maria Press a key "Enter"
    Then Maria Wait 1 seconds
    Then Maria Verify Presents of Element "//h5[contains(text(),'Restore Password')]"


