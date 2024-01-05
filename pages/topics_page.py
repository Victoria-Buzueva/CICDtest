import allure
import pytest
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
import time
from config.locators import TopicsLocators
from config.locators import MenuLocators


class TopicsPage(BasePage):
    PAGE_URL = Links.TOPICS_PAGE

    @allure.step("Create new topic without cover")
    def create_new_topic_without_cover(self):
        self.wait.until(EC.element_to_be_clickable(TopicsLocators.CREATE_NEW_TOPIC_BUTTON)).click()
        topic_name = "demo " + str(time.time())
        with allure.step(f"Create '{topic_name}' topic"):
            self.wait.until(EC.element_to_be_clickable(TopicsLocators.CREATE_TOPIC_NAME)).send_keys(topic_name)
            self.wait.until(EC.element_to_be_clickable(TopicsLocators.CREATE_TOPIC_OK_BUTTON)).click()

    @allure.step("Click e-mail button in Top menu")
    def click_email_button_in_top_menu(self):
        self.wait.until(EC.element_to_be_clickable(MenuLocators.EMAIL_BUTTON)).click()

    @allure.step("Click logout button in Top menu")
    def click_logout_button_in_top_menu(self):
        self.wait.until(EC.element_to_be_clickable(MenuLocators.LOGOUT_BUTTON)).click()
