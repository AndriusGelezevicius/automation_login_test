from pages.login_page import LoginPage
from pages.success_page import SuccessPage

def test_valid_login():
    login_page = LoginPage(driver)
    login_page.open("https://https://practicetestautomation.com/practice-test-login/")
    login_page.username_field("student")
    login_page.password_field("Password123")
    login_page.submit_button()

    success_page = SuccessPage(driver)
    assert "Successfully" in success_page.get_message_header()
    assert success_page.is_logout_button_displayed()