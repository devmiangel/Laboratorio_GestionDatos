from pages.login_page import LoginPage

def test_home(driver):
    assert "Swag Labs" in driver.title


def test_login(driver):
    login = LoginPage(driver)
    login.login('standard_user', 'secret_sauce')
    
    assert 'inventory' in driver.page_source

