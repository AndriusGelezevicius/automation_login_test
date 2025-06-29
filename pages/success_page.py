from selenium.webdriver.common.by import By

class SuccessPage:
    def __init__(self, driver): # driver - kad klasė galėtų atlikti veiksmus puslapyje
        self.driver = driver
        self.message_header = (By.TAG_NAME, "h1")
        self.logout_button = (By.LINK_TEXT, "Log out")

    def get_message_header(self):
        return self.driver.find_element(*self.message_header).text

    def is_logout_button_displayed(self):
        return self.driver.find_element(*self.logout_button).is_displayed()

