import time

from playwright.sync_api import Playwright, expect

from utils.apiBase import APIUtils


def test_e2e_web_api(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #create order -> orderId
    api_utils = APIUtils()
    order_id = api_utils.createOrder(playwright)


    #login
    page.goto('https://rahulshettyacademy.com/client/#/dashboard/myorders')
    page.locator("//input[@id='userEmail']").fill('nuzumaki@gmail.com')
    page.locator("//input[@id='userPassword']").fill('Naruto_123')
    page.locator("//input[@id='login']").click()

    #order History Page -> order is present
    page.locator("//button[contains(text(), 'ORDERS')]").click()
    rowNeeded = page.locator(f"//tr[th[contains(text(), '{order_id}')]]")
    rowNeeded.locator("xpath=.//td/button[contains(text(),'View')]").click()
    expect(page.locator("//p[@class='tagline']")).to_have_text('Thank you for Shopping With Us')


    time.sleep(3)

