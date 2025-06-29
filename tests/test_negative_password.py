from pages.login_page import LoginPage

def test_invalid_username(driver):
    login_page = LoginPage(driver)
    login_page.open("https://practicetestautomation.com/practice-test-login/")
    login_page.enter_username("student")
    login_page.enter_password("incorrectPassword")
    login_page.click_submit()

    assert login_page.is_error_message_displayed()
    assert login_page.get_error_message() == "Your password is invalid!"