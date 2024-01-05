import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from config.locators import LoginPageLocators


class LoginPage(BasePage):
    PAGE_URL = Links.LOGIN_PAGE

    @allure.step("Enter login")
    def enter_login(self, login):
        self.wait.until(EC.element_to_be_clickable(LoginPageLocators.LOGIN_USERNAME)).send_keys(login)

    @allure.step("Enter password")
    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(LoginPageLocators.LOGIN_PASSWORD)).send_keys(password)

    @allure.step("Click submit button")
    def click_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(LoginPageLocators.LOGIN_SUBMIT_BUTTON)).click()
