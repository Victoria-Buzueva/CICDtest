import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from config.locators import MenuLocators


class MyProjectsPage(BasePage):
    PAGE_URL = Links.MY_PROJECTS_PAGE

    @allure.step("Click on 'My projects' button in top menu")
    def open_my_projects_page(self):
        self.wait.until(EC.element_to_be_clickable(MenuLocators.MY_PROJECTS_BUTTON)).click()

    @allure.step("Click on 'NAME_OF_MY_PROJECT' button")
    def open_my_project(self):
        self.wait.until(EC.element_to_be_clickable(MenuLocators.NAME_OF_MY_PROJECT_BUTTON)).click()
