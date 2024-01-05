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

    @allure.step("Click add topic button")
    def click_add_topic_button(self):
        add_topic_button = self.wait.until(EC.element_to_be_clickable(TopicsLocators.CREATE_NEW_TOPIC_BUTTON))
        add_topic_button.click()

    @allure.step("Enter new topic name")
    def enter_topic_name(self, topic_name):
        enter_topic_name = self.wait.until(EC.element_to_be_clickable(TopicsLocators.CREATE_TOPIC_NAME))
        enter_topic_name.send_keys(topic_name)

    @allure.step("Click OK button on topic create window")
    def click_ok_button_in_creating_window(self):
        ok_button = self.wait.until(EC.element_to_be_clickable(TopicsLocators.CREATE_TOPIC_OK_BUTTON))
        ok_button.click()

    @allure.step("Check if the topic appear at the list")
    def topic_is_appeared_at_list(self, topic_name):
        NEW_TOPIC_LOCATOR = ("xpath", f"//h5[@class='TopicStyles_shortText__r+LnB' and text()='{topic_name}']")
        self.wait.until(EC.visibility_of_element_located(NEW_TOPIC_LOCATOR))

    @allure.step("Check if the topic opened")
    def topic_is_opened(self, topic_name):
        new_topic_name = self.wait.until(EC.presence_of_element_located(TopicsLocators.TOPIC_NAME_IN_NAVBAR))
        assert new_topic_name.text == topic_name, "Created topic is not opened"

    @allure.step("Click e-mail button in Top menu")
    def click_email_button_in_top_menu(self):
        email_button = self.wait.until(EC.element_to_be_clickable(MenuLocators.EMAIL_BUTTON))
        email_button.click()

    @allure.step("Click logout button in Top menu")
    def click_logout_button_in_top_menu(self):
        logout_button = self.wait.until(EC.element_to_be_clickable(MenuLocators.LOGOUT_BUTTON))
        logout_button.click()
