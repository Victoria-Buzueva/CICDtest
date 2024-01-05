

class LoginPageLocators:
    LOGIN_USERNAME = ("xpath", "//label[text()='Email address']/following-sibling::div//input")
    LOGIN_PASSWORD = ("xpath", "//label[text()='Password']/following-sibling::div//input")
    LOGIN_SUBMIT_BUTTON = ("xpath", "//button/span[text()='Sign in']")

class MenuLocators:
    # Top menu locators
    MY_PROJECTS_BUTTON = ("xpath", "//a[@href='/projects']")
    EMAIL_BUTTON = ("xpath", "//div[@aria-controls='myprofile-menu']")
    LOGOUT_BUTTON = ("xpath", "//li[text()='Log out']")

    # Open project button
    NAME_OF_MY_PROJECT_BUTTON = ("xpath", "//p[@id='projectName']")

class TopicsLocators:
    # Create topic locators
    CREATE_NEW_TOPIC_BUTTON = ("xpath", "//button[contains(@class,'List_addButton__gr0ex')]")
    CREATE_TOPIC_NAME = ("xpath", "//textarea[@id='addTopicInput']")
    CREATE_TOPIC_COVER = ("xpath", "//input[@id='topic-imageundefined']")
    CREATE_TOPIC_COVER_PICTURE = ("xpath", "//label[@for='topic-imageundefined']//img[@src and @width and @height]")
    CREATE_TOPIC_OK_BUTTON = ("xpath", "//button/span[text()='Create']")
    CREATE_TOPIC_CANCEL_BUTTON = ("xpath", "//button/span[text()='Cancel']")
    # Topic window locators
    TOPIC_NAME_IN_NAVBAR = ("xpath", "//nav//h5")

