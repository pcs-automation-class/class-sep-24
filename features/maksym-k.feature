Feature: Test login functionality
# Some login functionality tests
  
  
  Scenario: Play with login functionality
    Given Open "https://www.profitolizer.com/"
    Then Wait 2 seconds
    Then Click element "//a[@class='header-link _btn__link']"
    Then Wait 1 seconds
    Then Click element "//button[@class='btn btn-primary w-100']"
    Then Wait 1 seconds
    Then Verify presents of element "//div[text()='Email is required']"
    Then Wait 1 seconds
    Then Verify presents of element "//div[text()='Password is required']"
    Then Wait 1 seconds
    Then Click element "//a[text()='Forgot password?']"
    Then Wait 1 seconds
    Then Verify presents of element "//h5[text()='Restore Password']"
    Then Wait 1 seconds
    Then Type "test@mail.com" into "//input[@class='el-input__inner']"
    Then Wait 1 seconds
    Then Click element "//button[text()=' Send']"
    Then Wait 1 seconds
    Then Verify presents of element "//h5[contains(text(), 'Please check your inbox')]"
    Then Wait 1 seconds
    Then Click element "//a[@href='https://profitolizer.com/']"
    Then Wait 1 seconds