from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.login_heading = self.page.get_by_role("heading", name="Rater System Login")
        self.username_input = self.page.get_by_role("textbox", name="User Name")
        self.password_input = self.page.get_by_role("textbox", name="Password")
        self.login_btn = self.page.get_by_role("button", name="Login")

    def navigate(self, url: str):
        self.page.goto(url)
        self.page.wait_for_load_state("domcontentloaded")

    def login(self, username, password):
        expect(self.login_heading).to_be_visible()
        self.username_input.fill(username)
        self.password_input.fill(password)
        expect(self.login_btn).to_be_visible()
        expect(self.login_btn).to_be_enabled()
        self.login_btn.click()
