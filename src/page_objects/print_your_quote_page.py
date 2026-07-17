from playwright.sync_api import Page, expect
from utils.helpers import write_excel_cell, get_num

class PrintYourQuotePage:
    def __init__(self, page: Page):
        self.page = page
        self.total_premium_text = self.page.get_by_text("Total Premium: $").first
        self.total_fee_text = self.page.get_by_text("Total Fees: $")
        self.grand_total_text = self.page.get_by_text("Grand Total: $")
        self.total_tax_text = self.page.get_by_text("Total Tax: $")
        self.quote_number_text = self.page.get_by_text("#")

    def save_premium(self, data, output_filename):
        grand_total = get_num(self.grand_total_text.inner_text())
        total_fee = get_num(self.total_fee_text.inner_text())
        total_premium = get_num(self.total_premium_text.inner_text())
        total_tax = get_num(self.total_tax_text.inner_text())
        quote_number = get_num(self.quote_number_text.inner_text())

        print(f"grand_total: {grand_total}, total_fee: {total_fee}, total_premium: {total_premium}, total_tax: {total_tax}, quote_number: {quote_number}")

        write_excel_cell(f"src/data/output/{output_filename}.xlsx", "Output", row_value=data["01_Policy_Info"][0]["Test ID"], column_name="Quote Number", data=quote_number)
        write_excel_cell(f"src/data/output/{output_filename}.xlsx", "Output", row_value=data["01_Policy_Info"][0]["Test ID"], column_name="Total Premium", data=total_premium)
        write_excel_cell(f"src/data/output/{output_filename}.xlsx", "Output", row_value=data["01_Policy_Info"][0]["Test ID"], column_name="Total Fee", data=total_fee)
        write_excel_cell(f"src/data/output/{output_filename}.xlsx", "Output", row_value=data["01_Policy_Info"][0]["Test ID"], column_name="Total Tax", data=total_tax)
        write_excel_cell(f"src/data/output/{output_filename}.xlsx", "Output", row_value=data["01_Policy_Info"][0]["Test ID"], column_name="Grand Total", data=grand_total)


