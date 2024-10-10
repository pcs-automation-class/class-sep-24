Feature: Test login functionality

Scenario: Login with valid credentials
  Given Aleks_G_Open "https://www.profitolizer.com"
  Then Aleks_G_Click element "//a[text()='Login']"
  Then Aleks_G_Type "gordeevag@inbox.ru" into "//input[@name='username']"
  Then Aleks_G_Type "Zz12345678" into "//input[@name='password']"
  Then Aleks_G_Click element "//button[@type='submit']"
  Then Aleks_G_Wait 2 seconds
  Then Verify page by title "Profotolizer - Projects"

Scenario: Login with invalid password
  Given Aleks_G_Open "https://www.profitolizer.com"
  Then Aleks_G_Click element "//a[text()='Login']"
  Then Aleks_G_Type "testgmail@gmail.com" into "//input[@name='username']"
  Then Aleks_G_Type "WrongPassword" into "//input[@name='password']"
  Then Aleks_G_Click element "//button[@type='submit']"
  Then Aleks_G_Wait 2 seconds
  Then Verify presents of element "//p[text()='Invalid username or password']"

Scenario: Login with empty username field
  Given Aleks_G_Open "https://www.profitolizer.com"
  Then Aleks_G_Click element "//a[text()='Login']"
  Then Aleks_G_Type "PasswordTest" into "//input[@name='password']"
  Then Aleks_G_Click element "//button[@type='submit']"
  Then Aleks_G_Wait 2 seconds
  Then Verify presents of element "//div[text()='Email is required']"

Scenario: Restore password for registered email
  Given Aleks_G_Open "https://www.profitolizer.com"
  Then Aleks_G_Click element "//a[text()='Login']"
  Then Aleks_G_Wait 2 seconds
  Then Aleks_G_Click element "//a[text()='Forgot password?']"
  Then Aleks_G_Wait 2 seconds
  Then Aleks_G_Type "test@test.com" into "//input[@class]"
  Then Aleks_G_Click element "//button[text()=' Send']"
  Then Aleks_G_Wait 2 seconds
  Then Verify presents of element "//h5[contains(text(),'Restore Password')]"