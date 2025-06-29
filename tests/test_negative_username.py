from pages.login_page import LoginPage

def test_invalid_username(driver):
    login_page = LoginPage(driver)
    login_page.open("https://practicetestautomation.com/practice-test-login/")
    login_page.enter_username("incorrectUser")
    login_page.enter_password("Password123")
    login_page.click_submit()

    assert login_page.is_error_message_displayed()
    assert "invalid" in login_page.get_error_message() # assert login_page.get_error_message() == "Your username is invalid!"