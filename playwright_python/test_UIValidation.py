import time

from playwright.sync_api import Page, expect


def test_UIValidationDynamicScript(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.locator("//input[@id='signInBtn']").click()
    iphoneProduct = page.locator("//app-card").filter(has_text="iphone X")
    iphoneProduct.locator("//button[contains(@class, 'btn')]").click()
    nokiaProduct = page.locator("//app-card").filter(has_text="Nokia Edge")
    nokiaProduct.locator("//button[contains(@class, 'btn')]").click()
    page.get_by_text("Checkout").click()
    expect(page.locator("//div[@class = 'media-body']")).to_have_count(2)
    time.sleep(1)

def test_ChildWindowHandle(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as newPage_info:
        page.locator("//a[@href='https://rahulshettyacademy.com/documents-request']").click()
        newPage = newPage_info.value
        assertionText = newPage.locator("//p[contains(@class,'red')]").text_content()
        splitTexts = assertionText.split("at ")
        finalText = splitTexts[1].split("with")
        assert finalText[0].strip() == "mentor@rahulshettyacademy.com"
