import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
import time
from config.locators import TopicsLocators


class TopicsPage(BasePage):
    PAGE_URL = Links.TOPICS_PAGE

    @allure.step("Create new topic without cover")
    def create_new_topic_without_cover(self):
        self.wait.until(EC.element_to_be_clickable(TopicsLocators.CREATE_NEW_TOPIC_BUTTON)).click()
        topic_name = "demo " + str(time.time())
        with allure.step(f"Create '{topic_name}' topic"):
            self.wait.until(EC.element_to_be_clickable(TopicsLocators.CREATE_TOPIC_NAME)).send_keys(topic_name)
            self.wait.until(EC.element_to_be_clickable(TopicsLocators.CREATE_TOPIC_OK_BUTTON)).click()
