import pytest
from config.data import Data
from pages.login_page import LoginPage
from pages.my_projects_page import MyProjectsPage
from pages.topics_page import TopicsPage


class BaseTest:
    data: Data
    login_page: LoginPage
    my_project_page: MyProjectsPage
    topics_page: TopicsPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()
        request.cls.login_page = LoginPage(driver)
        request.cls.my_project_page = MyProjectsPage(driver)
        request.cls.topics_page = TopicsPage(driver)
