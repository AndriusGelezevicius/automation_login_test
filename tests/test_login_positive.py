from pages.login_page import LoginPage
from pages.success_page import SuccessPage

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open("https://practicetestautomation.com/practice-test-login/")
    login_page.enter_username("student")
    login_page.enter_password("Password123")
    login_page.click_submit()

    success_page = SuccessPage(driver)
    assert "logged-in-successfully" in driver.current_url
    assert "Successfully" in success_page.get_message_header()
    assert success_page.is_logout_button_displayed()