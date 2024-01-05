import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Topics")
class TestTopics(BaseTest):
    @allure.title("Create topic")
    @allure.severity("Critical")
    @pytest.mark.smoke
    @pytest.mark.usefixtures("login_open_project_logout")
    def test_admin_create_topic(self):
        self.topics_page.create_new_topic_without_cover()
        self.topics_page.make_screenshot("Succsess")
