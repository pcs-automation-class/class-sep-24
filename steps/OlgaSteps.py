from time import sleep

from behave import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@step('Open "{url}"')
def open_url(context, url):
    context.driver.get(url)



# @And("at least one {string} element should contain the text {string}")
#
#
# public void at_least_one_element_should_contain_the_text(String element, String text) {
#     List < WebElement > elements = getDriver().findElements(By.xpath("//" + element));
#     boolean found = elements.stream().anyMatch(el -> el.getText().contains(text));
#     Assert.assertTrue("Text '" + text + "' not found in any <" + element + "> element", found);
# }