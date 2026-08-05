from playwright.sync_api import Page, expect, TimeoutError

class FinanceQuotePage:
    def __init__(self, page: Page):
        self.page = page
        self.finance_quote_heading = self.page.get_by_role("heading", name="    Finance Quote")
        self.down_payment_percent_input = self.page.locator("[id=\"finance.dp_percent\"]")
        self.number_of_payments_select = self.page.locator("[id=\"finance.payments\"]")
        self.print_your_documents_button = self.page.get_by_role("button", name="Print Your Quote Documents")
        self.loading_screen = self.page.locator(".jss53")

    def fill_finance_quote_form(self):
        # expect(self.finance_quote_heading).to_be_visible()
        if self.down_payment_percent_input.is_visible():
            self.down_payment_percent_input.fill("100")
            self.number_of_payments_select.select_option("1")
        # expect(self.print_your_documents_button).to_be_visible()
        # expect(self.print_your_documents_button).to_be_enabled()
        self.print_your_documents_button.click()


    def check_loading(self):
        try:
            self.loading_screen.wait_for(state="visible", timeout=500)
        except TimeoutError:
            pass
        self.loading_screen.wait_for(state="hidden")


