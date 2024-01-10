import allure
import pytest
import random
import os
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
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
    def topic_is_appeared_at_list(self):
        # self.make_screenshot("Succsess")
        NEW_TOPIC_LOCATOR = ("xpath", f"//h5[@class='TopicStyles_shortText__r+LnB' and text()='{self.topic_name}']")
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
    def last_comment_has_text(self):
        self.wait.until(EC.text_to_be_present_in_element(TopicsLocators.LAST_COMMENT, self.new_comment))
        # element_text = self.wait.until(EC.presence_of_element_located(TopicsLocators.LAST_COMMENT))
        # assert element_text.text == self.new_comment, "Last comment text does not match the expectation"
        # print(f"/{element_text.text}/")
        # print(f"/{self.new_comment}/")

    @allure.step('Click send comment button')
    def click_send_comment_button(self):
        send_comment_button = self.wait.until(EC.element_to_be_clickable(TopicsLocators.COMMENT_SEND_BUTTON))
        send_comment_button.click()

    @allure.step('Click last comment edit button')
    def click_last_comment_edit_button(self):
        last_comment_edit_button = self.wait.until(EC.element_to_be_clickable(TopicsLocators.LAST_COMMENT_EDIT_BUTTON))
        last_comment_edit_button.click()

    @allure.step('Clear edit comment text field')
    def clear_edit_comment_text_field(self):
        edit_field = self.wait.until(EC.element_to_be_clickable(TopicsLocators.EDIT_FIELD))
        edit_field.send_keys(Keys.COMMAND + "A")
        edit_field.send_keys(Keys.BACKSPACE)
        assert edit_field.get_attribute("value") == "", "There is a text after clear edit comment field"

    @allure.step('Enter text in edit comment field')
    def enter_edit_comment(self):
        edit_field = self.wait.until(EC.element_to_be_clickable(TopicsLocators.EDIT_FIELD))
        self.new_comment = "edited"
        edit_field.send_keys(self.new_comment)

    @allure.step('Click edit OK button')
    def click_edit_ok_button(self):
        edit_ok_button = self.wait.until(EC.element_to_be_clickable(TopicsLocators.LAST_COMMENT_EDIT_OK_BUTTON))
        edit_ok_button.click()

    @allure.step("Click last comment delete button")
    def click_last_comment_delete_button(self):
        last_comment_delete_button = self.wait.until(EC.element_to_be_clickable(TopicsLocators.LAST_COMMENT_DELETE_BUTTON))
        last_comment_delete_button.click()

    @allure.step("Click YES button in delete alert")
    def click_comment_delete_alert_yes_button(self):
        yes_button = self.wait.until(EC.element_to_be_clickable(TopicsLocators.COMMENT_DELETE_ALERT_OK_BUTTON))
        yes_button.click()

    @allure.step("Check if the topic has not comments")
    def check_topic_has_not_comments(self):
        self.wait.until(EC.invisibility_of_element_located(TopicsLocators.COMMENT_TEXT))

    @allure.step('Click topic settings button')
    def click_topic_settings_button(self):
        settings_button = self.wait.until(EC.element_to_be_clickable(TopicsLocators.TOPIC_SETTINGS_BUTTON))
        settings_button.click()

    @allure.step('Click topic edit button')
    def click_topic_edit_button(self):
        edit_button = self.wait.until(EC.element_to_be_clickable(TopicsLocators.TOPIC_EDIT_BUTTON))
        edit_button.click()

    @allure.step('Clear edit topic field')
    def clear_edit_topic_field(self):
        edit_field = self.wait.until(EC.element_to_be_clickable(TopicsLocators.EDIT_TOPIC_NAME_FIELD))
        edit_field.send_keys(Keys.COMMAND + "A")
        edit_field.send_keys(Keys.BACKSPACE)
        assert edit_field.get_attribute("value") == "", "There is a text after clear edit topic field"

    @allure.step('Enter text in edit topic field')
    def enter_edit_topic_name(self):
        edit_field = self.wait.until(EC.element_to_be_clickable(TopicsLocators.EDIT_TOPIC_NAME_FIELD))
        self.topic_name = "edited"
        edit_field.send_keys(self.topic_name)

    @allure.step('Click save button in edit topic alert')
    def click_topic_edit_alert_save_button(self):
        save_button = self.wait.until(EC.element_to_be_clickable(TopicsLocators.TOPIC_EDIT_ALERT_SAVE_BUTTON))
        save_button.click()

    @allure.step('Check topic name in topic profile')
    def check_profile_topic_name(self):
        self.wait.until(EC.text_to_be_present_in_element(TopicsLocators.TOPIC_PROFILE_NAME, self.topic_name))
        new_topic_name = self.wait.until(EC.presence_of_element_located(TopicsLocators.TOPIC_PROFILE_NAME))
        assert new_topic_name.text == self.topic_name, "Edited topic did not change name"

    @allure.step('Click back button in topic profile')
    def click_topic_proile_back_button(self):
        back_button = self.wait.until(EC.element_to_be_clickable(TopicsLocators.TOPIC_PROFILE_BACK_BUTTON))
        back_button.click()

    @allure.step('Click topic delete button')
    def click_topic_delete_button(self):
        delete_button = self.wait.until(EC.element_to_be_clickable(TopicsLocators.TOPIC_DELETE_BUTTON))
        delete_button.click()

    @allure.step('Click topic yes button in topic delete alert')
    def click_topic_delete_alert_yes_button(self):
        yes_button = self.wait.until(EC.element_to_be_clickable(TopicsLocators.TOPIC_DELETE_ALERT_YES_BUTTON))
        yes_button.click()

    @allure.step('Check if the deleted topic disappear from the topic list')
    def topic_is_disappear_from_topic_list(self):
        DELETE_TOPIC_LOCATOR = ("xpath", f"//h5[@class='TopicStyles_shortText__r+LnB' and text()='{self.topic_name}']")
        self.wait.until(EC.invisibility_of_element_located(DELETE_TOPIC_LOCATOR))

    @allure.step("Click e-mail button in Top menu")
    def click_email_button_in_top_menu(self):
        email_button = self.wait.until(EC.element_to_be_clickable(MenuLocators.EMAIL_BUTTON))
        email_button.click()

    @allure.step("Click logout button in Top menu")
    def click_logout_button_in_top_menu(self):
        logout_button = self.wait.until(EC.element_to_be_clickable(MenuLocators.LOGOUT_BUTTON))
        logout_button.click()

    @allure.step("Click search topic button")
    def click_search_topic_button(self):
        search_button = self.wait.until(EC.element_to_be_clickable(TopicsLocators.TOPIC_SEARCH_BUTTON))
        search_button.click()

    @allure.step("Enter topic search")
    def enter_topic_search(self):
        topic_search = self.wait.until(EC.element_to_be_clickable(TopicsLocators.TOPIC_SEARCH_FIELD))
        self.success_topic_search = 'demo'
        topic_search.send_keys(self.success_topic_search)

    @allure.step("Check topic search result not null and contains a search string")
    def check_topic_search_result(self):
        list_search_result = self.wait.until(EC.visibility_of_any_elements_located(TopicsLocators.TOPIC_SEARCH_TOPIC_RESULT_BOLD))
        count_elements = len(list_search_result)
        assert count_elements != 0, "None of the topics were found"
        count_elements_with_search_text = 0
        for topic in list_search_result:
            topic_text_in_list = topic.text.strip()  # getting text from an element
            if self.success_topic_search == topic_text_in_list:  # checking for the presence of the "topic_search" line and increasing the counter if available
                count_elements_with_search_text += 1
        assert count_elements == count_elements_with_search_text, f'Not all found topics contain the substring {self.success_topic_search}'

    @allure.step("Enter comment search")
    def enter_comment_search(self):
        topic_search = self.wait.until(EC.element_to_be_clickable(TopicsLocators.TOPIC_SEARCH_FIELD))
        self.success_topic_search = 'comment'
        topic_search.send_keys(self.success_topic_search)

    @allure.step("Check comment search result not null and contains a search string")
    def check_comment_search_result(self):
        list_search_result = self.wait.until(EC.visibility_of_any_elements_located(TopicsLocators.TOPIC_SEARCH_COMMENT_RESULT_BOLD))
        count_elements = len(list_search_result)
        assert count_elements != 0, "None of the comments were found"
        count_elements_with_search_text = 0
        for topic in list_search_result:
            topic_text_in_list = topic.text.strip()  # getting text from an element
            if self.success_topic_search == topic_text_in_list:  # checking for the presence of the "topic_search" line and increasing the counter if available
                count_elements_with_search_text += 1
        assert count_elements == count_elements_with_search_text, f'Not all found comments contain the substring {self.success_topic_search}'

    @allure.step("Enter empty search")
    def enter_empty_search(self):
        topic_search = self.wait.until(EC.element_to_be_clickable(TopicsLocators.TOPIC_SEARCH_FIELD))
        topic_search.send_keys(str(time.time()) + str(time.time()) + str(time.time()))

    @allure.step("Check topic search has empty results")
    def check_empty_search_result(self):
        # self.wait.until(EC.invisibility_of_element_located(TopicsLocators.TOPIC_SEARCH_TOPIC_RESULT_BOLD))
        # self.wait.until(EC.invisibility_of_element_located(TopicsLocators.TOPIC_SEARCH_COMMENT_RESULT_BOLD))
        self.wait.until(EC.visibility_of_element_located(TopicsLocators.TOPIC_EMPTY_SEARCH_PICTURE))
        self.wait.until(EC.visibility_of_element_located(TopicsLocators.TOPIC_EMPTY_SEARCH_TITLE))

    @allure.step("Open random topic from search")
    def open_random_topic_from_search(self):
        list_search_result = self.wait.until(EC.visibility_of_any_elements_located(TopicsLocators.TOPIC_SEARCH_TOPIC_RESULT))
        if len(list_search_result) > 0:
            random_element = random.choice(list_search_result)
            random_element.click()
            self.wait.until(EC.text_to_be_present_in_element(TopicsLocators.TOPIC_NAME_IN_NAVBAR, random_element.text))
            topic_name = self.wait.until(EC.presence_of_element_located(TopicsLocators.TOPIC_NAME_IN_NAVBAR))
            assert topic_name.text == random_element.text, "The name of the open topic does not match the text you edited topic"

    @allure.step("Open random comment from search")
    def open_random_comment_from_search(self):
        # We get a list of the search queries in the comments
        list_search_result = self.wait.until(EC.visibility_of_any_elements_located(TopicsLocators.TOPIC_SEARCH_COMMENT_RESULT_BOLD))
        if len(list_search_result) > 0:
            # If something is found, click on a random element
            random_element = random.choice(list_search_result)
            random_element.click()
            text_of_random_element = random_element.text
            # Find the name of the topic in the comment that we clicked on
            clicked_topic_name = self.driver.execute_script(
                "var node = arguments[0];"
                "while (node) {"
                "    if (node.tagName === 'DIV' && node.querySelector('h5')) {"
                "        return node.querySelector('h5');"
                "    }"
                "    node = node.parentNode;"
                "}"
                "return null;",
                random_element
            )
            # We check that the name of the theme in the navbar corresponds to the clicked element
            self.wait.until(EC.text_to_be_present_in_element(TopicsLocators.TOPIC_NAME_IN_NAVBAR, clicked_topic_name.text))
            topic_name = self.wait.until(EC.presence_of_element_located(TopicsLocators.TOPIC_NAME_IN_NAVBAR))
            assert topic_name.text == clicked_topic_name.text, "The name of the open topic does not match clicked comment topic ame"
            # Creating a list of comment texts from an open topic
            list_of_comments = self.wait.until(EC.presence_of_all_elements_located(TopicsLocators.COMMENT_TEXT))
            # Looking for a comment that has the desired word in the text. Return the first one found.
            for comment in list_of_comments:
                comment_text = comment.text.strip()  # getting text from an element
                if text_of_random_element in comment_text:  # checking for the presence of the "demo"
                    founded_comment = comment_text
                    break
                else:
                    founded_comment = ""
        assert text_of_random_element in founded_comment, "The name of the open topic does not match the text you edited topic"
