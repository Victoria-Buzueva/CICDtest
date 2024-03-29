

class LoginPageLocators:
    LOGIN_USERNAME = ('xpath', '//label[text()="Email address"]/following-sibling::div//input')
    LOGIN_PASSWORD = ('xpath', '//label[text()="Password"]/following-sibling::div//input')
    LOGIN_SUBMIT_BUTTON = ('xpath', '//button/span[text()="Sign in"]')

class MenuLocators:
    # Top menu locators
    MY_PROJECTS_BUTTON = ('xpath', '//a[@href="/projects"]')
    EMAIL_BUTTON = ('xpath', '//div[@aria-controls="myprofile-menu"]')
    LOGOUT_BUTTON = ('xpath', '//li[text()="Log out"]')

    # Open project button
    NAME_OF_MY_PROJECT_BUTTON = ('xpath', '//p[@id="projectName"]')

class TopicsLocators:
    # Create topic locators
    CREATE_NEW_TOPIC_BUTTON = ('xpath', '//button[contains(@class,"List_addButton__gr0ex")]')
    CREATE_TOPIC_NAME = ('xpath', '//textarea[@id="addTopicInput"]')
    CREATE_TOPIC_COVER = ('xpath', '//input[@id="topic-imageundefined"]')
    CREATE_TOPIC_COVER_PICTURE = ('xpath', '//label[@for="topic-imageundefined"]//img[@src and @width and @height]')
    CREATE_TOPIC_OK_BUTTON = ('xpath', '//button/span[text()="Create"]')
    CREATE_TOPIC_CANCEL_BUTTON = ('xpath', '//button/span[text()="Cancel"]')
    # Topic navbar locators
    TOPIC_NAME_IN_NAVBAR = ('xpath', '//nav//h5')
    TOPIC_SETTINGS_BUTTON = ('xpath', '//div[@style="overflow: hidden;"]')
    # Topic profile locators
    TOPIC_PROFILE_NAME = ('xpath', '//h3')
    TOPIC_PROFILE_BACK_BUTTON = ('xpath', '//button[.//*[@width="22" and @height="22"]]')
    TOPIC_EDIT_BUTTON = ('xpath', '//button/span[text()="Edit topic"]')
    TOPIC_DELETE_BUTTON = ('xpath', '//button/span[text()="Delete topic"]')
    # Topic delete alert locators
    TOPIC_DELETE_ALERT_YES_BUTTON = ('xpath', '//button/span[text()="Yes"]')
    TOPIC_DELETE_ALERT_CANCEL_BUTTON = ('xpath', '//button/span[text()="Cancel"]')
    # Topic edit alert locators
    EDIT_TOPIC_NAME_FIELD = ('xpath', '//textarea[@id="addTopicInput"]')
    TOPIC_EDIT_ALERT_SAVE_BUTTON = ('xpath', '//button/span[text()="Save"]')
    TOPIC_EDIT_ALERT_CANCEL_BUTTON = ('xpath', '//button/span[text()="Cancel"]')
    # Topic search locators
    TOPIC_SEARCH_BUTTON = ('xpath', '//button[.//*[@width="20" and @height="20"]]')
    TOPIC_SEARCH_FIELD = ('xpath', '//input[@placeholder = "Search..."]')
    TOPIC_SEARCH_CLEAR_BUTTON = ('xpath', '//button[.//*[@width="20" and @height="20"]]')
    TOPIC_SEARCH_BACK_BUTTON = ('xpath', '//button[.//*[@width="1em" and @height="1em"]]')
    TOPIC_SEARCH_TOPIC_RESULT_BOLD = ('xpath', '//div[@class="TopicStyles_shortText__r+LnB"]/b')
    TOPIC_SEARCH_TOPIC_RESULT = ('xpath', '//div[@class="TopicStyles_shortText__r+LnB"]')
    TOPIC_SEARCH_COMMENT_RESULT_BOLD = ('xpath', '//div[@class="MuiGrid-root MuiGrid-container MuiGrid-wrap-xs-nowrap"]//b')
    TOPIC_SEARCH_COMMENT_RESULT = ('xpath', '//div[@class="MuiGrid-root MuiGrid-container MuiGrid-wrap-xs-nowrap"]//b/..')
    TOPIC_EMPTY_SEARCH_PICTURE = ('xpath', '//img[@src="/img/shock_smile.png"]')
    TOPIC_EMPTY_SEARCH_TITLE = ('xpath', '//p[text()="No results found"]')
    # Comment locators
    COMMENT_INPUT_FIELD = ('xpath', '//textarea[@id="messageInput"]')
    COMMENT_SEND_BUTTON = ('xpath', '//button[.//*[@width="40" and @height="40"]]')
    COMMENT_TEXT = ('xpath', '//div[@style="white-space: pre-wrap; word-break: break-word;"]')
    LAST_COMMENT = ('xpath', '(//div[@style="white-space: pre-wrap; word-break: break-word;"])[last()]')
    LAST_COMMENT_EDIT_BUTTON = ('xpath', '(//button[.//*[@width="12" and @height="12"]])[last()]')
    LAST_COMMENT_DELETE_BUTTON = ('xpath', '(//button[.//*[@width="12" and @height="12"]])[last()-1]')
    LAST_COMMENT_EDIT_OK_BUTTON = ('xpath', '//button[.//*[@width="18" and @height="18"]]')
    COMMENT_DELETE_ALERT_OK_BUTTON = ('xpath', '//button/span[text()="Yes"]')
    EDIT_FIELD = ('xpath', '//textarea[@id="editableText"]')
