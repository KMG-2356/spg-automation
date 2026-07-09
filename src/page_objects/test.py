from playwright.sync_api import sync_playwright

print("Test file started")


def test_single_input():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://rating.commund.com/")
        page.wait_for_timeout(2000)
        page.get_by_role("button", name="Start New Quote").click()
        page.locator(
            "div:nth-child(4) > .jss75 > .MuiGrid-root.jss80 > .MuiGrid-root.jss83 > .MuiSvgIcon-root"
        ).click()
        page.get_by_role("button", name="Commercial Lines Basic").click()
        page.wait_for_timeout(2000)
        page.get_by_role("button", name="Step 2 of").click()
        page.wait_for_timeout(2000)
        page.get_by_role("menuitem", name="Monoline Wind Location 1").click()

        # Fill Details
        page.wait_for_timeout(2000)
        page.get_by_role("textbox").first.fill("streets")
        page.get_by_role("textbox").nth(1).fill("street2")
        page.wait_for_timeout(5000)
        page.get_by_role("textbox").nth(2).fill("city")
        page.wait_for_timeout(5000)

        page.get_by_role("combobox").first.select_option("KY")

        # ⚠️ Agar ZIP textbox hai to fill() use karo.
        # Agar dropdown hai to select_option() hi rehne do.
        page.wait_for_timeout(2000)
        page.get_by_role("textbox").nth(3).fill("1")
        page.wait_for_timeout(5000)
        page.locator('[id="wd.locations.0.interest"]').select_option("Owner")
        page.wait_for_timeout(2000)
        page.locator('[id="wd.locations.0.dwelling_value"]').fill("1")
        page.wait_for_timeout(2000)
        page.locator('[id="wd.locations.0.contents_limit"]').fill("2")
        page.wait_for_timeout(2000)
        page.get_by_role(
            "textbox",
            description="Business Interruption Limit?",
            exact=True,
        ).fill("3")
        page.wait_for_timeout(2000)
        page.locator('[id="wd.locations.0.construction"]').select_option(
            "Joisted Masonry"
        )
        page.wait_for_timeout(2000)
        
        page.get_by_role("combobox").nth(3).select_option("no")
        page.get_by_role("combobox").nth(4).select_option("1/2 mile or less")

        page.locator('[id="wd.locations.0.roof_update"]').fill("77")
        page.locator('[id="wd.locations.0.protection_class"]').select_option("3")

        page.get_by_role(
            "spinbutton",
            description="Number of Stories?",
            exact=True,
        ).fill("122")

        page.get_by_role(
            "spinbutton",
            description="Area of Property?",
            exact=True,
        ).fill("33")

        page.get_by_role(
            "spinbutton",
            description="Year Built?",
            exact=True,
        ).fill("200")

        page.locator('[id="wd.locations.0.losses"]').select_option("yes")

        page.wait_for_timeout(15000)
        browser.close()


if __name__ == "__main__":
    test_single_input()