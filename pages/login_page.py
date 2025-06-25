from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.email_input = page.locator('[data-testid="email"]')
        self.password_input = page.locator('[data-testid="senha"]')
        self.login_button = page.locator('[data-testid="entrar"]')

    def login(self, email: str, senha: str):
        self.email_input.fill(email)
        self.password_input.fill(senha)
        self.login_button.click()

    def is_logged_in(self):
        # Aguarda redirecionamento e verifica se a URL contém /home
        self.page.wait_for_url("**/home")
        return "/home" in self.page.url
