import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    PAGE_URL = Links.LOGIN_PAGE
    LOGIN_USERNAME = ("xpath", "/html/body/div[1]/div[1]/div/div[1]/div/div/div/input")
    LOGIN_PASSWORD = ("css selector", ".MuiInputBase-input.MuiOutlinedInput-input.MuiInputBase-inputAdornedEnd.MuiOutlinedInput-inputAdornedEnd")
    LOGIN_SUBMIT_BUTTON = ("xpath", "/html/body/div[1]/div[1]/div/button[1]/span[1]")

    @allure.step("Enter login")
    def enter_login(self, login):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_USERNAME)).send_keys(login)

    @allure.step("Enter password")
    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_PASSWORD)).send_keys(password)

    @allure.step("Click submit button")
    def click_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_SUBMIT_BUTTON)).click()
