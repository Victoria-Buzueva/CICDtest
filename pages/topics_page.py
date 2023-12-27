import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
import time


class TopicsPage(BasePage):
    PAGE_URL = Links.TOPICS_PAGE
    CREATE_NEW_TOPIC_BUTTON = ("xpath", "/html/body/div[1]/div[1]/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div[2]/button")
    CREATE_TOPIC_NAME = ("xpath", "/html/body/div[6]/div[3]/div/div/div/div/div[1]/div[2]/div/div/textarea[1]")
    CREATE_TOPIC_COVER = ("xpath", "/html/body/div[6]/div[3]/div/div/div/div/div[1]/div[1]/div/input")
    CREATE_TOPIC_OK_BUTTON = ("xpath", "/html/body/div[6]/div[3]/div/div/div/div/div[3]/button[2]")

    @allure.step("Create new topic without cover")
    def create_new_topic_without_cover(self):
        self.wait.until(EC.element_to_be_clickable(self.CREATE_NEW_TOPIC_BUTTON)).click()
        topic_name = "demo " + str(time.time())
        with allure.step(f"Create '{topic_name}' topic"):
            self.wait.until(EC.element_to_be_clickable(self.CREATE_TOPIC_NAME)).send_keys(topic_name)
            self.wait.until(EC.element_to_be_clickable(self.CREATE_TOPIC_OK_BUTTON)).click()