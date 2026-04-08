import time

from playwright.sync_api import Page, expect, Playwright


def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.youtube.com/")

def test_playwrightShortCut(page: Page):
    page.goto("https://www.google.com/")

def test_coreLocators(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    expect (page.locator("//div[contains(@class, 'alert')]/strong")).to_be_visible()

def test_playwrightFirefox(playwright: Playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    # expect(page.locator("//div[contains(@class, 'alert')]/strong")).to_be_visible()
    iphoneProduct = page.locator("//app-card").filter(has_text="iphone X")
    iphoneProduct.locator("//button[contains(@class, 'btn')]").click()

# Credentials (Username: nuzumaki@gmail.com, Password: Naruto_123)
#Token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2OWMxNDBmMmY4NmJhNTFhNjUxZjc4NmMiLCJ1c2VyRW1haWwiOiJudXp1bWFraUBnbWFpbC5jb20iLCJ1c2VyTW9iaWxlIjozNDI0MjQyMzQyLCJ1c2VyUm9sZSI6ImN1c3RvbWVyIiwiaWF0IjoxNzc0MjczMDMwLCJleHAiOjE4MDU4MzA2MzB9.Jmzn4OJH0fdb1oHOThLCHD9eeo8pmBeP12H_qyg7IKA
def test_apiAutomation(page: Page):
    page.goto("https://rahulshettyacademy.com/client/auth/login")
    page.get_by_label("Username").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    expect (page.locator("//div[contains(@class, 'alert')]/strong")).to_be_visible()