class BasePage:
    def __init__(self, page):
        self.page = page

    def go_to(self, url: str):
        self.page.goto(url)

    def get_title(self):
        return self.page.title()

    def wait_for_element(self, selector: str, timeout: int = 5000):
        self.page.wait_for_selector(selector, timeout=timeout)

    def is_element_visible(self, selector: str) -> bool:
        return self.page.locator(selector).is_visible()
    
    def click(self, selector: str):
        self.page.locator(selector).click()

    def fill(self, selector: str, text: str):
        self.page.locator(selector).fill(text)

    def get_text(self, selector: str):
        return self.page.locator(selector).text_content()