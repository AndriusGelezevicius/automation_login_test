from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "username")
        self.password_field = (By.ID, "password")
        self.submit_button = (By.ID, "submit")

    def open(self, url):
        self.driver.get(url)
    def enter_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_submit(self):
        self.driver.find_element(*self.submit_button).click()

    def is_error_message_displayed(self):
        return self.driver.find_element(By.ID, "error").is_displayed()
    def get_error_message(self):
        return self.driver.find_element(By.ID, "error").text


