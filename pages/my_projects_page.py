import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class MyProjectsPage(BasePage):
    PAGE_URL = Links.MY_PROJECTS_PAGE
    MY_PROJECTS_BUTTON = ("xpath", "/html/body/div[1]/div[1]/header/div/div[2]/a")
    DEMO_PROJECT_BUTTON = ("xpath", "/html/body/div[1]/div[1]/div/div/div/div[1]/div")

    @allure.step("Open My project")
    def open_my_progect(self):
        self.wait.until(EC.element_to_be_clickable(self.MY_PROJECTS_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(self.DEMO_PROJECT_BUTTON)).click()
