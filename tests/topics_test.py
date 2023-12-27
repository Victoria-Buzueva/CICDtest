import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Topics")
class TestTopics(BaseTest):
    @allure.title("Create topic")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_admin_create_topic(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.my_project_page.is_opened()
        self.my_project_page.open_my_progect()
        # self.topics_page.is_opened()
        self.topics_page.create_new_topic_without_cover()
        self.topics_page.make_screenshot("Succsess")
