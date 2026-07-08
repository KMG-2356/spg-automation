from playwright.sync_api import Page, expect

class QuotePage:
    def __init__(self, page: Page):
        self.page = page
        # ADD LOCATORS HERE LIKE BELOW EXAMPLE
        # self.username_input = "input[name='username']"

    def navigate(self, url: str):
        self.page.goto(url)
        self.page.wait_for_load_state("domcontentloaded")

    # ADD METHODS HERE LIKE BELOW EXAMPLE
    # def login(self, username: str, password: str):


