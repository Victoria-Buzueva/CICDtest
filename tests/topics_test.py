import allure
import pytest
import time
from base.base_test import BaseTest


@allure.feature("Topics")
class TestTopics(BaseTest):
    @allure.title("Create topic")
    @allure.severity("Critical")
    @pytest.mark.smoke
    @pytest.mark.usefixtures("login_open_project_logout")
    def test_user_create_topic(self):
        topic_name = "demo " + str(time.time())
        self.topics_page.click_add_topic_button()
        self.topics_page.enter_topic_name(topic_name)
        self.topics_page.click_ok_button_in_creating_window()
        self.topics_page.topic_is_appeared_at_list(topic_name)
        self.topics_page.topic_is_opened(topic_name)
        self.topics_page.make_screenshot("Succsess")
