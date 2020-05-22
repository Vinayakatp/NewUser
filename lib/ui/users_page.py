from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class UserPage():
    def __init__(self,driver):
        self.driver = driver

    def get_add_user_button(self):
        try:
            return self.driver.find_element_by_xpath("//div[@class='components_button withPlusIcon']")
        except:
            return None

    def get_first_name_textbox(self):
        try:
            return self.driver.find_element_by_xpath("//div[@id='createUserPanel_accountInformationSection']//input[@name='firstName']")
        except:
            return None

    def get_last_name_textbox(self):
        try:
            return self.driver.find_element_by_xpath("//div[@class='userInputField lastName']/input[@id='createUserPanel_lastNameField']")
        except:
            return None

    def get_email_textbox(self):
        try:
            return self.driver.find_element_by_xpath("//div[@class='userInputField email']//input[@id='createUserPanel_emailField'] ")
        except:
            return None

    def get_access_selected(self):
        try:
            return self.driver.find_element_by_xpath("//div[@class='components_switcher small on animated']")
        except:
            return None
    def select_Date(self,date):
        try:
            return self.driver.find_element_by_xpath("//td[@class='x-date-active']//*[text()='"+date+"']")
        except:
            return None
    def get_department_dropdown(self):
        try:
            return self.driver.find_element_by_xpath("//div[@class='itemsContainer']//div[text()='HR & Finance']")
        except:
            return None
    def get_save_send_invitation_button(self):
        try:
            return self.driver.find_element_by_xpath("//div[text()='Save & Send Invitation']")
        except:
            return None

    def get_dropdown_list(self):
        try:
            return self.driver.find_element_by_xpath("//div[@class='simpleListMenuButton components_userGroupSelectorMenu emptyList notEmpty']")
        except:
            return None

    def wait_for_add_user_to_load(self):
        wait = WebDriverWait(driver=self.driver,timeout=30)
        #wait.until(expected_conditions.visibility_of(self.get_add_user_button()))
        wait.until(expected_conditions.visibility_of(self.get_first_name_textbox()))
        wait.until(expected_conditions.visibility_of(self.get_last_name_textbox()))
        wait.until(expected_conditions.visibility_of(self.get_email_textbox()))