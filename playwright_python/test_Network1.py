import time

from playwright.sync_api import Page

fakePayloadOrderResponse = {"data":[],"message":"No Orders"}

def intercept_response(route):
    route.fulfill(
        json = fakePayloadOrderResponse
    )

def test_Network1(page: Page):
    page.goto("https://rahulshettyacademy.com/client/")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    page.locator("//input[@id='userEmail']").fill('nuzumaki@gmail.com')
    page.locator("//input[@id='userPassword']").fill('Naruto_123')
    page.locator("//input[@id='login']").click()
    page.locator("//button[contains(text(), 'ORDERS')]").click()
    time.sleep(5)
    order_text = page.locator("//*[contains(@class, 'mt-4')]").text_content()
    print(order_text)