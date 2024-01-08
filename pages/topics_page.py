import allure
import pytest
import os
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
    def enter_topic_name_in_create_topic_window(self, topic_name):
        self.topic_name = topic_name
        enter_topic_name = self.wait.until(EC.element_to_be_clickable(TopicsLocators.CREATE_TOPIC_NAME))
        enter_topic_name.send_keys(topic_name)
        self.wait.until(EC.text_to_be_present_in_element_value(TopicsLocators.CREATE_TOPIC_NAME, topic_name))

    @allure.step("Add cover")
    def add_cover_in_create_topic_window(self):
        add_cover_button = self.wait.until(EC.presence_of_element_located(TopicsLocators.CREATE_TOPIC_COVER))
        current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
        file_path = os.path.join(current_dir, 'images.jpeg')  # добавляем к этому пути имя файла
        add_cover_button.send_keys(file_path)
        self.wait.until(EC.presence_of_element_located(TopicsLocators.CREATE_TOPIC_COVER_PICTURE))

    @allure.step("Click OK button on topic create window")
    def click_ok_button_in_create_topic_window(self):
        ok_button = self.wait.until(EC.element_to_be_clickable(TopicsLocators.CREATE_TOPIC_OK_BUTTON))
        ok_button.click()

    @allure.step("Check if the created topic appear at the list")
    def topic_is_appeared_at_list(self, topic_name):
        self.make_screenshot("Succsess")
        NEW_TOPIC_LOCATOR = ("xpath", f"//h5[@class='TopicStyles_shortText__r+LnB' and text()='{topic_name}']")
        self.wait.until(EC.visibility_of_element_located(NEW_TOPIC_LOCATOR))

    @allure.step("Check if the created topic has cover")
    def topic_has_cover(self, topic_name):
        TOPIC_COVER_LOCATOR = ("xpath", f"//h5[@class='TopicStyles_shortText__r+LnB' and text()='{topic_name}']/ancestor::div[@class='TopicStyles_title__2AiDc']//img[@class='MuiAvatar-img' and @src]")
        self.wait.until(EC.visibility_of_element_located(TOPIC_COVER_LOCATOR))

    @allure.step("Check if the created topic is opened")
    def topic_is_opened(self):
        new_topic_name = self.wait.until(EC.presence_of_element_located(TopicsLocators.TOPIC_NAME_IN_NAVBAR))
        assert new_topic_name.text == self.topic_name, "Created topic is not opened"

    @allure.step('Enter text comment')
    def enter_text_comment(self, new_comment):
        self.new_comment = new_comment
        enter_comment_field = self.wait.until(EC.element_to_be_clickable(TopicsLocators.COMMENT_INPUT_FIELD))
        enter_comment_field.send_keys(new_comment)
        self.wait.until(EC.text_to_be_present_in_element_value(TopicsLocators.COMMENT_INPUT_FIELD, new_comment))

    @allure.step('Check if last comment has sended text')
    def last_comment_has_text(self, new_comment):
        self.wait.until(EC.text_to_be_present_in_element(TopicsLocators.LAST_COMMENT, new_comment))

    @allure.step('Click send comment button')
    def click_send_comment_button(self):
        send_comment_button = self.wait.until(EC.element_to_be_clickable(TopicsLocators.COMMENT_SEND_BUTTON))
        send_comment_button.click()

    @allure.step('Click topic settings button')
    def click_topic_settings_button(self):
        settings_button = self.wait.until(EC.element_to_be_clickable(TopicsLocators.TOPIC_SETTINGS_BUTTON))
        settings_button.click()

    @allure.step('Click topic delete button')
    def click_topic_delete_button(self):
        delete_button = self.wait.until(EC.element_to_be_clickable(TopicsLocators.TOPIC_DELETE_BUTTON))
        delete_button.click()

    @allure.step('Click topic yes button in topic delete alert')
    def click_delete_alert_yes_button(self):
        yes_button = self.wait.until(EC.element_to_be_clickable(TopicsLocators.TOPIC_DELETE_ALERT_YES_BUTTON))
        yes_button.click()

    @allure.step('Check if the deleted topic disappear from the topic list')
    def topic_is_disappear_from_topic_list(self):
        DELETE_TOPIC_LOCATOR = ("xpath", f"//h5[@class='TopicStyles_shortText__r+LnB' and text()='{self.topic_name}']")
        self.wait.until(EC.invisibility_of_element_located(DELETE_TOPIC_LOCATOR))

    @allure.step('Delete created topic in the end of test')
    def delete_created_topic(self):
        self.click_topic_settings_button()
        self.click_topic_delete_button()
        self.click_delete_alert_yes_button()
        self.topic_is_disappear_from_topic_list()

    @allure.step("Click e-mail button in Top menu")
    def click_email_button_in_top_menu(self):
        email_button = self.wait.until(EC.element_to_be_clickable(MenuLocators.EMAIL_BUTTON))
        email_button.click()

    @allure.step("Click logout button in Top menu")
    def click_logout_button_in_top_menu(self):
        logout_button = self.wait.until(EC.element_to_be_clickable(MenuLocators.LOGOUT_BUTTON))
        logout_button.click()
