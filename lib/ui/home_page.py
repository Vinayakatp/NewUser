from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class HomePage():

    def __init__(self,driver):
        self.driver = driver

    def get_users_button(self):
        try:
            return self.driver.find_element_by_xpath("//a[@class='content users']")
        except:
            return None
        