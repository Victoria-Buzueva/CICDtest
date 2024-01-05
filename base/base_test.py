import time
import allure
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

    @pytest.fixture
    def login_open_project_logout(self, request):
        with allure.step("Login"):
            self.login_page.open()
            self.login_page.is_opened()
            self.login_page.enter_login(self.data.LOGIN)
            self.login_page.enter_password(self.data.PASSWORD)
            self.login_page.click_submit_button()
            self.my_project_page.is_opened()
        with allure.step("Open My project"):
            self.my_project_page.open_my_projects_page()
            self.my_project_page.open_my_project()
            self.topics_page.is_opened()

        with allure.step("Logout"):
            def finalizer():

                self.topics_page.click_email_button_in_top_menu()
                self.topics_page.click_logout_button_in_top_menu()
                self.login_page.is_opened()

            request.addfinalizer(finalizer)

