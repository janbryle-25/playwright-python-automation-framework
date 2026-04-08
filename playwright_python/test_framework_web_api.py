import json
import time

import pytest
from playwright.sync_api import Playwright, expect

from pageObjects.login import LoginPage
from utils.apiBase import APIUtils

with open("data/credentials.json") as f:
    jsonData = json.load(f)
    print(jsonData)
    user_credentials_list = jsonData["user_credentials"]

@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_e2e_web_api(playwright: Playwright, user_credentials):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()



    #create order -> orderId
    api_utils = APIUtils()
    order_id = api_utils.createOrder(playwright, user_credentials)

    loginPage = LoginPage(page)
    #login
    username = user_credentials['userEmail']
    password = user_credentials['userPassword']
    loginPage.navigate()
    dashboardPage = loginPage.login(username, password)

    #order History Page -> order is present
    orderHistoryPage = dashboardPage.goToOrders()

    ordersDetailsPage = orderHistoryPage.select_orders(order_id)
    ordersDetailsPage.verifyOrderMessage()


    # rowNeeded = page.locator(f"//tr[th[contains(text(), '{order_id}')]]")
    # rowNeeded.locator("xpath=.//td/button[contains(text(),'View')]").click()
    # expect(page.locator("//p[@class='tagline']")).to_have_text('Thank you for Shopping With Us')


    time.sleep(3)

