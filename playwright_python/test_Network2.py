import time

from playwright.sync_api import Page, expect, Playwright

from utils.apiBase import APIUtils

fakePayloadOrderResponse = {"data":[],"message":"No Orders"}

def interceptRequest(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6711e249ae2afd4c0b9f6fb0")

def test_Network2(page: Page):
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", interceptRequest)
    page.goto("https://rahulshettyacademy.com/client/")
    page.locator("//input[@id='userEmail']").fill('nuzumaki@gmail.com')
    page.locator("//input[@id='userPassword']").fill('Naruto_123')
    page.locator("//input[@id='login']").click()
    page.locator("//button[contains(text(), 'ORDERS')]").click()
    rowNeeded = page.locator(f"//tr[th[contains(text(), '69d6362bf86ba51a655253ef')]]")
    rowNeeded.locator("xpath=.//td/button[contains(text(),'View')]").click()
    expected_message = page.locator("//*[@class='blink_me']").text_content()
    print(expected_message)
    time.sleep(5)

def test_session_storage(playwright: Playwright):
    api_utils = APIUtils()
    tokenValue = api_utils.getToken(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.add_init_script(f"""localStorage.setItem("token", '{tokenValue}');""")
    page.goto("https://rahulshettyacademy.com/client/")
    page.locator("//button[contains(text(), 'ORDERS')]").click()
    expect(page.get_by_text("Your Orders")).to_be_visible()