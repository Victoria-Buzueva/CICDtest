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
        self.topics_page.topic_is_opened(topic_name)
        self.topics_page.make_screenshot("Succsess")

    @pytest.mark.skip
    @allure.title("Create topic with cover")
    @allure.severity("Normal")
    @pytest.mark.smoke
    @pytest.mark.usefixtures("login_open_project_logout")
    def test_user_create_topic_with_cover(self):
        topic_name = "demo " + str(time.time())
        self.topics_page.click_add_topic_button()
        self.topics_page.enter_topic_name_in_create_topic_window(topic_name)
        self.topics_page.add_cover_in_create_topic_window()
        self.topics_page.click_ok_button_in_create_topic_window()
        self.topics_page.topic_is_appeared_at_list(topic_name)
        self.topics_page.topic_has_cover(topic_name)
        self.topics_page.topic_is_opened(topic_name)
        self.topics_page.make_screenshot("Succsess")


