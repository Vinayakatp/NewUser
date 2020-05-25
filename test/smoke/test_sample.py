import unittest
from selenium.webdriver import Chrome
from lib.ui.login_page import LoginPage
from lib.ui.home_page import HomePage
from lib.ui.users_page import UserPage
import json



class TestSample(unittest.TestCase):

    def setUp(self):
        self.driver = Chrome("C://chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(40)
        self.driver.get("https://demo.actitime.com/")
        self.login = LoginPage(self.driver)
        self.home = HomePage(self.driver)
        self.user = UserPage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_invalid_login_TC13121(self):
        Data = json.load(open("./test/regression/login/UserStory123.json"))
        self.login.wait_for_login_page_to_load()
        self.login.get_username_textbox().send_keys(Data['TC12345']['Username1'])
        self.login.get_password_textbox().send_keys(Data['TC12345']['Password1'])
        self.login.get_login_button().click()
        actual_error_msg = self.login.get_login_error_msg().text
        expected_error_msg = "Username or Password is invalid. Please try again."
        assert actual_error_msg == expected_error_msg,"Its invalid"

    def test_Add_User(self):
        Data = json.load(open("./test/regression/login/UserStory123.json"))
        self.login.wait_for_login_page_to_load()
        self.login.get_username_textbox().send_keys(Data['TC12345']['Username'])
        self.login.get_password_textbox().send_keys(Data['TC12345']['Password'])
        self.login.get_login_button().click()
        self.home.get_users_button().click()
        self.user.get_add_user_button().click()
        self.user.wait_for_add_user_to_load()
        self.user.get_first_name_textbox().send_keys("Kushal")
        self.user.get_last_name_textbox().send_keys("R")
        self.user.get_email_textbox().send_keys("kushalr@gmail.com")
        self.user.get_dropdown_list().click()
        self.user.get_department_dropdown().click()
        self.user.get_save_send_invitation_button().click()