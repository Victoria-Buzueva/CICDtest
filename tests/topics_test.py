import allure
import pytest
import time
from base.base_test import BaseTest


@allure.feature("Topics")
class TestTopics(BaseTest):
    # @pytest.mark.skip
    @allure.title("Create topic without cover")
    @allure.severity("Critical")
    @pytest.mark.smoke
    @pytest.mark.usefixtures("login_open_project_logout")
    def test_user_create_topic_without_cover(self):
        topic_name = "demo " + str(time.time())
        self.topics_page.click_add_topic_button()
        self.topics_page.enter_topic_name_in_create_topic_window(topic_name)
        self.topics_page.click_ok_button_in_create_topic_window()
        self.topics_page.topic_is_appeared_at_list(topic_name)
        self.topics_page.topic_is_opened()
        # self.topics_page.make_screenshot("Succsess")
        self.topics_page.delete_created_topic()

    # @pytest.mark.skip
    @allure.title("Create topic with cover")
    @allure.severity("Normal")
    @pytest.mark.smoke
    @pytest.mark.usefixtures("login_open_project_logout")
    def test_user_create_topic_with_cover(self):
        self.topic_name = "demo " + str(time.time())
        self.topics_page.click_add_topic_button()
        self.topics_page.enter_topic_name_in_create_topic_window(self.topic_name)
        self.topics_page.add_cover_in_create_topic_window()
        self.topics_page.click_ok_button_in_create_topic_window()
        self.topics_page.topic_is_appeared_at_list(self.topic_name)
        self.topics_page.topic_has_cover(self.topic_name)
        self.topics_page.topic_is_opened()
        # self.topics_page.make_screenshot("Succsess")
        self.topics_page.delete_created_topic()

    # @pytest.mark.skip
    @allure.title("Add text comment")
    @allure.severity("Critical")
    @pytest.mark.smoke
    @pytest.mark.usefixtures("login_open_project_logout")
    def test_user_add_text_comment(self):
        self.test_user_create_topic_without_cover()
        self.new_comment = "comment " + str(time.time())
        self.topics_page.enter_text_comment(self.new_comment)
        self.topics_page.click_send_comment_button()
        self.topics_page.last_comment_has_text(self.new_comment)
        self.topics_page.delete_created_topic()

    # @allure.title("Edit text comment")
    # @allure.severity("Critical")
    # @pytest.mark.smoke
    # @pytest.mark.usefixtures("login_open_project_logout")
    # def test_user_edit_text_comment(self):
    #     self.test_user_add_text_comment()

        # self.topics_page.delete_created_topic()

    @allure.title("Delete topic")
    @allure.severity("Critical")
    @pytest.mark.smoke
    @pytest.mark.usefixtures("login_open_project_logout")
    def test_user_delete_topic(self):
        self.test_user_create_topic_without_cover()
        self.topics_page.click_topic_settings_button()
        self.topics_page.click_topic_delete_button()
        self.topics_page.click_delete_alert_yes_button()
        self.topics_page.topic_is_disappear_from_topic_list()





