Feature: Test login functionality

Scenario: Login with valid credentials
  Given Open "https://www.profitolizer.com"
  Then Click element "//a[text()='Login']"
  Then Type "gordeevag@inbox.ru" into "//input[@name='username']"
  Then Type "Zz12345678" into "//input[@name='password']"
  Then Click element "//button[@type='submit']"
  Then Wait 2 seconds
  Then Verify page by title "Profotolizer - Projects"

Scenario: Login with invalid password
  Given Open "https://www.profitolizer.com"
  Then Click element "//a[text()='Login']"
  Then Type "testgmail@gmail.com" into "//input[@name='username']"
  Then Type "WrongPassword" into "//input[@name='password']"
  Then Click element "//button[@type='submit']"
  Then Wait 2 seconds
  Then Verify presents of element "//p[text()='Invalid username or password']"

Scenario: Login with empty username field
  Given Open "https://www.profitolizer.com"
  Then Click element "//a[text()='Login']"
  Then Type "PasswordTest" into "//input[@name='password']"
  Then Click element "//button[@type='submit']"
  Then Wait 2 seconds
  Then Verify presents of element "//div[text()='Email is required']"

Scenario: Restore password for registered email
  Given Open "https://www.profitolizer.com"
  Then Click element "//a[text()='Login']"
  Then Click element "//a[text()='Forgot password?']"
  Then Wait 2 seconds
  Then Type "test@test.com" into "//input[@class]"
  Then Click element "//button[text()=' Send']"
  Then Wait 2 seconds
  Then Verify presents of element "//h5[contains(text(),'Restore Password')]"