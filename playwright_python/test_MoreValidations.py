import time

from playwright.sync_api import Page, expect


def test_UIChecks(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    page.on("dialog", lambda dialog: dialog.accept())
    page.locator("//input[@id='confirmbtn']").click()

    page.locator("//button[@id='mousehover']").hover()
    page.locator("//a[text()='Top']").click()
    time.sleep(3)

    pageFrame = page.frame_locator("//iframe[@id='courses-iframe']")
    pageFrame.locator("//nav[@class='main-menu']//a[text()='All Access plan']").first.click()
    expect (pageFrame.locator("body")).to_contain_text("Happy Subscibers!")
    time.sleep(5)

def test_tablePrice(page: Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    tableHeader = page.locator("th")
    for i in range(tableHeader.count()):
        if tableHeader.nth(i).filter(has_text= "Price").count() > 0:
            colValue = tableHeader.nth(i).text_content()
            print(f"Price column value {colValue}")
            break
    riceRow = page.locator("tr").filter(has_text= "Rice")
    expect (riceRow.locator("//td[2]")).to_have_text("37")

    # tableRows = page.locator("//table[contains(@class,'table-bordered')]//tr")
    # for i in range(tableRows.count()):
    #     row = tableRows.nth(i)
    #     cell_text = row.locator("td").first.text_content()
    #
    #     if cell_text == "Rice":
    #         priceValue = row.locator("td").nth(1).text_content()
    #         priceValue = int(priceValue)
    #         if priceValue == 37:
    #             print("Value of Rice is still 37.")
    #             break