from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.new_quote_btn = self.page.get_by_role("button", name="Start New Quote")
        self.new_quote_heading = self.page.get_by_role("heading", name="Generate a New Quote")

    def navigate(self, url: str):
        self.page.goto(url)
        self.page.wait_for_load_state("domcontentloaded")

    def click_new_quote_button(self):
        expect(self.new_quote_heading).to_be_visible()
        expect(self.new_quote_btn).to_be_visible()
        expect(self.new_quote_btn).to_be_enabled()
        self.new_quote_btn.click()