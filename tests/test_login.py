from pages.login_page import LoginPage

def test_login_com_sucesso(page):
    login_page = LoginPage(page)
    login_page.go_to("https://front.serverest.dev/login")
    login_page.login("fulano@qa.com", "teste")  # Credenciais públicas do ambiente Serverest

    assert login_page.is_logged_in()
