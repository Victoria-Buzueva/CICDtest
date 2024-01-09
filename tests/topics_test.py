import allure
import pytest
import time
from base.base_test import BaseTest


@allure.feature("Topics")
class TestTopics(BaseTest):
    @pytest.mark.skip
    @allure.title("Create topic without cover")
    @allure.severity("Critical")
    @pytest.mark.smoke
    @pytest.mark.usefixtures("login_open_project_logout", "delete_created_topic")
    def test_user_create_topic_without_cover(self):
        topic_name = "demo " + str(time.time())
        self.topics_page.click_add_topic_button()
        self.topics_page.enter_topic_name_in_create_topic_window(topic_name)
        self.topics_page.click_ok_button_in_create_topic_window()
        self.topics_page.topic_is_appeared_at_list()
        self.topics_page.topic_is_opened()

    @pytest.mark.skip
    @allure.title("Create topic with cover")
    @allure.severity("Normal")
    @pytest.mark.smoke
    @pytest.mark.usefixtures("login_open_project_logout", "delete_created_topic")
    def test_user_create_topic_with_cover(self):
        self.topic_name = "demo " + str(time.time())
        self.topics_page.click_add_topic_button()
        self.topics_page.enter_topic_name_in_create_topic_window(self.topic_name)
        self.topics_page.add_cover_in_create_topic_window()
        self.topics_page.click_ok_button_in_create_topic_window()
        self.topics_page.topic_is_appeared_at_list()
        self.topics_page.topic_has_cover(self.topic_name)
        self.topics_page.topic_is_opened()

    @pytest.mark.skip
    @allure.title("Add text comment")
    @allure.severity("Critical")
    @pytest.mark.smoke
    @pytest.mark.usefixtures("login_open_project_logout", "create_topic_without_cover", "delete_created_topic")
    def test_user_add_text_comment(self):
        self.new_comment = "comment " + str(time.time())
        self.topics_page.enter_text_comment(self.new_comment)
        self.topics_page.click_send_comment_button()
        self.topics_page.last_comment_has_text()

    @pytest.mark.skip
    @allure.title("Edit text comment")
    @allure.severity("Critical")
    @pytest.mark.smoke
    @pytest.mark.usefixtures("login_open_project_logout", "create_topic_without_cover", "add_text_comment", "delete_created_topic")
    def test_user_edit_text_comment(self):
        self.topics_page.click_last_comment_edit_button()
        self.topics_page.clear_edit_comment_text_field()
        self.topics_page.enter_edit_comment()
        self.topics_page.click_edit_ok_button()
        self.topics_page.last_comment_has_text()

    @pytest.mark.skip
    @allure.title("Delete single comment in the topic")
    @allure.severity("Critical")
    @pytest.mark.smoke
    @pytest.mark.usefixtures("login_open_project_logout", "create_topic_without_cover", "add_text_comment", "delete_created_topic")
    def test_user_delete_single_comment(self):
        self.topics_page.click_last_comment_delete_button()
        self.topics_page.click_comment_delete_alert_yes_button()
        self.topics_page.check_topic_has_not_comments()

    @pytest.mark.skip
    @allure.title("Edit topic")
    @allure.severity("Critical")
    @pytest.mark.smoke
    @pytest.mark.usefixtures("login_open_project_logout", "create_topic_without_cover", "delete_created_topic")
    def test_user_edit_topic_name(self):
        self.topics_page.click_topic_settings_button()
        self.topics_page.click_topic_edit_button()
        self.topics_page.clear_edit_topic_field()
        self.topics_page.enter_edit_topic_name()
        self.topics_page.click_topic_edit_alert_save_button()
        self.topics_page.check_profile_topic_name()
        self.topics_page.topic_is_appeared_at_list()
        self.topics_page.click_topic_proile_back_button()

    @pytest.mark.skip
    @allure.title("Delete topic")
    @allure.severity("Critical")
    @pytest.mark.smoke
    @pytest.mark.usefixtures("login_open_project_logout", "create_topic_without_cover")
    def test_user_delete_topic(self):
        self.topics_page.click_topic_settings_button()
        self.topics_page.click_topic_delete_button()
        self.topics_page.click_topic_delete_alert_yes_button()
        self.topics_page.topic_is_disappear_from_topic_list()

    # @pytest.mark.skip
    @allure.title("Successful topic search")
    @allure.severity("Major")
    @pytest.mark.smoke
    @pytest.mark.usefixtures("login_open_project_logout")
    def test_user_success_topic_search(self):
        self.topics_page.click_search_topic_button()
        self.topics_page.enter_topic_search()
        self.topics_page.check_topic_search_result()



